from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter
from tkinter import *
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys

def process(my_bot, chat_window, message_window, top):
    q = Entry.get(message_window)
    if q == '' or q.isspace():
        print(type(q))
        return
    
    if q == 'bye' or q == 'Bye':
        top.destroy()
        return

    display = Text.get(chat_window, '1.0', END)
    Text.delete(chat_window, '1.0', END)
    display = display + 'You: '+q+'\nRed_Bot: '+str(my_bot.get_response(q))
    Text.insert(chat_window, END, display)
    Text.see(chat_window, END)
    Entry.delete(message_window, 0, END)
    
def init_chatbot():
    my_bot = ChatBot(name='red_bot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
    
    small_talk = ['hi there!', 'hi!', 'how do you do?', 'how are you?', 'i\'m cool', 'fine, you?', 'always cool', 'i\'m ok', 'glad to hear that', 'what is your name', 'red_bot']
    math_talk1 = ['pythagoras theoram', 'a^2 + b^2 = c^2']
    
    list_trainer = ListTrainer(my_bot)
    for item in (small_talk, math_talk1):
        list_trainer.train(item)
        
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.english')
    
    return my_bot

def run_gui(my_bot):
    top = Tk()

    top.title('ChatBot')
    top.geometry('400x500')
    top.resizable(width=False, height=False)

    chat_window = Text(top, bd=1, bg='black', width='50', height='8', font=('Arial', 18), foreground='#00ffff')

    chat_window.place(x=6,y=6, height=385, width=370)

    message_window = Entry(top, bd=0, bg="black", font=("Arial", 18), foreground="#00ffff")
    message_window.place(x=6, y=400, height=88, width=260)

    scrollbar = Scrollbar(top, command=chat_window.yview, cursor="star")
    scrollbar.place(x=375,y=5, height=385)

    send = Button(top, text="Send", command=lambda: process(my_bot, chat_window, message_window, top), width=12, height=5, bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
    send.place(x=275, y=400, height=88)

    top.mainloop()
    
if __name__ == '__main__':
    sys.setrecursionlimit(10**6) 
    my_bot = init_chatbot()
    run_gui(my_bot)