import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from bs4 import BeautifulSoup

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = get_driver()

def page_source(url):
    driver.get(url)
    return driver.page_source

def get_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True)]

urls = get_urls(page_source("http://example.com"))

for product_url in urls:
    st.markdown(f'<a href="{product_url}" download target="_blank">{product_url}</a>', unsafe_allow_html=True)
    
