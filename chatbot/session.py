import json,time,uuid
from pathlib import Path
from config import CONTEXT_MESSAGES,INACTIVITY_MINUTES,RESTORE_HOURS
from .models import Session,Message
from .entities import extract,preserve
STORE=Path("sessions.json")
def _load():
    return json.loads(STORE.read_text()) if STORE.exists() else {"sessions":{},"summaries":{}}
def _save(s): STORE.write_text(json.dumps(s,indent=2))
def get_or_create(customer_id):
    s=_load(); now=time.time(); active=None
    for x in s["sessions"].values():
        if x["customer_id"]==customer_id and x["active"]:
            if now-x["last_activity"]<=INACTIVITY_MINUTES*60: active=x; break
            x["active"]=False
    if active: return active
    recent=[x for x in s["sessions"].values() if x["customer_id"]==customer_id and now-x["last_activity"]<=RESTORE_HOURS*3600]
    if recent:
        old=max(recent,key=lambda x:x["last_activity"])
        x={"session_id":str(uuid.uuid4()),"customer_id":customer_id,"messages":[],"summary":old.get("summary",""),"language":old.get("language","en"),"last_activity":now,"active":True,"entities":old.get("entities",{})}
    else:
        x={"session_id":str(uuid.uuid4()),"customer_id":customer_id,"messages":[],"summary":"","language":"en","last_activity":now,"active":True,"entities":{}}
    s["sessions"][x["session_id"]]=x; _save(s); return x
def append(session,text,role,language):
    s=_load(); x=s["sessions"][session["session_id"]]; x["messages"].append({"role":role,"text":text,"language":language,"timestamp":time.time()}); x["messages"]=x["messages"][-CONTEXT_MESSAGES:]; x["last_activity"]=time.time(); x["active"]=True; _save(s)
def expire_sessions():
    s=_load(); now=time.time()
    for x in s["sessions"].values():
        if x["active"] and now-x["last_activity"]>INACTIVITY_MINUTES*60:
            x["active"]=False; x["summary"]=" | ".join(m["text"] for m in x["messages"][-CONTEXT_MESSAGES:])
    _save(s)
