import turtle

def draw_square(turtle_name):

	square_count=0
	while square_count < 4:
		turtle_name.forward(100)
		turtle_name.right(90)
		square_count += 1

def draw_triangle(turtle_name):
	triangle_count = 0
	while triangle_count < 3:
		turtle_name.left(120)
		turtle_name.forward(75)
		triangle_count += 1

window = turtle.Screen()
window.bgcolor("green")

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("red")
steve.speed(40)
for i in range(1,37):
	draw_square(steve)
	steve.right(5)

#debbie = turtle.Turtle()
#debbie.shape("arrow")
#debbie.color("blue")
#debbie.circle(100)

#frank = turtle.Turtle()
#frank.shape("circle")
#frank.color("yellow")
#draw_triangle(frank)

window.exitonclick()
