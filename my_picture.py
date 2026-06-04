import simple_graphics as sg

def draw_house(x, y, color):
    """
    Draws a parameterized house with a base, roof, and door using public sg commands.
    """
    # 1. House Base
    sg.set_outline_color("black")
    sg.set_fill_color(color)
    sg.fill_rectangle(x, y, 160, 80)
    
    # 2. House Roof
    sg.set_fill_color("brown")
    # fill_triangle takes x1, y1, x2, y2, x3, y3
    sg.fill_triangle(x - 20, y, x + 80, y - 60, x + 180, y)
    
    # 3. House Door
    sg.set_fill_color("brown")
    sg.fill_rectangle(x + 60, y + 20, 40, 60)

def draw_bird(x, y, color):
    """
    Draws a simple V-shaped bird flying in the sky using public sg commands.
    """
    sg.set_outline_color(color)
    # The original was one connected line; here we use two separate lines for the V-shape
    sg.draw_line(x - 15, y - 8, x, y)
    sg.draw_line(x, y, x + 15, y - 8)
    
#cloud
def draw_cloud(x, y):
    sg.set_outline_color("white")
    sg.set_fill_color("white")
    sg.fill_rectangle(x-60, y-20, 120, 40)
    sg.fill_rectangle(x-40, y-40, 80, 80)
    sg.fill_arc(x-80,y-20,40,40,270,-180)
    sg.fill_arc(x-60,y-40,40,40,180,-90)
    sg.fill_arc(x-60,y,40,40,180,270)
    sg.fill_circle(x,y,55)
    sg.fill_arc(x+40,y-20,40,40,270,180)
    sg.fill_arc(x+20,y-40,40,40,90,-90)
    sg.fill_arc(x+20,y,40,40,0,-90)

def draw_flower(x,y):
    sg.set_outline_color("#77FF57")
    sg.set_fill_color("#77FF57")
    sg.fill_rectangle(x-1,y,2,20)
    sg.set_outline_color("white")
    sg.set_fill_color("white")
    sg.fill_circle(x+5,y+5,5)
    sg.fill_circle(x+5,y-5,5)
    sg.fill_circle(x-5,y+5,5)
    sg.fill_circle(x-5,y-5,5)
    sg.set_outline_color("yellow")
    sg.set_fill_color("yellow")
    sg.fill_circle(x,y,5)
    
#Person
def draw_blocky_person(x, y, height, color):
    """
    Draws a simple blocky 2D person.
    x, y: The top-left corner of where the person should start.
    height: The total height of the person.
    color: The main color of the person's clothes/body.
    """
    # Scale everything cleanly based on the total height
    unit = height / 10  # Break the height into 10 block units
    
    head_size = unit * 2
    body_w = unit * 3
    body_h = unit * 4
    limb_w = unit * 0.8
    limb_h = unit * 4
    
    # 1. Draw the Head
    sg.set_fill_color("#ffcc99") # Skin tone block
    sg.set_outline_color("black")
    sg.set_line_thickness(2)
    sg.fill_rectangle(x + unit, y, head_size, head_size)
    
    # 2. Draw the Body (Torso)
    sg.set_fill_color(color)
    sg.fill_rectangle(x + unit * 0.5, y + head_size, body_w, body_h)
    
    # 3. Draw the Legs
    # Left Leg
    sg.fill_rectangle(x + unit * 0.7, y + head_size + body_h, limb_w, limb_h)
    # Right Leg
    sg.fill_rectangle(x + unit * 2.5, y + head_size + body_h, limb_w, limb_h)
    
    # 4. Draw the Arms
    # Left Arm
    sg.fill_rectangle(x - unit * 0.5, y + head_size, limb_w, body_h)
    # Right Arm
    sg.fill_rectangle(x + unit * 3.7, y + head_size, limb_w, body_h)
 
