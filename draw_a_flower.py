import turtle

def one_square(turt):
    for i in range(1,5):
        turt.forward(50)
        turt.right(90)

def draw_many_squares():
    donatello=turtle.Turtle()
    donatello.shape("turtle")
    donatello.color("gold","mediumaquamarine")
    donatello.speed(0)
    for i in range(1,51):
        donatello.right(7.5)
        one_square(donatello)
    donatello.ht()    
        
def rhombus(turt):
    for i in range(1,2):
        turt.forward(50)
        turt.right(40)
        turt.forward(145)
        turt.right(160)
        turt.forward(145)
        turt.right(40)
        turt.forward(50)

def smaller_rhombus(turt):
    turt.forward(71)
    turt.right(20)
    turt.forward(71)
    turt.right(160)
    turt.forward(71)
    turt.right(20)
    turt.forward(71)
    turt.right(160)
        
def testing():
    testo=turtle.Turtle()
    testo.shape("turtle")
    testo.speed(0)
    testo.color("violet")
    for i in range (1,25):
        rhombus(testo)
        testo.right(15)
    testo.ht()    
    

    
        
def draw_secondrhomb():
    leo=turtle.Turtle()
    leo.shape("square")
    leo.color("navy")
    leo.speed(0)
    leo.right(5)
    for i in range (1,49):
        
        smaller_rhombus(leo)
        leo.right(7.5)
    leo.ht()
        

def small_circles():
    mike=turtle.Turtle()
    mike.shape("turtle")
    mike.speed(0)
    mike.color("yellow")
    for i in range (1,37):
        mike.circle (25)
        mike.right (10)
    mike.ht()
    
    
   
def draw_right_triangles():
    raphael=turtle.Turtle()
    raphael.shape("turtle")
    raphael.color("magenta","limegreen")
    raphael.speed(6)
    n=20
    while n<100:
        raphael.forward(n)
        raphael.right(90)
        raphael.forward(n*(3**.5))
        raphael.right(150)
        raphael.forward(2*n)
        n=n*1.08
    raphael.forward(100)    
def stem():
    bobby=turtle.Turtle()
    bobby.color("green")
    bobby.speed(9)
    bobby.right(90)
    bobby.forward(180)
    bobby.pensize(6)
    bobby.forward(220)
    bobby.backward(50)
    bobby.pensize(1)
    bobby.right(270)
    n=10
    while n<=45:
        
        bobby.forward(.4*n)
        bobby.circle(n)
        bobby.left(2)
        n=n*1.15
        
    bobby.left(40)
    n=n-5
    while n>3:
        
        bobby.forward(.4*n)
        bobby.circle(n)
        bobby.left(2)
        n=.87* n
        bobby.ht()

def whats_in_a_name():
    danny=turtle.Turtle()
    danny.speed(0)
    danny.pu()
    danny.goto(-200,-200)
    danny.down()
    danny.color("white")
    danny.right(90)
    danny.pensize(16)
    danny.forward(80)
    danny.pensize(1)
    danny.forward(10)
    danny.left(90)
    
    for i in range (1,37):
        danny.circle(8)
        danny.forward(6)
        danny.left(6)
    danny.pu()
    danny.goto(-120,-280)
    danny.right(126)
    danny.down()
    danny.pensize(16)
    danny.forward(80)
    danny.backward(40)
    danny.right(90)
    danny.forward(40)
    danny.pu()
    danny.left(90)
    danny.forward(40)
    danny.right(180)
    danny.pensize(1)
    danny.down()
    for i in range (1,18):
        danny.circle(8)
        danny.forward(5)
    danny.ht()    
    
    
    
def lets_make_shapes():
    window = turtle.Screen()
    window.bgcolor("royalblue")
    testing()
    whats_in_a_name()
    draw_secondrhomb()
   
    draw_many_squares()
    
    small_circles()
    stem()
 #   draw_right_triangles()
    window.exitonclick()
    


    


lets_make_shapes()    
