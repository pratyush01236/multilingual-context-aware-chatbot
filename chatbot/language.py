import re
from config import SUPPORTED_LANGUAGES,LANGUAGE_CONFIDENCE_THRESHOLD
# Lightweight offline detector. Replace with a production language model/API when needed.
HINDI=set("hai hain kya mujhe mera meri chahiye order kaha kab kitna".split())
SPANISH=set("hola necesito quiero mi pedido donde cuando cuanto".split())
def normalize(text):
    text=text.strip()
    # Common transliteration normalization for conversational variants.
    replacements={"plz":"please","pls":"please","kr":"kar","karo":"karo","haii":"hai"}
    for a,b in replacements.items(): text=re.sub(r"\b"+a+r"\b",b,text,flags=re.I)
    return text
def detect(text):
    words=set(re.findall(r"[A-Za-zÀ-ÿ]+",text.lower()))
    scores={"en":0.55,"hi":0.0,"es":0.0}
    scores["hi"]=min(1.0,0.2+0.15*len(words&HINDI))
    scores["es"]=min(1.0,0.2+0.15*len(words&SPANISH))
    lang=max(scores,key=scores.get); confidence=scores[lang]
    if lang not in SUPPORTED_LANGUAGES: return "unknown",confidence
    return lang,confidence
def confident(text):
    lang,score=detect(text)
    return (lang,score) if score>=LANGUAGE_CONFIDENCE_THRESHOLD else ("unknown",score)
