import sqlite3
import urllib2
import twitter
import time
#path to user's history database (Chrome)
while True:
    path = sqlite3.connect("/Users/ocsmith/Library/Application Support/Google/Chrome/Default/History")
    cursor = path.cursor()
    cursor.execute("SELECT urls.title FROM urls")
    rows = cursor.fetchall()
    recents = []
    for row in rows:
        recents.append(row)
    getLastEntry = str(recents[-1])
    lastTab = getLastEntry[3:-3]
    path.close()

    file = open("twitter.txt")
    keys = file.read().split('\n')
    api = twitter.Api(keys[0],keys[1],keys[2],keys[3])
    response = api.PostUpdate("I recently viewed: "+ lastTab)

    print("Status has been updated to: " + response.text)
    time.sleep(3600)
    #print("Status updated to: " + response.text)
