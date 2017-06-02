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
import subprocess
from subprocess import call
from selenium.webdriver.common.action_chains import ActionChains
from subprocess import call

tempvol = 0
volume = 0

call(["amixer", "-D", "pulse", "sset", "Master", "10%+"])

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

def get_master_volume():
    proc = subprocess.Popen('/usr/bin/amixer sget Master', shell=True, stdout=subprocess.PIPE)
    amixer_stdout = proc.communicate()[0].split('\n')[4]
    proc.wait()

    find_start = amixer_stdout.find('[') + 1
    find_end = amixer_stdout.find('%]', find_start)

    return float(amixer_stdout[find_start:find_end])
print(get_master_volume())
def increasevolume(num):
    call(["amixer", "-D", "pulse", "sset", "Master", str(num)+"%"])
def decreasevoume(num):
    call(["amixer", "-D", "pulse", "sset", "Master", str(num)+"0%"])

while 1:
    info = db.child("youtube").get()
    url = info.val()['link']
    volinfo = db.child("volume").get()
    vol  = int(info.val()['vol'])

    if int(vol) > tempvol:
        if volume < 100:
            volume += vol
            increasevolume(volume)

    elif int(vol) < tempvol:
        if volume > 0 :
            volume -= vol
            decreasevoume(volume)

    tempvol = int(vol)

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


