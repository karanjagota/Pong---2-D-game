## code written by karan jagota

import simplegui 

width=500
height=250
ball_pos=[width/2,height/2]
radius=20
ball_vel=[2,2]
counter1=0
counter2=0
pad_width = 8
pad_height = 70
half_pad_width = pad_width / 2
half_pad_height = pad_height/ 2
pad_vel=0
pad1_pos=height/2
pad2_pos=height/2
pad2_vel=0

def new_game():
    global ball_pos,counter1,counter2
    ball_pos =[width/2,height/2]    
    counter1=0
    counter2=0
    pad1_pos=height/2
    pad2_pos=height/2

def draw(canvas):
    global ball_pos,counter1,counter2,pad1_pos,pad_vel,pad2_pos,pad2_vel
    
    pad1_pos+=pad_vel
    
    
    if pad1_pos<=25:
        pad1_pos=25
    elif pad1_pos>=height-25:
        pad1_pos=height-25
    
    pad2_pos+=pad2_vel
    
    if pad2_pos<=25:
        pad2_pos=25
    elif pad2_pos>=height-25:
        pad2_pos=height-25
            
        
        
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
  
    if ball_pos[0]<pad_width-radius: 
        ball_vel[0]= - ball_vel[0]
        ball_vel[1]=-ball_vel[1]
        
        
    if ball_pos[0] <= pad_width + radius and (ball_pos[1] < pad1_pos or ball_pos[1] > pad1_pos + pad_height):
         ball_pos[0] = width/2;ball_pos[1]=height/2
         counter2+=1 
    if ball_pos[0]>(width-1)-radius:
        ball_vel[0] = - ball_vel[0]
        
                
    if ball_pos[0] >= width - pad_width - radius and (ball_pos[1] < pad2_pos or ball_pos[1] > pad2_pos + pad_height):        
        ball_pos[0]=width/2;ball_pos[1]=height/2
        counter1+=1
        
    if ball_pos[1]<radius or ball_pos[1]>(height-1)-radius:
        ball_vel[1]= -ball_vel[1]
    
    
    canvas.draw_line([width/2,0],[width/2,height],2,"red")
    canvas.draw_line([half_pad_width, pad1_pos - half_pad_height],[half_pad_width, pad1_pos +half_pad_height],pad_width, 'red')
    canvas.draw_line([(width-1)-half_pad_width, pad1_pos - half_pad_height],[(width-1)-half_pad_width, pad1_pos +half_pad_height],pad_width, 'red')
    canvas.draw_text(str(counter1),[145,75],30,"red")
    canvas.draw_text(str(counter2),[365,75],30,"red")
    canvas.draw_circle([250,125],22,1,"red","black")
    canvas.draw_circle(ball_pos,radius,2,"blue","green")
    
def keydown(key):
    global pad_vel,pad2_vel
    if key ==simplegui.KEY_MAP["up"]:
        pad_vel-=1
    elif key==simplegui.KEY_MAP["down"]:
        pad_vel+=1
    elif key==simplegui.KEY_MAP["W"]:
        pad2_vel-=1
    elif key==simplegui.KEY_MAP["S"]:
        pad2_vel+=1
    
frame=simplegui.create_frame("pong",width,height)
frame.set_draw_handler(draw)
frame.add_button("Restart",new_game,100)
frame.set_keydown_handler(keydown)
frame.start()