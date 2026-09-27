import os
from dotenv import load_dotenv
load_dotenv()
SUPPORTED_LANGUAGES=[x.strip() for x in os.getenv("SUPPORTED_LANGUAGES","en,hi,es").split(",")]
LANGUAGE_CONFIDENCE_THRESHOLD=float(os.getenv("LANGUAGE_CONFIDENCE_THRESHOLD","0.70"))
INTENT_CONFIDENCE_THRESHOLD=float(os.getenv("INTENT_CONFIDENCE_THRESHOLD","0.70"))
CONTEXT_MESSAGES=int(os.getenv("CONTEXT_MESSAGES","10"))
INACTIVITY_MINUTES=int(os.getenv("INACTIVITY_MINUTES","30"))
RESTORE_HOURS=int(os.getenv("RESTORE_HOURS","24"))
