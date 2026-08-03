import pygame
import sys
# Initialize Pygame
pygame.init()
# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game: Developed By Md. Jakirul Islam(1065)")
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7
# Ball settings
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
# Scores
score_left = 0
score_right = 0
SCORE_LIMIT = 20
# Fonts
font = pygame.font.SysFont(None, 50)
# Paddle positions
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 -
PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
# Ball position and speed
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
clock = pygame.time.Clock()
def draw():

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    # Draw scores
    left_score_text = font.render(str(score_left), True, WHITE)
    right_score_text = font.render(str(score_right), True, WHITE)
    screen.blit(left_score_text, (WIDTH // 4, 20))
    screen.blit(right_score_text, (WIDTH * 3 // 4, 20))
def handle_input():
    keys = pygame.key.get_pressed()
    # Left paddle controls: W and S
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    # Right paddle controls: Up and Down arrows
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED
def move_ball():
    global ball_speed_x, ball_speed_y, score_left, score_right
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    # Bounce off paddles
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x *= -1
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball_speed_x *= -1
    # Score points
    if ball.left <= 0:
        score_right += 1
        reset_ball()
    if ball.right >= WIDTH:
        score_left += 1
        reset_ball()

    if score_left >= SCORE_LIMIT:
        game_over("Left Player")

    if score_right >= SCORE_LIMIT:
        game_over("Right Player")
def reset_ball():

    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1
    ball_speed_y = BALL_SPEED_Y if ball_speed_y > 0 else -BALL_SPEED_Y

# Game Over function
def game_over(winner):
    screen.fill(BLACK)
    over_text = font.render(f"GAME OVER! {winner} Wins!", True, WHITE)
    screen.blit(over_text, (WIDTH//2 - 250, HEIGHT//2 - 25))

    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.quit()
    sys.exit()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        handle_input()
        move_ball()
        draw()
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()