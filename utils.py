import pandas as pd
import logging
from config import LOG_FILE, OUTPUT_FILE

def setup_logger():
    """Configures a professional logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def save_data(data_list):
    """Saves list of dictionaries to CSV/Excel."""
    if not data_list:
        print("No data to save.")
        return

    df = pd.DataFrame(data_list)
    
    # Clean up data (Remove duplicates)
    df.drop_duplicates(subset=['Name'], keep='first', inplace=True)
    
    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    print(f"✅ Data saved successfully to {OUTPUT_FILE} ({len(df)} records)")