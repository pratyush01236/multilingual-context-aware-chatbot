from config import INTENT_CONFIDENCE_THRESHOLD
from .language import normalize,confident
from .intent import detect_intents
from .entities import extract,preserve
from .session import get_or_create,append,expire_sessions
class ChatEngine:
    def reply(self,customer_id,text):
        expire_sessions(); session=get_or_create(customer_id); text=normalize(text)
        lang,lang_conf=confident(text)
        if lang=="unknown":
            return {"status":"clarification_required","message":"Please tell me which language you prefer and clarify your request.","language_confidence":lang_conf,"session_id":session["session_id"]}
        intents=detect_intents(text); best=max(intents,key=lambda x:x[1])
        if best[1]<INTENT_CONFIDENCE_THRESHOLD:
            return {"status":"clarification_required","message":"Could you clarify what you need help with?","language":lang,"intent_confidence":best[1],"session_id":session["session_id"]}
        session["language"]=lang; session["entities"]=preserve(session.get("entities",{}),extract(text))
        append(session,text,"customer",lang)
        replies={"order_status":"I can help check the order status. Please confirm the order ID if needed.","refund":"I can help with a return or refund. Please provide the order ID.","price":"I can help with product pricing. Please provide the product code."}
        answer=replies.get(best[0],"Please clarify your request.")
        append(session,answer,"assistant",lang)
        return {"status":"ok","message":answer,"language":lang,"intent":best[0],"session_id":session["session_id"],"entities":session["entities"],"context_messages":10}
