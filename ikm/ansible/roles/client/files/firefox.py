from selenium import webdriver
import logging

url = "https://www.ikm.internal/"

logging.basicConfig(
    filename="firefox.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
options.set_preference("network.dns.native_https_query", True)
service = webdriver.FirefoxService(executable_path="/snap/bin/geckodriver")

driver = None

try:
    driver = webdriver.Firefox(options=options, service=service)
    driver.get(url)
    logging.info(f"successfully accessed {url}")
except Exception as e:
    logging.error(f"failed to access {url}: {e}")
finally:
    if driver:
        driver.quit()
