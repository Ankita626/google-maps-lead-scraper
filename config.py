 # config.py

# ==========================================
# SEARCH CONFIGURATION
# ==========================================

# Targeted search queries for Bangladesh Tourism
SEARCH_QUERIES = [
    "Hotels in Cox's Bazar",
    "Resorts in Sajek Valley",
    "Tourist spots in Sylhet",
    "Restaurants in Banani Dhaka",
    "Travel agencies in Chittagong"
]

# How many results to fetch per query (Google Maps usually loads 100-120 max per search)
MAX_RESULTS = 50 

# ==========================================
# BROWSER SETTINGS
# ==========================================

# Set to False to watch the browser work (Great for portfolio videos!)
HEADLESS = False 

# Time to wait for elements (in milliseconds)
TIMEOUT = 30000 

# Language settings ensure we get English results even if scraping from BD
LOCALE = "en-US"

# Output filenames
OUTPUT_FILE = "bd_tourism_data.csv"
LOG_FILE = "scraper.log"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
