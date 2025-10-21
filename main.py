from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from leaderboard import Leaderboard

# Game settings
SCREEN_SIZE = 600
WALL_LIMIT = 280
POINTS_FOR_LEVEL_UP = 5
MAX_LEVEL = 5

# Setup screen
screen = Screen()
screen.setup(SCREEN_SIZE, SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Get player name
player_name = screen.textinput("Player Name", "Enter your name:")
if not player_name:
    player_name = "Player"
else:
    player_name = player_name.strip()

print(f"Starting game for: {player_name}")

def calculate_speed(level, score):
    """Get game speed based on level and score"""
    base = 0.15
    level_boost = (level - 1) * 0.015
    score_boost = score * 0.002
    speed = base - level_boost - score_boost
    return max(0.03, speed)

def restart_game(snake, food, scoreboard):
    """Reset everything for a new game"""
    # Clear old snake segments
    for segment in snake.segments:
        segment.goto(1000, 1000)
    snake.segments.clear()
    
    # Make new snake
    snake.make_snake()
    food.new_food()
    scoreboard.reset()

def hit_wall(snake):
    """Check if snake crashed into wall"""
    head = snake.segments[0]
    return abs(head.xcor()) > WALL_LIMIT or abs(head.ycor()) > WALL_LIMIT

def hit_tail(snake):
    """Check if snake ran into itself"""
    head = snake.segments[0]
    for segment in snake.segments[1:]:
        if head.distance(segment) < 10:
            return True
    return False

# Main game loop
keep_playing = True

while keep_playing:
    # Create fresh game objects for each round
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    leaderboard = Leaderboard()
    
    # Setup controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    game_on = True
    
    while game_on:
        screen.update()
        time.sleep(calculate_speed(scoreboard.level, scoreboard.score))
        snake.move()
        
        # Check if snake ate food
        if snake.segments[0].distance(food) < 15:
            food.new_food()
            snake.extend()
            scoreboard.increase_score()
            
            # Level up check
            if scoreboard.score % POINTS_FOR_LEVEL_UP == 0 and scoreboard.level < MAX_LEVEL:
                scoreboard.level += 1
                scoreboard.show_level_up()
        
        # Check for collisions
        if hit_wall(snake) or hit_tail(snake):
            scoreboard.show_game_over()
            leaderboard.update(player_name, scoreboard.score)
            game_on = False
            time.sleep(1.5)
    
    # Ask if player wants another round
    response = screen.textinput("Game Over", "Play again? (yes/no)")
    if not response or response.lower() not in ["yes", "y"]:
        keep_playing = False
        print(f"Thanks for playing, {player_name}!")

screen.bye()