from turtle import *
from random import randrange
from freegames import square, vector

# Initialize the position of the food, snake, and the direction of movement.
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Function to change the direction of the snake based on keyboard input.
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Function to check if the head of the snake is inside the game boundaries.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Function to move the snake and update its position.
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake hits the boundaries or collides with itself.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Append the new head to the snake.
    snake.append(head)

    # Check if the snake eats the food.
    if head == food:
        print('Snake:', len(snake))
        # Generate new random position for the food.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # If the snake didn't eat the food, remove the tail.
        snake.pop(0)

    # Clear the screen and update the positions of snake and food.
    clear()

    # Draw the snake body.
    for body in snake:
        square(body.x, body.y, 9, 'black')

    # Draw the food.
    square(food.x, food.y, 9, 'green')

    # Update the display.
    update()

    # Set a timer to call the move function after a delay (100 milliseconds in this case).
    ontimer(move, 100)

# Set up the game window.
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Listen for keyboard input to change the snake's direction.
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Start the game by calling the move function.
move()

# Finish the game when the window is closed.
done()
