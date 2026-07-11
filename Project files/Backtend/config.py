# =========================
# MODEL CONFIGURATION
# =========================

MODEL_NAMES = {
    "event_analysis": "distilbert-base-uncased",
    "text_generator": "gpt2",
    "conversation_generation": "gpt2"
}

# =========================
# FACT CHECK API CONFIG
# =========================
# Wikipedia API does not need a key, but your code expects this variable

FACT_CHECK_API = "wikipedia"

# =========================
# OPTIONAL SETTINGS
# =========================

APP_NAME = "Personalized Networking Assistant"
DEBUG = True