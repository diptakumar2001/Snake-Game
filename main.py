from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from leaderboard import Leaderboard


WIDTH, HEIGHT = 600, 600
HALF_BOUND = 280
LEVEL_UP_EVERY = 5
MAX_LEVEL = 5

restart_flag = False

def on_restart():
    """Triggered when user presses 'r' key to restart."""
    global restart_flag
    restart_flag = True


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


name_from_ui = screen.textinput("Player Name", "Enter your name:")
player_name = (name_from_ui.strip() if name_from_ui else "Player")

# Print confirmation to console
print(f"Starting game for: {player_name}")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
leaderboard = Leaderboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(on_restart, "r")


def reset_for_new_round():
    """Reset snake, food, scoreboard, and level for a new round."""
    global restart_flag
    restart_flag = False
    for segment in snake.segments:
        segment.goto(1000, 1000)
    snake.segments.clear()
    snake.make_snake()
    food.new_food()
    scoreboard.reset()
    scoreboard.level = 1

def calc_speed(level, score):
    base = 0.15
    level_adj = (level - 1) * 0.015
    score_adj = score * 0.002
    return max(0.03, base - level_adj - score_adj)


while True:
    reset_for_new_round()
    game_running = True

    while game_running:
        screen.update()
        time.sleep(calc_speed(scoreboard.level, scoreboard.score))
        snake.move()
        head = snake.segments[0]

        # Detect collision with food
        if head.distance(food) < 15:
            food.new_food()
            snake.extend()
            scoreboard.increase_score()

            # Level up after every few points
            if scoreboard.score % LEVEL_UP_EVERY == 0 and scoreboard.level < MAX_LEVEL:
                scoreboard.level += 1
                scoreboard.announce_level_up()

        # Detect collision with border
        if abs(head.xcor()) > HALF_BOUND or abs(head.ycor()) > HALF_BOUND:
            scoreboard.game_over()
            game_running = False
            break

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if head.distance(segment) < 10:
                scoreboard.game_over()
                game_running = False
                break

    # Game Over: update leaderboard
    leaderboard.update(player_name, scoreboard.score)
    print("Game over. Press 'r' to restart.")

    # Wait for restart
    while True:
        screen.update()
        time.sleep(0.12)
        if restart_flag:
            break

# Keeps window open until closed manually
screen.exitonclick()
