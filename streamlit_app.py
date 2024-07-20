import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from bs4 import BeautifulSoup

@st.cache_resource
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = get_driver()

def page_source(url):
    driver.implicitly_wait(100)
    driver.get(url)
    
    return driver.page_source

def get_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True)]

with st.form("myform"):
    url = st.text_input("What url do you want to scrape?", "")
    submitted = st.form_submit_button("Submit")
    if submitted and url:
        urls = get_urls(page_source(url))
        for product_url in urls:
            st.markdown(f'<a href="{product_url}" download target="_blank">{product_url}</a>', unsafe_allow_html=True)

    
