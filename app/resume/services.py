### DOCX TO RTF CONVERTERS
### pip install requests beautifulsoup4 readability-lxml
### import bleach

import bleach
import requests
from bs4 import BeautifulSoup
from readability import Document

# --- Scrape job description from URL ---
def scrape_job_description(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Use Readability to isolate main content
        doc = Document(response.text)
        html = doc.summary()
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(separator='\n')

        return bleach.clean(text.strip())
    except Exception as e:
        print("Error scraping URL:", e)
        return None



### pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_with_selenium(url):
    options = Options()
    options.add_argument('--headless')  # run in background
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Let JS load

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    return bleach.clean(soup.get_text(separator="\n").strip())


### pip install playwright
### playwright install
import asyncio
from playwright.async_api import async_playwright

async def scrape_with_playwright(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(5000)  # wait for JS to load

        content = await page.content()
        await browser.close()

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        return bleach.clean(soup.get_text(separator="\n").strip())

# To run:
# asyncio.run(scrape_with_playwright("https://example.com/job"))