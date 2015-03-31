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

message = ""
min = 0
max = 100
value = 0


# Handler for mouse click
def start():
    global min, max
    min = 0
    max = 100
    prepare_start()

def hard_start():
    global min, max
    min = 0
    max = 10000
    prepare_start()
    
# get start ready
def prepare_start():
    global message, value
    message = "Guess the Nubmer [" + str(min) + "," + str(max) + ")"
    value = random.randrange(min, max)

    
# check input is number
def your_guess(your_value):
    global message
    try:
        your_value = int(your_value)
    except ValueError:
        message = "Please Input a Number!"
        return
    if (new_range(your_value) == True):
        message = "Perfect!"
#        if (timer.is_running()):
#            timer.stop()
    else:
        message = "Wrong! Try [" + str(min) + "," + str(max) + ")"

# cal the new ragne        
def new_range(your_value):
    global value,max,min
    if (your_value == value):
        return True
    else:
        if (your_value >= min and your_value < value):
            min = your_value
        elif (your_value > value and your_value < max):
            max = your_value
        return False
        
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 12, "Red")

    
# Timer Handler
def timer_handler():
    global message
    message = "Timeout!"
    if(timer.is_running()):
        timer.stop()

# Init game with [0,100) mode
start()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.add_button("[0, 100) Start", start, 200)
frame.add_button("[0 10000) Start", hard_start, 200);
frame.add_input("Your Guess", your_guess, 200)

# Start the frame animation
frame.start()

# TODO add timer .Start timer
timer = simplegui.create_timer(600000, timer_handler)
#timer.start()
