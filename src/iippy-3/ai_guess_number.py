# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
from Tkinter import *
import tkFileDialog
import ast

class Message:
    def __init__(self):
        self.msg_list = []

    def add_message(self, msg):
        self.msg_list.append(msg)

class QuizSetter:
    def __init__(self, min_value, max_value, name):
        self.min_value = min_value
        self.max_value = max_value
        self.name = name
        self.value = random.randrange(min_value, max_value)
        self.msg_list = []
        
    def quiz(self):
        
        self.msg_list.append(self.name + ": Guess the Nubmer [" + str(self.min_value) + "," + str(self.max_value) + ")")
        return [self.min_value, self.max_value];

    def judge(self, ai_guess, ai_name):
        self.msg_list.append(ai_name + ": Guess " + str(ai_guess))
        if (ai_guess == self.value):
            self.msg_list.append(ai_name + ": Perfect!")
            return True
        else:
            if (ai_guess >= self.min_value and ai_guess < self.value):
                self.min_value = ai_guess
            elif (ai_guess > self.value and ai_guess < self.max_value):
                self.max_value = ai_guess
            return False

class AIPlayer:
    def __init__(self, name):
        self.ai_guess = 0
        self.name = name;

    def guess(self, min_value, max_value):
        ai_guess = min_value + (max_value - min_value)/2
        if(ai_guess==self.guess):
            self.ai_guess = ai_guess + 1
        else:
            self.ai_guess = ai_guess
        return self.ai_guess

class GameHistory:
    def __init__(self, name):
        self.name = name
        self.quiz = []
        self.ai_guess = []
        self.msg_list = []

    def add_quiz(self, quiz):
        self.quiz.append(quiz)

    def add_guess(self, guess):
        self.ai_guess.append(guess)
   
    def __str__(self):
        return self.name + "\n" + str(self.quiz) + "\n" + str(self.ai_guess)

    def str_to_history(self, history_str):
        history = history_str.split('\n')
        if(len(history) != 3):
           return False
        # TODO ERROR handler
	try:
            self.name = history[0]
  	    self.quiz = ast.literal_eval(history[1])
            self.ai_guess = ast.literal_eval(history[2])
            return True
        except SyntaxError:
            return False

    # save self.name self.quiz self.ai_guess to file
    def save(self, save_file):
        save_file.write(str(self))

    # read self.quiz and self.qi_guess from file
    # play
    def play(self, open_file):
        end = False
        history_str = ""
        while not end:
            read_str = open_file.readline(1024)
            if not read_str:
                end = True
            else:
                history_str += read_str
        if not self.str_to_history(history_str):
            self.msg_list=[]
            self.msg_list.append("File Format Not Right!")
            return;
        i = 0
        self.msg_list=[]
        self.msg_list.append("History: ");
        while i < len(self.quiz):
            self.msg_list.append(self.name + ": Guess the Nubmer [" + str(self.quiz[i][0]) + "," + str(self.quiz[i][1]) + ")")
            self.msg_list.append(self.name + ": Guess " + str(self.ai_guess[i]))
            i += 1
        self.msg_list.append(self.name + ": Perfect!");
        

class GuessNumberGame:
    def __init__(self, name):
        self.quiz = QuizSetter(0, 100, name)
        self.ai = AIPlayer(name)
        self.history = GameHistory(name)
        self.play = False

    def start(self):
        quiz_range = self.quiz.quiz()
        self.history.add_quiz(quiz_range)
        ai_guess = self.ai.guess(quiz_range[0], quiz_range[1])
        self.history.add_guess(ai_guess)
        while not self.quiz.judge(ai_guess, self.ai.name):
            quiz_range = self.quiz.quiz()
            self.history.add_quiz(quiz_range)
            ai_guess = self.ai.guess(quiz_range[0], quiz_range[1])
            self.history.add_guess(ai_guess)
           
    def draw_text(self, canvas, pos, size, color):
	if self.play:
            index = 0
   	    for message in self.history.msg_list:
                canvas.draw_text(message, [pos[0], pos[1] + index * 30], size, color)
                index +=1
        else:
            index = 0
   	    for message in self.quiz.msg_list:
                canvas.draw_text(message, [pos[0], pos[1] + index * 30], size, color)
                index +=1

    def set_play(self, mode):
        self.play = mode

# init game
game = GuessNumberGame("GameOne")
# save game
def save_game():
    game.set_play(False)
    save_file = tkFileDialog.asksaveasfile(mode='w')
    game.history.save(save_file)
    save_file.flush()
    save_file.close()

def play_game():
    game.set_play(True)
    open_file = tkFileDialog.askopenfile(mode='r')
    game.history.play(open_file)
    open_file.close()
#    game.set_play(False)
    
    
# Handler to draw on canvas
def draw(canvas):
    game.draw_text(canvas, [50, 50], 24, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("AI Guess", 1000, 800)
frame.set_draw_handler(draw)

# frame add save and play
frame.add_button("Save", save_game)
frame.add_button("Play", play_game)
# Game Start
game.start()

root = Tk()
root.withdraw()

# Start the frame animation
frame.start()
