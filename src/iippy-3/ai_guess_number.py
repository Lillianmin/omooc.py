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

class GuessNumberGame:
    def __init__(self, name):
        self.quiz = QuizSetter(0, 100, name)
        self.ai = AIPlayer(name)

    def start(self):
        quiz_range = self.quiz.quiz()
        ai_guess = self.ai.guess(quiz_range[0], quiz_range[1])
        while not self.quiz.judge(ai_guess, self.ai.name):
            quiz_range = self.quiz.quiz()
            ai_guess = self.ai.guess(quiz_range[0], quiz_range[1])
           
    def draw_text(self, canvas, pos, size, color):
        index = 0
	for message in self.quiz.msg_list:
            canvas.draw_text(message, [pos[0], pos[1] + index * 30], size, color)
            index +=1


# init game
game = GuessNumberGame("GameOne")

# Handler to draw on canvas
def draw(canvas):
    global game
    game.draw_text(canvas, [50, 50], 24, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("AI Guess", 1000, 800)
frame.set_draw_handler(draw)

# Game Start
game.start()

# Start the frame animation
frame.start()

