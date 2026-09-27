import re
ORDER=re.compile(r"\b(?:ORD|ORDER)[-:# ]?[A-Z0-9]{3,}\b",re.I)
DATE=re.compile(r"\b(?:20\d{2}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]20\d{2})\b")
PRODUCT=re.compile(r"\b(?:SKU|PROD|MODEL)[-:# ]?[A-Z0-9_-]{2,}\b",re.I)
def extract(text):
    return {"order_ids":ORDER.findall(text),"dates":DATE.findall(text),"product_codes":PRODUCT.findall(text)}
def preserve(old,new):
    result=dict(old)
    for k,v in new.items():
        if v: result[k]=v
    return result
