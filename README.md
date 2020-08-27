README.md

# Some cool stuff with selenium
Followed a tutorial on youtube, and made this. Not that great but it works nicely

I used osu.ppy.sh for the data

You need to download Chromedriver, I got one for Chrome version 81
If you don't want to use Chrome, you can get a driver for your favorite browser if avaliable and replace it in the script

You also need Selenium
``pip install Selenium`` should work
This script works for any website that has public data in it, you just need to know some basic HTML code.

# Pretty bad code ahead

When I did this, I was still learning python (still am), so the code might not be the most optimized, but I did try my best

# Selenium is retarded
After some time, I tried adding a "song lyric" thing to the script, it works fine normally, but not headless.
In fact, not even rank comparing works headless, so if you want to try those 2, change ``options.headless`` to ``False``

# Songs
I'm not sure why, but it doesn't works 100% of the time. Currently using Genius.com for the lyrics, to change it, you must change everything related to it, including the search bar, the first result and lyrics class
