from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from langchain.chains import create_extraction_chain
from langchain.tools import tool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserTools:
    
    @tool("Scrape website content async")
    def scrape_and_summarize_website(url):
        """Useful to scrape and summerize website content"""
        try:
            # Set up Selenium
            chrome_options = Options()
            chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            # driver = webdriver.Chrome(options=chrome_options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            print(url)
            driver.get(url)

            # Wait for the page to load (you may need to adjust the wait time)
            driver.implicitly_wait(5)

            # Get the page source after it has loaded
            page_source = driver.page_source

            # Use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(page_source, 'html.parser')

            # Extract text content
            text_content = soup.get_text()

            # Format the text (remove leading/trailing spaces, break into lines, etc.)
            lines = (line.strip() for line in text_content.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
            formatted_content = '\n'.join(chunk for chunk in chunks if chunk)

            # Return only the first 5k characters
            return formatted_content[:5000]

        finally:
            # Close the Selenium WebDriver
            driver.quit()
