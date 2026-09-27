import re
def detect_intents(text):
    t=text.lower()
    intents=[]
    if re.search(r"order|pedido|ऑर्डर",t): intents.append(("order_status",0.85))
    if re.search(r"refund|return|devol|वापस|refund",t): intents.append(("refund",0.82))
    if re.search(r"price|precio|cost|कीमत",t): intents.append(("price",0.80))
    if not intents: intents=[("unknown",0.35)]
    return intents
