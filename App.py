import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
For some dumb reason, stuff works differently with and without GUI.
I made this to work with one, so I don't recommend turning it off.
If stuff works fine, ignore every warning or weird stuff you don't recognize.

Code still sucks"""

PATH = "C:/Program Files (x86)/chromedriver.exe" # I used Chrome, but if you have the driver for other browsers, specify the path here
						                         # Also works with Brave, just need to specify it's path

brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

options = webdriver.ChromeOptions()
#options.binary_location = brave_path # Uncomment to use Brave Browser
# option.add_argument("--incognito") # OPTIONAL
options.headless = False



def cls():
    os.system('cls' if os.name=='nt' else 'clear') # Just to make stuff uncluttered

def main():
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
    def lyrics(): # Search for song lyrics using Genius.com
        cls()

        inp = input("Name of the song to get lyrics: ")
        driver.get("https://genius.com") # Website used for song lyrics, if you change this, you must also change the "input","mini_card" and "lyrics" class to match with other websites's class
        src = driver.find_element_by_tag_name("input") # Genius's search bar class
        src.send_keys(inp) # Type the song into the search bar
        src.send_keys(Keys.ENTER) # Send "Enter" key
        time.sleep(10) # Sometimes it loads so slow, the program can't find the top result, giving an error. This little slow down is to make sure everything is loaded first
        driver.find_element_by_class_name("mini_card-info").click() # First result class on Genius.com
        try:
            lyric = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "lyrics")) # Same thing like "mini_card" here, just more easier to do, could've done both but am lazy
                )
            print("[!]------------------Lyrics below------------------[!]","\n",lyric.text) # Some random text might be printed before the actual lyrics, just a headsup
        except Exception as e:
            print(e)
            driver.quit()
        finally:
            driver.quit()
            time.sleep(2)
            main()
    def scors(): # Gets a user profile from osu!
        cls()
        usr = str(input("Please input a valid osu! username: "))
        driver.get("https://osu.ppy.sh/users/" + usr)
        print(driver.title, '\n')

        try:
            ranks = driver.find_elements_by_class_name("value-display__value") # Osu changed shit with the web so I had to find a new way to display ranks
            print("Global Rank: ", '\n', ranks[0].text) #Global ranks
            print('_____________', '\n')
            print("Local Rank: ", '\n', ranks[1].text) #Local ranks
            print('_____________', '\n')

            h = 2
            while h < 5:
                print(ranks[h].text) # This is for the extra stuff I am too lazy to write it
                print('_____________', '\n')
                h += 1


            stats = driver.find_elements_by_class_name("profile-header") #Entire osu! stats
            for i in stats:
                i = 0
                while i < 7: # Total of 7 stats on the website
                    tons_of_shit = driver.find_elements_by_tag_name("dl")[i].text # on the website, the stats are saved in a "dl" tag, it makes
                    print(tons_of_shit)                                           # things so much easier, we can just look for entries with it
                    print('_____________', '\n')
                    i += 1
            else:
                pass

            print("Song Ranks Machine Broke, idk how 2 fix, am dum","\n","_________","\n")
            """
            # idk what they've done, or I'm just stupid, but I can no longer get the ranks on profiles (S,A,SS,Silver SS)
            k = 0
            scores_ranks = driver.find_elements_by_class_name("profile-rank-count")

            while k < 5:
                if k == 0:
                    print('-------------------------------------------------------------', '\n')
                    print("Silver SS amount: ", scores_ranks[k].text)
                elif k == 1:
                    print("Gold SS amount: ", scores_ranks[k].text)
                elif k == 2:
                    print("Silver S amount: ", scores_ranks[k].text)
                elif k == 3:
                    print("Gold S amount:", scores_ranks[k].text)
                elif k == 4:
                    print("A scores amount: ", scores_ranks[k].text, '\n')
                    print('-------------------------------------------------------------', '\n')
                k += 1
            """
            friends = driver.find_elements_by_class_name("profile-detail-bar__column.profile-detail-bar__column--left") # Amount of followers
            print('Followers' + '\n' + friends[0].text)
            print('_____________', '\n')
            level = driver.find_elements_by_class_name("profile-detail-bar__entry.profile-detail-bar__entry--level") # Current level
            print('Level' + '\n' + level[0].text)
            print('_____________', '\n')


        except Exception as e:
            print(e)
            driver.quit()
        finally:
            driver.quit()
            time.sleep(2)
            main()
    def compare(): # Compare 2 users ranks
        cls()
        try:
            import re

            usr1 = input("First username for comparison: ")
            usr2 = input("Second username for comparison: ")
            driver.get("https://osu.ppy.sh/users/" + usr1)
            driver.implicitly_wait(5)
            first_rank = driver.find_elements_by_class_name("profile-detail__bottom-right-item")[0].text # Global ranks

            driver.get("https://osu.ppy.sh/users/" + usr2)
            driver.implicitly_wait(5)
            second_rank = driver.find_elements_by_class_name("profile-detail__bottom-right-item")[0].text # Global ranks

            time.sleep(3)
            convert = int(re.sub("\D","",first_rank)) # Convert every number we find to int   
            convert_sec = int(re.sub("\D","",second_rank)) # same here

            print(convert)
            print(convert_sec)

            # stupid code to make math
            if convert_sec > convert:
                res = eval('convert_sec -  convert') 
                print(usr1, " is ahead by: ", res, " ranks!")
            else:
                res = eval('convert - convert_sec')
                print(usr2, " is ahead by: ", res, " ranks!")
        except Exception as e:
            print(e)
            driver.quit()
        finally:
            driver.quit()
            time.sleep(2)
            main()


    # Main menu, thought it would be nice to do this
    time.sleep(5)
    cls()
    print("\n[!]-------------Cool osu! thingy-----------[!]\n[1] Show Scores\n[2] Compare Ranks\n[3] Song Lyrics (Genius.com)\n[0] Exit\n[!]-------------Cool osu! thingy-----------[!]")
    try:
        c = int(input(">"))
        if c == 1:
            scors()
            c = 0 
        elif c == 2:
            compare()
            c = 0
        elif c == 3:
            lyrics()
            c = 0
        elif c == 0:
            cls()
            driver.quit()
            print("Cya next time")
        else:
            print("Error, try again")
            main()
    except ValueError:
        print("Your choice must be an integer")
        main()

    

    
    


if __name__ == "__main__":
    cls()
    main()

# Again, I'm still learning python, so if you wanna contribute I would greatly appreciate it