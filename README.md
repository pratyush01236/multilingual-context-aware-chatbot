# Multilingual Context-Aware Chatbot

A configurable multilingual conversation engine for mixed-language customer conversations.

## Features
- English, Hindi and Spanish support by default; configurable language list.
- Mixed-language messages and language switching within a conversation.
- Transliteration and common spelling normalization.
- Preserves order IDs, dates and product codes.
- Retains the last 10 messages by default.
- Isolates simultaneous customer sessions by customer ID.
- Handles multiple intents and corrected entity information.
- Requests clarification when language or intent confidence is low.
- Ends active sessions after 30 minutes of inactivity.
- Restores a conversation summary when the customer returns within 24 hours.
- Starts a new session after the restore window.

## Run
python -m venv venv
pip install -r requirements.txt
Copy .env.example to .env
uvicorn app:app --reload

## API
POST /chat
Example:
{"customer_id":"customer-123","message":"Hola, necesito revisar mi pedido ORD-1234"}

customer_id isolates sessions. Responses include detected language, intent, session ID and preserved entities.

## Configuration
SUPPORTED_LANGUAGES=en,hi,es
LANGUAGE_CONFIDENCE_THRESHOLD=0.70
INTENT_CONFIDENCE_THRESHOLD=0.70
CONTEXT_MESSAGES=10
INACTIVITY_MINUTES=30
RESTORE_HOURS=24

## Production notes
The included detector is a lightweight offline reference implementation. Production deployments should use a tested multilingual language/intent model, persistent database or distributed session store, authentication, encryption and durable session storage.