#Dog
def draw_blocky_dog(x, y, height, color):
    """
    Draws a simple blocky 2D dog looking to the right.
    x, y: The top-left corner of where the dog should start (the head/ears area).
    height: The total height of the dog from paws to the top of its head.
    color: The main color of the dog's fur.
    """
    # Scale everything based on the total height (10 block units)
    unit = height / 10
    
    # Dimensions
    head_w = unit * 3
    head_h = unit * 2
    snout_w = unit * 1.5
    snout_h = unit * 1
    ear_w = unit * 1
    ear_h = unit * 1.5
    body_w = unit * 5
    body_h = unit * 3.5
    leg_w = unit * 1
    leg_h = unit * 4.5
    tail_w = unit * 1.5
    tail_h = unit * 0.8
    
    # 1. Setup global outlines and line thickness
    sg.set_outline_color("black")
    sg.set_line_thickness(2)
    
    # 2. Draw Ears (attached to back of the head)
    sg.set_fill_color("black") # contrasting color for ears
    sg.fill_rectangle(x, y + unit * 0.5, ear_w, ear_h)
    
    # 3. Draw Head
    sg.set_fill_color(color)
    sg.fill_rectangle(x + unit * 0.5, y + unit, head_w, head_h)
    
    # 4. Draw Snout/Muzzle (extends to the right)
    sg.fill_rectangle(x + unit * 0.5 + head_w, y + unit + (head_h - snout_h), snout_w, snout_h)
    
    # 5. Draw Eye & Nose
    sg.set_fill_color("white")
    sg.fill_rectangle(x + unit * 2.2, y + unit * 1.3, unit * 0.5, unit * 0.5) # Eye
    sg.set_fill_color("black")
    sg.fill_rectangle(x + unit * 2.4, y + unit * 1.5, unit * 0.3, unit * 0.3) # Pupil
    sg.fill_rectangle(x + unit * 0.5 + head_w + snout_w - (unit * 0.5), y + unit + (head_h - snout_h), unit * 0.5, unit * 0.4) # Nose
    
    # 6. Draw Body (behind and below the head)
    sg.set_fill_color(color)
    sg.fill_rectangle(x + unit * 0.5, y + unit + head_h, body_w, body_h)
    
    # 7. Draw Legs
    # Back Leg (Left side)
    sg.fill_rectangle(x + unit * 1, y + unit + head_h + body_h, leg_w, leg_h)
    # Front Leg (Right side)
    sg.fill_rectangle(x + unit * 4, y + unit + head_h + body_h, leg_w, leg_h)
    
    # 8. Draw Tail (on the left side of the body)
    sg.fill_rectangle(x - tail_w + unit * 0.5, y + unit + head_h + unit * 0.5, tail_w, tail_h) 

def draw_picture(width, height):
    """Draws a static picture."""

    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    #Ground
    sg.set_outline_color("green")
    sg.set_fill_color ("green")
    sg.fill_rectangle(0, 280,600, 400)
    sg.set_fill_color("cyan")
    sg.fill_rectangle(0, 0, 600, 280)
    
    #Lake
    sg.set_fill_color("blue")
    sg.set_outline_color("blue")
    sg.fill_rectangle(450, 280,100, 25)
    sg.fill_rectangle(425, 300,100, 25)
    sg.fill_rectangle(400, 320,100, 25)
    sg.fill_rectangle(375, 340,100, 25)
    sg.fill_rectangle(350, 360,100, 25)
    sg.fill_rectangle(325, 380,100, 25)
    
    #clouds
    draw_cloud(120,70)
    draw_cloud(320,65)
    
    #House (Base)
    sg.set_outline_color("black")
    sg.set_fill_color ("pink")
    sg.fill_rectangle(240, 200,160, 80)
    
    #House (Roof)
    sg.set_outline_color("black")
    sg.set_fill_color("brown")
    sg.fill_triangle (220,200,320,140,420,200)
    sg.set_outline_color("brown")
    
    #House (Door)
    sg.set_fill_color("brown")
    sg.fill_rectangle(300, 220, 40, 60)
    
    #Tree
    sg.set_fill_color ("brown")
    sg.fill_rectangle(75, 180, 25, 100)
    sg.set_fill_color ("green")
    sg.set_outline_color("green")
    sg.fill_rectangle (38, 100, 100, 100)
    
    #Sun
    sg.set_fill_color ("yellow")
    sg.fill_circle(600, 0, 100)
    
    #Person
    draw_blocky_person (560, 230, 50, "blue")
    draw_blocky_person (200, 230, 50, "red")
    
    #House
    draw_house(240, 200, "pink")
    
    #Dog
    draw_blocky_dog(150, 250, 30, "grey")
    draw_blocky_dog(380, 250, 30, "white")

    #Flower
    draw_flower(200,340)
    draw_flower(50,300)
    draw_flower(120,320)
    draw_flower(60,360)
    draw_flower(300,350)

    #Bird
    draw_bird(220, 80, "white")
if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
