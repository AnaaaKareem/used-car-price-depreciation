# Import standard libraries for managing randomized delays, human-like behavior, and path management
import time
import random
import re
import os
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Define the base website domain and search filter URL for URL construction
BASE_URL = "https://www.autotrader.co.uk"
BASE_SEARCH_URL = "https://www.autotrader.co.uk/car-search?advertising-location=at_cars&channel=cars&fuel-type=Electric&homeDeliveryAdverts=include&make=&postcode=SW1A%201AA&sort=relevance&year-to=2026"

# Set the total target for car records to define the extraction limit
TARGET_CARS = 10000

# Define relative directory paths for raw and processed data ingestion to ensure scalability
PROCESSED_DATA_DIR = os.path.join('..', 'data', 'raw')

# Generate a unique timestamp for the raw output filename to prevent data overwriting
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
RAW_OUTPUT_PATH = os.path.join(PROCESSED_DATA_DIR, f'auto_trader_uk_scraped_cars_{TIMESTAMP}.csv')

def handle_cookie_consent(page):
    # Identify the cookie acceptance button using text matching to clear blocking overlays
    try:
        accept_button = page.locator('button:has-text("Accept All"), button:has-text("Accept all cookies")').first
        
        # Check if the accept button is visible within 5 seconds before attempting interaction
        if accept_button.is_visible(timeout=5000):
            # Click the cookie acceptance button to enable full page interaction
            accept_button.click()
            
            # Output confirmation of cookie acceptance to the console
            print("Accepted cookies.")
            
            # Introduce a randomized delay to mimic human response time
            time.sleep(random.uniform(1.0, 2.0))
    except Exception:
        # Output notice if no cookie banner is encountered to proceed with extraction
        print("No cookie banner found. Proceeding...")

def extract_listing_links(page, target_count):
    # Initialize a set for unique car links to prevent duplicate record extraction
    links = set()
    
    # Initialize the page number counter for search result pagination
    page_num = 1
    
    # Iterate through search pages until the target link count is reached
    while len(links) < target_count:
        # Construct the paginated search URL for the current result set
        paginated_url = f"{BASE_SEARCH_URL}&page={page_num}"
        
        # Output current page progress to track extraction status
        print(f"Loading search feed: Page {page_num}...")
        
        try:
            # Navigate to the paginated search URL with a 15-second timeout safeguard
            page.goto(paginated_url, timeout=15000)
        except PlaywrightTimeoutError:
            # Output timeout warning and stop pagination to avoid infinite loops
            print(f"Timeout on page {page_num}. Stopping pagination...")
            break
            
        # Handle cookie consent on the initial page load to ensure visibility of links
        if page_num == 1:
            handle_cookie_consent(page)
            
        # Introduce a randomized delay to mimic human browsing behavior and avoid bot detection
        time.sleep(random.uniform(1.5, 3.5))
        
        # Identify search listing title elements using the data-testid attribute
        elements = page.locator('a[data-testid="search-listing-title"]').all()
        
        # Check if listing elements were found on the page to verify search results
        if not elements:
            # Output end of results notice if no more car listings are available
            print(f"No more cars found. Reached end of search results.")
            break
            
        # Store the current link count for comparison to detect pagination caps
        initial_count = len(links)
        
        # Iterate through identified elements to extract individual href attributes
        for el in elements:
            # Extract the href attribute from the element to acquire the car URL
            href = el.get_attribute('href')
            if href:
                # Clean the URL by removing query parameters and adding the base domain
                clean_url = BASE_URL + href.split('?')[0]
                
                # Add the clean URL to the links set to ensure uniqueness
                links.add(clean_url)
                
        # Output current link extraction progress to the console
        print(f"Found {len(links)} unique car links...")
        
        # Check if the link count failed to increase to detect anti-scraping measures
        if len(links) == initial_count:
            # Output warning if AutoTrader appears to be capping results
            print("No new links found. AutoTrader may be capping results.")
            break
            
        # Increment the page number counter to progress to the next set of results
        page_num += 1
        
    # Return the truncated link list to match the specific target count
    return list(links)[:target_count]

