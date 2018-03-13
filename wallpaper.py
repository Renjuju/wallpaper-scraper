import json
import urllib2
from appscript import app, mactypes
import os
import subprocess

cwd = os.getcwd()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)

url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

wallpaper_response = json.load(urllib2.urlopen(url))

res = wallpaper_response['images'][0]
image_url = 'https://bing.com' + res['url']

print str(image_url)
f = open( res['hsh'] + '.jpg', 'wb')
f.write(urllib2.urlopen(str(image_url)).read())

# app('Finder').desktop_picture.set(mactypes.File(cwd + '/' + res['hsh'] + '.jpg'))
#set_desktop_background(cwd + '/' + res['hsh'] + '.jpg')


