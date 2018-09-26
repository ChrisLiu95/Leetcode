from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ListTrainer'
)

# # Train based on the english corpus
# chatbot.train("chatterbot.corpus.english")
chatbot.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to an input statement
print(chatbot.get_response("Your flight has been booked"))
