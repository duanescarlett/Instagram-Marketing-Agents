from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from langchain.chains import create_extraction_chain

class BrowserTools:
    
    def scrape_and_summarize_website(self):
        data = ""

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)

            page = await browser.new_page()
            await page.goto(site)

            page_source = await page.content()
            soup = BeautifulSoup(page_source, "html.parser")

            for script in soup(["script", "style"]):
                scrikpt.extract()

            # get text
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
            # drop blank lines
            data = '\n'.join(chunk for chunk in chunks if chunk)

            await browser.close()
        
        return data

    @tool("Scrape website content")
    def scrape_website(website):
        """Useful to scrape a website content"""
        url = f"https://chrome.browserless.io/content?token={config('BROWSERLESS_API_KEY')}"
        payload = json.dumps({"url": website})
        headers = {
        'cache-control': 'no-cache',
        'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])

        # Return only the first 5k characters
        return content[:5000]