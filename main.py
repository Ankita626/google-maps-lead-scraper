from scraper import GoogleMapsScraper
from config import SEARCH_QUERIES
from utils import save_data, setup_logger

logger = setup_logger()

def main():
    scraper = GoogleMapsScraper()
    all_leads = []
    
    try:
        scraper.start_browser()
        
        for query in SEARCH_QUERIES:
            scraper.search(query)
            scraper.scroll_results()
            leads = scraper.extract_data()
            all_leads.extend(leads)
            logger.info(f"Extracted {len(leads)} leads for '{query}'")
            
        save_data(all_leads)
        
    except Exception as e:
        logger.critical(f"Critical Failure: {e}")
    finally:
        scraper.close()

if __name__ == "__main__":
    main()