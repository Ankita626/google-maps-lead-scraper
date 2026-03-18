import time
from playwright.sync_api import sync_playwright, Page, BrowserContext
from config import *
from locators import MapsLocators
from utils import setup_logger

logger = setup_logger()

class GoogleMapsScraper:
    def __init__(self):
        self.p = None
        self.browser = None
        self.page = None

    def start_browser(self):
        """Initializes Playwright with stealth settings."""
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=HEADLESS)
        context: BrowserContext = self.browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 720}
        )
        self.page = context.new_page()
        logger.info("Browser started.")

    def search(self, query):
        """Navigates to Maps and performs a search."""
        logger.info(f"Searching for: {query}")
        self.page.goto("https://www.google.com/maps", timeout=TIMEOUT)
        self.page.wait_for_selector(MapsLocators.SEARCH_BOX)
        
        self.page.fill(MapsLocators.SEARCH_BOX, query)
        self.page.click(MapsLocators.SEARCH_BUTTON)
        self.page.wait_for_timeout(3000) # Wait for initial load

    def scroll_results(self):
        """Scrolls the left panel to load more results."""
        logger.info("Scrolling results panel...")
        try:
            # Hover over the results panel to ensure focus
            self.page.hover(MapsLocators.RESULTS_PANEL)
            
            for _ in range(MAX_RESULTS // 5): # Rough calculation for scrolls
                self.page.mouse.wheel(0, 1000)
                self.page.wait_for_timeout(1000)
                
                # Check if 'You've reached the end' message appears (Optional logic)
                end_of_list = self.page.get_by_text("You've reached the end of the list").is_visible()
                if end_of_list:
                    logger.info("End of list reached.")
                    break
        except Exception as e:
            logger.warning(f"Scrolling issue: {e}")
    
    def extract_data(self):
        """Parses visible cards and extracts details."""
        results = []
        cards = self.page.locator(MapsLocators.RESULT_CARD)
        count = cards.count()
        logger.info(f"Found {count} cards. Extracting details...")

        for i in range(min(count, MAX_RESULTS)):
            card = cards.nth(i)

            data = {
                "Name": "N/A",
                "Rating": "N/A",
                "Address": "N/A",
                "Link": "N/A"
            }

            try:
                # Name
                text_content = card.inner_text().split('\n')
                if text_content:
                    data["Name"] = text_content[0]

                # Link
                link_locator = card.locator("a")
                if link_locator.count():
                    data["Link"] = link_locator.first.get_attribute("href")

                # Rating
                rating_loc = card.locator(MapsLocators.RATING)
                if rating_loc.count():
                    data["Rating"] = rating_loc.first.get_attribute("aria-label")

                results.append(data)

            except Exception as e:
                logger.error(f"Error parsing card: {e}")
                continue

        return results

    def close(self):
        if self.browser:
            self.browser.close()
        if self.p:
            self.p.stop()
        logger.info("Browser closed.")
