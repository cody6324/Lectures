#We bascially went over turtles and the basics of really just how they work and etc..
#sadly not much to take notes over.
#Gave us hints about the quiz tomorrow, and also showed us that a default constructor is a constructor that doesnt
#have any parameters to send
#An example of a default constructor is
#t = Turtle()
#while an initializing constructor is
#t.forward(distance) because it takes a distance as a parameter
#t.pencolor(r, g, b)
#t.pencolor(string)
#It is called a method that is overloaded, because it is the same name but can be used in different ways
#and then we move to live coding
import turtle

def drawSquare(t, x, y, length):
    """Draws a square with the given turtle t, an upper-left cornet point 9x, y), and a side length s"""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)

def radialHexagons(t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)


def main():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    #drawSquare(alex, 50, -20, 250)     #Calls the function that draws a square
    radialHexagons(alex, 10, 150)
    #alex.forward(150)
    #alex.left(90)
    #alex.forward(75)
    #Either of the following will keep the canvas up
    turtle.done()
    #turtle.exitonclick()



if __name__ == "__main__":
    main()
