import random
from datetime import datetime as dt
import os, glob

greetingIntent = ["hello","hi","hey","hi there","hello there"]
dateIntent = ["date","tell me date","what's the date","today's date"]
timeIntent = ["time","tell me time","what's the time","current time"]
musicIntent = ["play song","start song","play music"]

#Membership operator - in, not in
chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    #if msg == "hello" or msg == "hi" or msg == "hey":
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :",date.strftime("%d %b,%Y,%A"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is :",time.strftime("%H:%M:%S,%p"))
    elif msg in musicIntent:
        os.chdir("Songs")
        songs = glob.glob('*.mp3')
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
