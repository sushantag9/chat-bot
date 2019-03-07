from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from tkinter import *

bot = ChatBot('Narad ji')

bot.set_trainer(ListTrainer)
for files in os.listdir ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
        data = open ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files, 'r').readlines()
        bot.train(data)
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Narad ji : Dear Guest Thank You for reaching us. How can I help you")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
#repl = Entry(window,width=20)
 
txt.grid(column=1, row=0)
#repl.grid(column=2, row=0)
reply = bot.get_response(txt.get())



print('Narad ji : Dear Guest Thank You for reaching us. How can I help you')
while True:
        def clicked():
 
            lbl.configure(text= reply)
 
        btn = Button(window, text="Click Me", command=clicked)
 
        btn.grid(column=3, row=0)
 
        window.mainloop()
