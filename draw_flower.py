import turtle

def draw_triangle(turtle_name):
	for i in range(1,4):
		turtle_name.forward(100)
		turtle_name.right(120)

def draw_diamond(turtle_name):
	for i in range(1,3):
		turtle_name.forward(100)
		turtle_name.right(145)
		turtle_name.forward(100)
		turtle_name.right(35)

window = turtle.Screen()
window.bgcolor("brown")

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("yellow")
steve.speed(50)

for i in range (1,28):
	draw_diamond(steve)
	steve.right(20)

steve.left(90)
steve.color("green")
steve.forward(300)

window.exitonclick()