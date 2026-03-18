# locators.py

class MapsLocators:
    # The input box for searching
    SEARCH_BOX = 'input[role="combobox"]'
    SEARCH_BUTTON = 'button[class="mL3xi"]'
    
    # The scrollable panel containing the list of results
    RESULTS_PANEL = 'div[role="feed"]'
    
    # Each individual result card in the list
    RESULT_CARD = 'div[role="article"]'
    
    # Specific details within a card (Note: These are fragile and may need updates)
    # We will use Aria-labels and generic structure in the scraper logic for robustness,
    # but here are standard class-based fallbacks.
    TITLE = 'div.fontHeadlineSmall'
    RATING = 'span.fontBodyMedium > span[role="img"]'
    ADDRESS_BUTTON = 'button[data-item-id="address"]'
    WEBSITE_BUTTON = 'a[data-item-id="authority"]'
    PHONE_BUTTON = 'button[data-item-id^="phone"]'