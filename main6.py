from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from tkinter import *
from tkinter import ttk


bot = ChatBot('Narad ji')

bot.set_trainer(ListTrainer)
def calculate(*args):
    try:
        value =rep.get()
        ans.set(bot.get_response(rep.get()))
    except ValueError:
        pass
    
root = Tk()
root.title("chat bot")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

rep = StringVar()
ans = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=rep)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=ans).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="sendTo NaradJi", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="input").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text=" @@@@@ ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text=" !!!! ").grid(column=3, row=2, sticky=W)
for files in os.listdir ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
        data = open ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files, 'r').readlines()
        bot.train(data)
while True:
        if req.strip()!= 'bye':
            reply = bot.get_response(rep.get())
              
        if req.strip()== 'bye':
            print('Bot : bye')
            break
        elif req.strip()== 3:
            print('Bot : Enter something')
root.mainloop()