def scrape_vehicle_data(page, url):
    # Navigate to the individual listing page to extract technical specifications
    try:
        page.goto(url)
        
        # Introduce a randomized delay to simulate human reading time
        time.sleep(random.uniform(1.5, 3.0))
        
        # Extract the header text from the page to identify the vehicle make and model
        h1_text = page.locator('h1').inner_text(timeout=5000)
        
        # Split the header text to isolate the manufacturer and model variant
        parts = h1_text.split(' ', 1)
        
        # Identify the car make and standardize to lowercase for training consistency
        make = parts[0].strip().lower()
        
        # Identify the car model or assign as unknown if parsing fails
        model = parts[1].strip().lower() if len(parts) > 1 else 'unknown'
        
        # Extract the price text from the page using the advert-price test ID
        price_text = page.locator('[data-testid="advert-price"]').inner_text()
        
        # Use regular expressions to convert price text into a clean float value
        price = float(re.sub(r'[^\d.]', '', price_text))
        
        # Extract the mileage text using specific xpath positioning for technical specs
        mileage_text = page.locator('xpath=//p[text()="Mileage"]/following-sibling::p').inner_text()
        
        # Use regular expressions to convert mileage text into a numerical float
        mileage = float(re.sub(r'[^\d.]', '', mileage_text))
        
        # Extract the registration text to determine the vehicle manufacturing year
        reg_text = page.locator('xpath=//p[text()="Registration"]/following-sibling::p').inner_text()
        
        # Use regular expressions to find the 4-digit registration year pattern
        year_match = re.search(r'\d{4}', reg_text)
        
        # Assign the matched year or default to 2020 if parsing is unsuccessful
        year = int(year_match.group(0)) if year_match else 2020
        
        # Extract the gearbox text to categorize the transmission type
        transmission_text = page.locator('xpath=//p[text()="Gearbox"]/following-sibling::p').inner_text()
        
        # Format the transmission text to lowercase for pipeline standardization
        transmission = transmission_text.strip().lower()
        
        # Output extraction summary for the current vehicle to verify success
        print(f"Scraped: {make.title()} {model.title()} - £{price}")
        
        # Return a dictionary of vehicle features for dataset integration
        return {
            'country': 'uk',
            'make': make,
            'model': model,
            'year': year,
            'mileage': mileage,
            'transmission': transmission,
            'fuelType': 'electric', 
            'mpg': 0.0,
            'engineSize': 0.0,
            'price': price
        }
    except Exception as e:
        # Output detailed error information for failed vehicle extractions
        print(f"Failed to scrape {url}: {str(e)}")
        return None

def run_scraper():
    # Initialize a list to store scraped car record dictionaries
    scraped_data = []

    # Initialize the playwright browser engine to start automation
    with sync_playwright() as p:
        # Launch a chromium browser instance in headless mode for performance
        browser = p.chromium.launch(headless=True) 
        
        # Create a new browser context with a custom user agent to bypass simple bot filters
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Open a new browser page for search navigation
        page = context.new_page()

        # Execute the link extraction process to acquire target vehicle URLs
        target_links = extract_listing_links(page, TARGET_CARS)

        # Iterate through acquired links to extract detailed car features
        for link in target_links:
            record = scrape_vehicle_data(page, link)
            if record:
                scraped_data.append(record)
        
        # Close the browser instance to free up system resources
        browser.close()

    # Execute dataset integration and file export
    if scraped_data:
        # Initialize a dataframe from the results list for manipulation
        df_new = pd.DataFrame(scraped_data)
        
        # Initialize the ordered_columns list to maintain feature placement consistency
        ordered_columns = ['country', 'make', 'model', 'year', 'age', 'mileage', 'transmission', 'fuelType', 'mpg', 'engineSize', 'price']
        
        # Reorder the dataframe columns to match the primary dataset schema
        df_new = df_new[ordered_columns]
        
        # Save the new raw records to a CSV file using the generated timestamp
        df_new.to_csv(RAW_OUTPUT_PATH, index=False)
        
        # Output save confirmation to the console
        print(f"New data saved to: {RAW_OUTPUT_PATH}")

if __name__ == "__main__":
    # Execute the scraper pipeline
    run_scraper()