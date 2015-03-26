# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

min = 100
max = 10000
value = random.randInt(min+1, max-1)

message = "Guess the Nubmer between " + str(min) + str(max) + "\nPress Start Button to Start!"

# Handler for mouse click
def start():
    global your_input
    message = "Good job!"
    
# check input is number
def your_guess(your_value):
    if (new_range(your_value) == True)
        message = "Perfect, your are right"
        frame.set_draw_handler(draw)
        timer.stop()
    else
        message = "Sorry, your are wrong! Try number between " + str(min) + " and " + str(max)
        frame.set_draw_handler(draw)
        
# cal the new ragne        
def new_range(your_value):
    if (your_value == value)
        return True
    else 
        if (your_value >= min && your_value < value)
            max = your_value
        elif (your_value > value && your_value <= max)
            min = your_value
        return False
        
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

    
# Timer Handler
def tiemr_handler():
    message = "Timeout!"
    frame.set_draw_handler(draw)
    timer.stop()
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_input("Your Guess", your_guess, 100)

# Start the frame animation
frame.start()

# Start timer
timer = simplegui.create_timer(30000, timer_handler)
timer.start()
