import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from geecracker import validate, panel_visible, GeeConfig
from PIL import Image
import requests
import time
import sys, os
import random   

class My_Chrome(uc.Chrome):
    def __del__(self):
        pass

def simulate_typing(string, element):
    for i in string:
        element.send_keys(i)
        randNum = random.uniform(0, 0.2)
        time.sleep(randNum)

def main(scholarEmail, scholarPassword):
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox --no-first-run --no-service-autorun --password-store=basic")
    driver = My_Chrome(options=options, version_main=96)
    driver.get("https://marketplace.axieinfinity.com/login/")
    time.sleep(3)

    try:
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/button[1]/span[1]/div[1]")))
        button.click()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    
    try:
        emailTextBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        simulate_typing(scholarEmail, emailTextBox)
        passwordTextBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]")))
        simulate_typing(scholarPassword, passwordTextBox)
        loginButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]/h6[1]")))
        loginButton.click()
        time.sleep(15)
        gee_config = GeeConfig()

        # Hard-coded ignoring error
        try:
            if panel_visible(driver):
                validate(driver, gee_config)
        except:
            print("Ingoring error for validating geetest")
            pass
        showQRButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[1]/button[1]")))
        showQRButton.click()
        time.sleep(2)
        driver.get_screenshot_as_file("screenshot.jpg")

        time.sleep(500)
        
    except Exception as e:
        driver.quit()
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        # Check failed attempt and retry

if __name__ == "__main__":
    main()
