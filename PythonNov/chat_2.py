import random

greetingIntent = ["hello","hi","hey","hi there","hello there"]

#Membership operator - in, not in
chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    #if msg == "hello" or msg == "hi" or msg == "hey":
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
