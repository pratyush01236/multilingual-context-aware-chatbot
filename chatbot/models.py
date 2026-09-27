from dataclasses import dataclass,field
from datetime import datetime
@dataclass
class Message:
    role:str
    text:str
    language:str
    timestamp:float
@dataclass
class Session:
    session_id:str
    customer_id:str
    messages:list[Message]=field(default_factory=list)
    summary:str=""
    language:str="en"
    last_activity:float=0.0
    active:bool=True
