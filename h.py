import turtle

# Constants
FORWARD_DISTANCE = 20
TURN_ANGLE_INNER = 40
TURN_ANGLE_OUTER = 45
FULL_ROTATION = 30
SECOND_FORWARD_DISTANCE = 10
FINAL_TURN_ANGLE = 55
REPEAT_TIMES = 20

# Initialize the turtle
pat = turtle.Turtle()

# Main pattern drawing loop
for _ in range(REPEAT_TIMES):
    for _ in range(4):
        pat.forward(FORWARD_DISTANCE)
        pat.color('green')
        pat.right(TURN_ANGLE_INNER)
        
        pat.forward(FORWARD_DISTANCE)
        pat.color('orange')
        pat.right(TURN_ANGLE_OUTER)
    
    pat.right(FULL_ROTATION)
    pat.color('red')
    
    pat.forward(SECOND_FORWARD_DISTANCE)
    pat.right(FINAL_TURN_ANGLE)
    pat.forward(FORWARD_DISTANCE)

# Hide the turtle and finish
pat.hideturtle()
turtle.done()