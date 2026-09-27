from chatbot.language import detect,normalize
from chatbot.entities import extract
from chatbot.engine import ChatEngine
def test_languages():
    assert detect("hello I need my order")[0]=="en"
    assert detect("hola necesito mi pedido")[0]=="es"
    assert detect("mera order kaha hai")[0]=="hi"
def test_transliteration():
    assert normalize("plz mera order check karo").startswith("please")
def test_entities_preserved():
    e=extract("Order ORD-1234 date 2026-09-27 SKU-ABC")
    assert e["order_ids"]==["ORD-1234"]
    assert e["product_codes"]==["SKU-ABC"]
def test_low_intent_clarifies():
    r=ChatEngine().reply("test-user-low","hello")
    assert r["status"]=="clarification_required"
def test_session_isolation():
    a=ChatEngine().reply("customer-a","my order is ORD-1111")
    b=ChatEngine().reply("customer-b","my order is ORD-2222")
    assert a["session_id"]!=b["session_id"]
