import simple_graphics as sg

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

    #Flower
    draw_flower(200,340)
    draw_flower(50,300)
    draw_flower(120,320)
    draw_flower(60,360)
    draw_flower(300,350)

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
