

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

#TODO map pos to shape, draw shape list
#init
click_pos_list=[]
drag_pos_list=[]
cur_shape="Circle"
cur_index=0
message=""
mouse_mode="click"
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
    if cur_index < len(click_pos_list):
	cur_index += 1
	if cur_index >= len(click_pos_list):
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
def get_square_points(pos, length):
    pos1=pos
    pos2=[pos[0], pos[1] + length]
    pos3=[pos[0] + length, pos[1] + length]
    pos4=[pos[0] + length, pos[1]]
    return [pos1, pos2, pos3, pos4, pos1]

#get triangle points list
def get_triangle_points(pos, length):
    pos1=pos
    pos2=[pos[0]-length/2, pos[1]-length*math.sqrt(3)/2]
    pos3=[pos[0]+length/2, pos2[1]]
    return [pos1, pos2, pos3, pos1]

#draw 
def draw(canvas):
    if(mouse_mode == "click"):
	if ((cur_index >= 0) and (cur_index < len(click_pos_list))):
	    cur_pos = click_pos_list[cur_index]
	    if cur_shape == "Circle":
	        canvas.draw_circle(cur_pos, 30, 2, "Red")
	    elif cur_shape == "Triangle":
	        canvas.draw_polyline(get_triangle_points(cur_pos,60), 2, "Green")
	    elif cur_shape == "Square":
	        canvas.draw_polyline(get_square_points(cur_pos,60), 2, "Blue")
	    else:
	        canvas.draw_point(cur_pos, "Black")
	else:
	    canvas.draw_text(message,[50,50],24,"Red")
    elif(mouse_mode == "drag"):
        for pos in drag_pos_list:
	    canvas.draw_point(pos,"Black")

#mouse click
def click(pos):
    click_pos_list.append(pos)
    global cur_index,message,mouse_mode
    cur_index=len(click_pos_list) - 1
    messaage=""
    mouse_mode="click"

def drag(pos):
    drag_pos_list.append(pos)
    global mouse_mode
    mouse_mode="drag"


#create frame
frame = simplegui.create_frame("Your Draw", 1200, 800)

#set background white
frame.set_canvas_background("White")

#add shape control buttons
frame.add_button("Circle", shape_circle)
frame.add_button("Triangle", shape_triangle)
frame.add_button("Square", shape_square)

#add undo/redo button
frame.add_button("Undo", undo)
frame.add_button("Redo", redo)

#add mouse click and draw
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)

#start
frame.start()

