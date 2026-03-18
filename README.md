# 🗺️ Google Maps B2B Lead Scraper

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automated-green.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow.svg)

An enterprise-grade, modular web scraper built with Python and Playwright. This tool automates the extraction of highly targeted B2B leads (Names, Ratings, and Links) from Google Maps and processes them into clean, ready-to-use CSV/Excel files.

## 🚀 Features

* **Anti-Bot Navigation:** Utilizes Playwright with custom user agents and locale settings to navigate Google Maps reliably.
* **Intelligent Infinite Scroll:** Custom algorithms to handle Google Maps' dynamic sidebar loading, ensuring maximum data extraction without timing out.
* **Modular Architecture:** Code logic is separated from configuration (`config.py`) and UI locators (`locators.py`), making the tool highly scalable and easy to maintain if UI changes occur.
* **Automated Data Cleaning:** Integrates `pandas` to automatically drop duplicate listings and format the output.
* **Robust Error Logging:** Professional, real-time logging via `utils.py` to track extraction progress and catch isolated element errors without crashing the main loop.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Automation Framework:** Playwright
* **Data Manipulation:** Pandas

## 📂 Project Structure

```text
google-maps-lead-scraper/
│
├── config.py           # Search queries, output settings, and browser parameters
├── locators.py         # Centralized CSS selectors for easy maintenance
├── utils.py            # Logging setup and Pandas data processing
├── scraper.py          # Core Object-Oriented scraping logic
├── main.py             # Entry point and loop executor
└── requirements.txt    # Python dependencies
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/google-maps-lead-scraper.git](https://github.com/yourusername/google-maps-lead-scraper.git)
   cd google-maps-lead-scraper
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## 💻 Usage

1. Open `config.py` and modify the `SEARCH_QUERIES` list with your target keywords (e.g., `["Software companies in London", "Plumbers in Texas"]`).
2. Run the scraper:
   ```bash
   python main.py
   ```
3. Retrieve your clean data from the generated `data_output.csv` file.

## ⚠️ Disclaimer
This tool is built for educational purposes and personal portfolio demonstration. Always ensure your web scraping activities comply with the target website's Terms of Service and local data privacy laws (like GDPR or CCPA). 

## 🤝 Hire Me
Looking for custom data extraction, B2B lead generation, or web automation? I build reliable, fast, and clean web scraping solutions. 

**[🔗 Check out my Fiverr Gig here!](Insert your Fiverr link here)**
