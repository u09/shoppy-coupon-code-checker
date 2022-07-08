from selenium import webdriver
from webdriver_auto_update import check_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os, logging, ctypes

logging.basicConfig(level=logging.CRITICAL, format="\x1b[35m[\x1b[0m%(asctime)s\x1b[35m] \x1b[0m| \x1b[35m%(message)s\x1b[0m", datefmt="%I:%M:%S")
logging.getLogger().setLevel(logging.CRITICAL)
os.system("mode 80, 40")
check_driver(".")

def title(text):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Shoppy Coupon Code Bruteforcer | {text}")

coptions=webdriver.ChromeOptions()
coptions.add_argument("--incognito")
coptions.add_argument("--start-maximized")
coptions.add_argument("--disable-logging")
coptions.add_argument("--log-level=3")
coptions.add_argument("--disable-crash-reporter")
coptions.add_argument("--disable-dev-shm-usage")
coptions.add_argument("--output=/dev/null")
coptions.add_argument("--disable-in-process-stack-traces")
coptions.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.3610")

if __name__=="__main__":
    title("Config")
    os.system("cls")
    logging.critical("Please enter product link: ")
    link_=input("")
    logging.critical("Product name (ex: Netflix, Minecraft, Youtube): ")
    product_name_=input("")
    os.system("cls")
    
    coupon_list=[]
    before_words=["START", "SALE", "GIFT", "LAUNCH", "HALLOWEEN", "WELCOME", "SAVE", "SUMMER", "SPRING", "FALL", "WINTER", "LUCK", "LUCKY", "BLACKFRIDAY", "CYBERMONDAY", "HOLIDAY", "TEST", "NEW", "FREE", "MILITARY", product_name_.capitalize()]
    after_words=["OFF", "BLACKFRIDAY", "CYBERMONDAY", "HOLIDAY", "SALE", "GIFT", product_name_.capitalize()]

    for before_word in before_words:
        s1=0

        coupon_list.append(before_word.lower())

        for x in range(20):
            s1=s1+5
            coupon_list.append(f"{before_word.lower()}{s1}")

    for after_word in after_words:
        s1=0

        coupon_list.append(after_word.lower())

        for x in range(20):
            s1=s1+5
            coupon_list.append(f"{s1}{after_word.lower()}")

    final_link_=""
    driver = webdriver.Chrome(options=coptions, service_log_path=None)
    wait=WebDriverWait(driver, 1000)

    if "https://" in link_:
        final_link_=link_
    else:
        final_link_=f"https://{link_}"
    
    driver.get(final_link_)
    title("Bruteforcing")
    for coupon_ in coupon_list:
        try:
            applyacoupon=wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[4]")))
            applyacoupon.click()

            couponcode=wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div/div/div[1]/input")))
            couponcode.click()

            couponcode.send_keys(coupon_)

            apply=driver.find_element(By.XPATH, value="/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div/div/div[2]/button")
            apply.click()
            logging.critical(f"Tested | {coupon_}")
        except:
            logging.critical("Valid code found")
            break
            


        



    
    