from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Narad ji', read_only = True)
#trainer = ListTrainer(bot)
#bot.set_trainer(ListTrainer)
#for files in os.listdir ('C:/Users/minato\Desktop\chat_bot\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
        #data = open ('C:/Users/minato\Desktop\chat_bot\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files, 'r').readlines()
       # trainer.train(data)

print('Narad ji : Dear Guest Thank You for reaching us @ PSIT.')
print('           How can Narad ji help you')
while True:
        req = input('You the Guest : ')
        #print(req)
        if req.strip()!= 'bye':
            reply = bot.get_response(req)
            print('Narad ji :', reply)
            
        elif req.strip()== 'bye':
           print('Bot : bye')
           break
        
            

