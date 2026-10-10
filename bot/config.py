import os
from pathlib import Path

# Helper: Load .env file automatically without external dependencies
def _load_dotenv():
    env_paths = [
        Path.cwd() / ".env",
        Path(__file__).resolve().parent.parent / ".env",
        Path(__file__).resolve().parent / ".env"
    ]
    for p in env_paths:
        if p.exists() and p.is_file():
            try:
                with open(p, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#") or "=" not in line:
                            continue
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip("'\"")
                        if k not in os.environ:
                            os.environ[k] = v
                break
            except Exception:
                pass

_load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()

# Amazon Now Session & Store Configuration
AMAZON_COOKIE = os.getenv("AMAZON_COOKIE", "").strip()
AMAZON_BRAND_ID = os.getenv("AMAZON_BRAND_ID", "").strip()

# Deal Filters & Runtime Settings
MIN_DISCOUNT = int(os.getenv("MIN_DISCOUNT", "70"))

# Custom discount rules based on keyword in title or brand
CUSTOM_RULES = {
    "aashirvaad": 40,
    "tide": 40,
    "atta": 40,
    "ground coffee": 40,
    "cashew": 50,
    "almond": 50,
    "ariel": 50,
    "dal": 60,
    "chocolate": 70,
    "home decor": 70
}

MAX_WORKERS = int(os.getenv("MAX_WORKERS", "5"))
INTER_PAGE_DELAY = float(os.getenv("INTER_PAGE_DELAY", "0.8"))
CACHE_FILE = os.getenv("CACHE_FILE", os.path.join("data", "posted_deals.json"))
DRY_RUN = os.getenv("DRY_RUN", "false").lower() in ("true", "1", "yes")

# HTTP & API Headers
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

DEFAULT_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": USER_AGENT,
    "origin": "https://www.amazon.in",
    "referer": "https://www.amazon.in/tez/browse/home"
}

# Optional browse node for Skin Care (set via env var or replace here once discovered)
SKIN_CARE_NODE_ID = os.getenv("SKIN_CARE_NODE_ID", "").strip()

# Target High-Yield Categories on Amazon Now
CATEGORIES = [
    # Fresh Produce & Meat
    {"name": "Fresh Vegetables", "nodeId": "218833871031", "endpoint": "category"},
    {"name": "Fresh Fruits", "nodeId": "218833884031", "endpoint": "category"},
    {"name": "Meat & Seafood", "nodeId": "218876203031", "endpoint": "category"},

    # Grocery & Staples (Atta, Rice, Oil, Dal, Masala)
    {"name": "Atta & Flours", "nodeId": "204870009031", "endpoint": "category"},
    {"name": "Rice & Grains", "nodeId": "204870014031", "endpoint": "category"},
    {"name": "Dals & Pulses", "nodeId": "204870007031", "endpoint": "category"},
    {"name": "Cooking Oils & Ghee", "nodeId": "204870005031", "endpoint": "category"},
    {"name": "Spices & Masalas", "nodeId": "204870013031", "endpoint": "category"},

    # Dairy & Breakfast
    {"name": "Fresh Milk", "nodeId": "204870018031", "endpoint": "category"},
    {"name": "Bread & Bakery", "nodeId": "204870003031", "endpoint": "category"},
    
    # Snacks, Sweets & Beverages
    {"name": "Chips & Crisps", "nodeId": "204924530031", "endpoint": "category"},
    {"name": "Indian Namkeen", "nodeId": "215540425031", "endpoint": "category"},
    {"name": "Wafers & Biscuits", "nodeId": "204924537031", "endpoint": "category"},
    {"name": "Sweets & Mithai", "nodeId": "204924552031", "endpoint": "category"},
    {"name": "Dry Fruits & Nuts", "nodeId": "204924525031", "endpoint": "category"},
    {"name": "Cold Drinks & Sodas", "nodeId": "204924556031", "endpoint": "category"},
    {"name": "Tea (Leaf & Bags)", "nodeId": "204924559031", "endpoint": "category"},
    {"name": "Coffee (Instant & Filter)", "nodeId": "204924558031", "endpoint": "category"},

    # Ice Creams (Strictly requires 'merch' endpoint based on amazon-now-deals.js)
    {"name": "Ice Cream Store", "nodeId": "216450600031", "endpoint": "merch"},
    
    # Beauty, Personal Care & Cleaning
    {"name": "Face Creams & Moisturizers", "nodeId": "204992632031", "endpoint": "category"},
    {"name": "Makeup & Lipsticks", "nodeId": "204992616031", "endpoint": "category"},
    {"name": "Men Grooming & Shaving", "nodeId": "204992619031", "endpoint": "category"},
    {"name": "Floor Cleaners (Lizol)", "nodeId": "204952368031", "endpoint": "category"},
]

# Dynamically include Skin Care if node ID is configured
if SKIN_CARE_NODE_ID:
    CATEGORIES.insert(2, {"name": "Skin Care", "nodeId": SKIN_CARE_NODE_ID, "endpoint": "category"})
