

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import re

#init
color_list=["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow","YellowGreen"]
shape_list=[]
drag_pos_list=[]
cur_shape="Circle"
play_mode=False
cur_color="Red"
cur_index=0
play_index=0
message=""
mouse_mode="click"
interval=1000
#set shape circle
def shape_circle():
    global cur_shape
    cur_shape = "Circle"

#set shape triangle
def shape_triangle():
    global cur_shape
    cur_shape = "Triangle"

#set shape square
def shape_square():
    global cur_shape
    cur_shape = "Square"

#redo 
def redo():
    global cur_index, message
    if cur_index < len(shape_list):
	cur_index += 1
	if cur_index >= len(shape_list):
	    message="Nothing to Redo"
    else:
	message="Nothing to Redo"

#undo
def undo():
    global cur_index,message
    if cur_index >= 0:
	cur_index -= 1
	if cur_index < 0:
	    message="Nothing to Undo"
    else:
	message="Nothing to Undo"

#get square points list
def get_square_points(x, y, length):
    pos=[x,y]
    pos1=pos
    pos2=[pos[0], pos[1] + length]
    pos3=[pos[0] + length, pos[1] + length]
    pos4=[pos[0] + length, pos[1]]
    return [pos1, pos2, pos3, pos4, pos1]

#get triangle points list
def get_triangle_points(x, y, length):
    pos=[x,y]
    pos1=pos
    pos2=[pos[0]-length/2, pos[1]-length*math.sqrt(3)/2]
    pos3=[pos[0]+length/2, pos2[1]]
    return [pos1, pos2, pos3, pos1]

#color rgb reg
def color_rgb_reg(color):
    return re.match(r'#[0-9a-f]{6}', color, re.IGNORECASE)

#draw 
def draw(canvas):
    if( not play_mode):
        if(mouse_mode == "click"):
    	    if ((cur_index >= 0) and (cur_index < len(shape_list))):
	        cur_shape = shape_list[cur_index]
	        draw_shape(canvas, cur_shape)
            else:
	        canvas.draw_text(message,[50,50],24,cur_color)
        elif(mouse_mode == "drag"):
            for pos in drag_pos_list:
	        canvas.draw_point([pos[0], pos[1]], pos[2])
    else:
    	if ((play_index >= 0) and (play_index <= cur_index)):
            cur_shape = shape_list[play_index]
	    draw_shape(canvas, cur_shape)
        else:
            canvas.draw_text(message,[50,50],34,cur_color)

#draw shape
def draw_shape(canvas, shape):
    if shape["shape"] == "Circle":
	canvas.draw_circle([shape["x"], shape["y"]], 30, 2, shape["color"])
    elif shape["shape"] == "Triangle":
	canvas.draw_polyline(get_triangle_points(shape["x"], shape["y"], 60), 2, shape["color"])
    elif shape["shape"] == "Square":
	canvas.draw_polyline(get_square_points(shape["x"], shape["y"], 60), 2, shape["color"])
    else:
	canvas.draw_point([shape["x"], shape["y"]], shape["color"])

#set color
def set_color(color):
    global cur_color, message
    if (color in color_list) or color_rgb_reg(color):
        cur_color = color
    else:
        message = "Please Input Correct Color Name:" + str(color_list) + " or RGB like #ff0000/#FF0000"
        color_input.set_text("")


#mouse click
def mouse_click(pos):
    shape={"x":pos[0], "y":pos[1], "shape":cur_shape, "color":cur_color}
    shape_list.append(shape)
    global cur_index,message,mouse_mode
    cur_index=len(shape_list) - 1
    messaage=""
    mouse_mode="click"

def drag(pos):
    special_pos=[pos[0], pos[1], cur_color]
    drag_pos_list.append(special_pos)
    global mouse_mode
    mouse_mode="drag"

# set interval
def set_interval(input_interval):
    global interval,message
    try:
	interval = int(input_interval)
    except ValueError:
        message = "Please Input a Integer for Interval!"
        interval_input.set_text("")

# play the draw 
def play_stop():
    global message,play_mode
    if play_stop_btn.get_text() == "play":
        play_mode=True
        play_stop_btn.set_text("stop")
        timer.start()
    elif play_stop_btn.get_text() == "stop":
        message = "Play Stoped by User"
	play_end()

# play end
def play_end():
    global play_index, play_mode
    play_stop_btn.set_text("play")
    timer.stop()
    play_index=-1
    play_mode=False

# timer ticker
def timer_handler():
    global play_index,message
    if (play_index>=-1 and play_index < cur_index):
	play_index += 1
    else:
	message = "Play End"
        play_end()
    

#create frame
frame = simplegui.create_frame("Your Draw", 1200, 800)

#set background white
frame.set_canvas_background("White")

#add shape control buttons
frame.add_button("Circle", shape_circle)
frame.add_button("Triangle", shape_triangle)
frame.add_button("Square", shape_square)

#add color input
color_input = frame.add_input("Set Color", set_color, 200);

#add undo/redo button
frame.add_button("Undo", undo)
frame.add_button("Redo", redo)

# add timer interval input
interval_input = frame.add_input("Set Interval(ms)", set_interval, 200);

#add play btn
play_stop_btn = frame.add_button("play", play_stop)

#add mouse click and draw
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_click)
frame.set_mousedrag_handler(drag)

#create timer
timer = simplegui.create_timer(interval, timer_handler)

#start
frame.start()

