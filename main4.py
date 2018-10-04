from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot import comparisons
import os

bot = ChatBot('Narad ji' , logic_adapters=[
    {
        'import_path' : "chatterbot.logic.BestMatch",
        'statement_comparison_function' : 'chatterbot.comparisons.levenshtein_distance',
        'response_selection_method' : 'chatterbot.response_selection.get_first_response'
        
    },
    {
        'import_path' : "chatterbot.logic.TimeLogicAdapter"
    }
    #{
     #   'import_path' : "chatterbot.logic.LowConfidenceAdapter",
     #   'threshold' : 0.50,
     #   'default_response' : "i didn't get you"
   # }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)
bot.set_trainer(ListTrainer)
for files in os.listdir ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
        data = open ('C:/Users/minato\Desktop\chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files, 'r').readlines()
        bot.train(data)
print(" ")       
print("@@ type 'bye' without quotes(') in reply to exit @@")
print('Narad ji : Dear Guest Thank You for reaching us @ PSIT.')
print('           How can Narad ji help you')
while True:
        req = input('You the Guest : ')
        if req.strip()!= 'bye':
            reply = bot.get_response(req)
            print('Narad ji :', reply)
           # print(comparisons.JaccardSimilarity.compare(req,req,'hi there'))           
        elif req.strip()== 'bye':
           print('Bot : bye')
           break
        
            

