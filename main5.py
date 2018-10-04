from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Greetings!",
    "Hello",
])
while True:
    req = input('You : ')
    if req.strip()!= 'bye':
            reply = chatterbot.get_response(req)
            print('Bot :', reply)
