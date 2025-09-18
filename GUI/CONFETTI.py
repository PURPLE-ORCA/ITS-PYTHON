import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (255, 192, 203) # Pink
]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Confetti Animation")
clock = pygame.time.Clock()

# Confetti class
class Confetti:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-100, 0)
        self.size = random.randint(5, 15)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(1, 5)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-3, 3)
        self.shape = random.choice(["rect", "circle", "triangle"])
        
    def update(self):
        # Move downward
        self.y += self.speed
        
        # Add some sideways movement to simulate air resistance
        self.x += random.uniform(-1, 1)
        
        # Rotate the confetti
        self.angle += self.rotation_speed
        
        # Reset if it goes off screen
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-100, 0)
            self.x = random.randint(0, SCREEN_WIDTH)
    
    def draw(self):
        if self.shape == "rect":
            # Create a surface for the rectangle
            confetti_surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            pygame.draw.rect(confetti_surface, self.color, (0, 0, self.size, self.size))
            
            # Rotate the surface
            rotated_surface = pygame.transform.rotate(confetti_surface, self.angle)
            
            # Get the new rect and position it
            rect = rotated_surface.get_rect(center=(self.x, self.y))
            
            # Draw the rotated surface
            screen.blit(rotated_surface, rect)
            
        elif self.shape == "circle":
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size // 2)
            
        else:  # triangle
            # Calculate triangle points
            radius = self.size // 2
            points = [
                (
                    self.x + radius * pygame.math.Vector2(1, 0).rotate(self.angle + angle).x,
                    self.y + radius * pygame.math.Vector2(1, 0).rotate(self.angle + angle).y
                )
                for angle in [0, 120, 240]
            ]
            pygame.draw.polygon(screen, self.color, points)

# Create confetti pieces
confetti_count = 100
confetti_pieces = [Confetti() for _ in range(confetti_count)]

# Button for creating more confetti
button_rect = pygame.Rect(SCREEN_WIDTH - 180, SCREEN_HEIGHT - 50, 160, 40)
button_color = (100, 100, 200)
button_hover_color = (120, 120, 220)
font = pygame.font.SysFont(None, 30)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Add more confetti when button is clicked
                confetti_pieces.extend([Confetti() for _ in range(50)])
    
    # Fill the screen
    screen.fill(BLACK)
    
    # Update and draw confetti
    for confetti in confetti_pieces:
        confetti.update()
        confetti.draw()
    
    # Draw the button
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
    else:
        pygame.draw.rect(screen, button_color, button_rect)
    
    # Button text
    text = font.render("Add Confetti", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    
    # Show current confetti count
    count_text = font.render(f"Confetti: {len(confetti_pieces)}", True, WHITE)
    screen.blit(count_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()