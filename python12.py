import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
BASKET_WIDTH, BASKET_HEIGHT = 80, 80  
BASKET_Y = HEIGHT - 80  
BASKET_SPEED = 10

HEART_SIZE = 80  
WHITE, RED, PINK = (255, 255, 255), (255, 0, 0), (255, 182, 193)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catching Your LOVE")

# Load Images
basket_img = pygame.image.load("/Users/manasvisingh/Downloads/eba6e5f9efb51596566bd22083760ffc-removebg-preview.png")
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))

heart_img = pygame.image.load("/Users/manasvisingh/Downloads/_-removebg-preview.png")
heart_img = pygame.transform.scale(heart_img, (HEART_SIZE, HEART_SIZE))

# Basket Position
basket = pygame.Rect(WIDTH // 2 - BASKET_WIDTH // 2, BASKET_Y, BASKET_WIDTH, BASKET_HEIGHT)

# Track Hearts & Score
hearts = []
score = 0
font = pygame.font.Font(None, 36)

# Game Loop
running = True
clock = pygame.time.Clock()
message_displayed = False  # Track if the message has been shown

while running:
    screen.fill(PINK)  # Set Background Color
    
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move Basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.x > 0:
        basket.x -= BASKET_SPEED
    if keys[pygame.K_RIGHT] and basket.x < WIDTH - BASKET_WIDTH:
        basket.x += BASKET_SPEED
    
    # Spawn Hearts Randomly
    if random.randint(1, 30) == 1:
        hearts.append([random.randint(0, WIDTH - HEART_SIZE), 0])  # Add new heart at random x-position
    
    # Move Hearts and Check for Collision
    hearts_to_remove = []
    for heart in hearts:
        heart[1] += 5  # Move heart down

        # Collision Check: Heart inside Basket
        if heart[1] + HEART_SIZE > BASKET_Y and basket.x < heart[0] < basket.x + BASKET_WIDTH:
            score += 1  
            hearts_to_remove.append(heart)  
        
        # Remove hearts that fall off the screen
        elif heart[1] > HEIGHT:
            hearts_to_remove.append(heart)

    # Remove collected or missed hearts
    for heart in hearts_to_remove:
        hearts.remove(heart)

    # Draw Hearts First (Behind Basket)
    for heart in hearts:
        screen.blit(heart_img, (heart[0], heart[1]))  

    # Draw Basket on Top
    screen.blit(basket_img, (basket.x, basket.y))  

    # Display Score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Display Valentine Message at Score 10
    if score == 10 and not message_displayed:
        message_font = pygame.font.Font(None, 50)
        message_text = message_font.render("Will you be my Valentine? 💖", True, RED)
        
        # Center Message
        text_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(message_text, text_rect)
        
        pygame.display.flip()
        pygame.time.delay(3000)  # Pause Game for 3 Seconds
        message_displayed = True  

    pygame.display.flip()
    clock.tick(30)  # Set FPS to 30

pygame.quit()








