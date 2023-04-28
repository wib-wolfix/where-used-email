# Developer:
# Wolfix (https://github.com/wib-wolfix)

import os
import time
import string
import random
import requests

from pystyle import Write, Colors, Colorate

class WhereUsedEmail:

  green = "\x1b[38;2;0;255;0m"
  red = "\x1b[38;2;255;0;0m"
  end = "\x1b[0m"

  def __init__(self):
    self.main()

  def main(self):
    self.clear()

    Write.Print(f"------------------------\n" +
                f"-       Analiser       -\n" +
                f"------------------------", Colors.red_to_purple, interval=0.0025)
    print("\n")

    thetype = Write.Input("Select the method: \n"+
                    "\n"+
                    "[1] Email\n"+
                    "[2] Phone\n"+
                    "\nChoice: ", Colors.yellow_to_red, interval=0.0025)

    if thetype == "1":
      email = Write.Input("Enter the email: ", Colors.yellow_to_red, interval=0.0025)
      self.start(int(thetype), email)
    elif thetype == "2":
      phone = Write.Input("Enter the phone: ", Colors.yellow_to_red, interval=0.0025)
      self.start(int(thetype), phone)
    else:
      print(self.red+"Please enter a valid choice!"+self.end)
      time.sleep(3)
      self.main()

  def start(self, method, info):
    if method == 1:
      self.startEmail(info)
    elif method == 2:
      self.startPhone(info)

  def startEmail(self, email):
    if self.isEmail(email):
      self.print("\nStarting search for email: " + email)
      print("\n")

      print(self.spotify(email))
    else:
      print(self.red+"Please enter a valid email!"+self.end)
      time.sleep(3)
      self.main()

  def startPhone(self, phone):
    self.print("\nStarting search for phone: " + phone + "\n")

  def spotify(self, email):
    url = "https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email="
    result = requests.get(url + email).text
    if "email" in result:
      return "["+self.green+"+"+self.end+"] "+self.green+"Spotify"+self.end
    return "["+self.red+"-"+self.end+"] "+self.red+"Spotify"+self.end

  def isEmail(self, email):
    if len(email) > 6:
      if "@" in email:
        if "." in email:
          return True
    return False

  def genLowercase(self, num = 6):
    result = ""
    thisIsCool = string.ascii_lowercase
    for i in range(num):
        result += random.choice(thisIsCool)
    return result

  def print(self, content):
    print(Colorate.Horizontal(Colors.blue_to_green, content, 1))

  def clear(self):
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")

WhereUsedEmail()
