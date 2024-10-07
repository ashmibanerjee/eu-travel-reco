from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium_stealth import stealth


def get_html_dumps(base_url: str, args=None):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")

    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, )

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.get(base_url)
    time.sleep(7)
    try:
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()
        time.sleep(5)
    except Exception as e:
        print(e)
    html_source = driver.page_source
    time.sleep(10)
    driver.quit()
    return html_source
