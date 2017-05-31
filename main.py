import pyrebase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import org.openqa.selenium.Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium
from selenium.webdriver.common.action_chains import ActionChains




config = {
  "apiKey": "AIzaSyAujDNI5-U7PUG-jtB0jUZsklX2mXPkjSs",
  "authDomain": "pokeride-ff2ce.firebaseapp.com",
  "databaseURL": "https://pokeride-ff2ce.firebaseio.com/",
  "storageBucket": "pokeride-ff2ce.appspot.com",
  "serviceAccount": "/Users/chigoanyaso/PycharmProjects/afterawhile/yotubeSync/youtubeSync/pokeride-ff2ce-firebase-adminsdk-6kfba-28253c578d.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = {"link": "http://google.com"}

# db.child("youtube").set(data)

def update(link):
    data["link"] = link
    db.child("youtube").update(data)

update("http://youtube.com")
time.sleep(1)
info = db.child("youtube").get()
url = info.val()['link']
driver = webdriver.Chrome("/Users/chigoanyaso/PycharmProjects/afterawhile/yotubeSync/youtubeSync/chromedriver")
wait = WebDriverWait(driver, 15)
driver.get(url)
last_link = url

while 1:
    info = db.child("youtube").get()
    url = info.val()['link']

    if url != last_link:
        driver.get(url)
        try:
            enlarge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-fullscreen-button")))
            if enlarge:
                print("yes")
                enlarge.click()

            emailfield = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
            emailfield.send_keys("godwinanyaso@gmail.com")

            nextbutton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ZFr60d")))
            nextbutton.click()
        except:
            pass

        last_link = url


