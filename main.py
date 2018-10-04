from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os


bot = ChatBot('Test')
#conv = open('hi.txt' , 'r').readline()
bot.set_trainer(ListTrainer)
for files in os.listdir('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbotcorpus\data\english/conversations.yml/'):
        data = open('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbotcorpus\data\english/conversations.yml/' + files, 'r').readlines()
        bot.train(data)
              

while True:
	request = input('You : ')
	if (request.script() != 'bye'):
                reply = bot.get_response(request)
                print('Bot :', reply)
        #if (request.script() == 'bye'):
               # print('Bot : bye')
               # break
                
