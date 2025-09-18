import pygame
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BLACK = (0, 0, 0)
FPS = 60

PARTICLE_COUNT_PER_BLOOM = 150
MIN_LIFESPAN = 60
MAX_LIFESPAN = 120
MIN_SPEED = 1.5
MAX_SPEED = 4.5
MIN_SIZE = 2
MAX_SIZE = 5
FADE_OUT_EFFECT = True
COLOR_SHIFT_SPEED = 0
PARTICLE_HUE_RANGE = 90

class Particle:
    def __init__(self, x, y, base_hue):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        self.lifespan = random.randint(MIN_LIFESPAN, MAX_LIFESPAN)
        self.initial_lifespan = self.lifespan
        
        self.size = random.randint(MIN_SIZE, MAX_SIZE)
        self.initial_size = self.size

        self.hue = (base_hue + random.uniform(-PARTICLE_HUE_RANGE / 2, PARTICLE_HUE_RANGE / 2)) % 360
        self.saturation = random.randint(80, 100)
        self.lightness = random.randint(50, 70)
        
        self.hsla_alpha_percent = 100
        
        self.color = pygame.Color(0)
        self.color.hsla = (self.hue, self.saturation, self.lightness, int(self.hsla_alpha_percent))
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifespan -= 1

        if self.lifespan <= 0:
            self.hsla_alpha_percent = 0
        elif FADE_OUT_EFFECT:
            progress = 1.0 - max(0, self.lifespan / self.initial_lifespan)
            
            self.hsla_alpha_percent = max(0, (1.0 - progress**1.5) * 100.0)
            
            lifespan_ratio = max(0, self.lifespan / self.initial_lifespan)
            self.size = max(1, int(self.initial_size * lifespan_ratio))
        
        try:
            h = self.hue % 360
            s = max(0, min(100, self.saturation))
            l = max(0, min(100, self.lightness))
            a = max(0, min(100, int(self.hsla_alpha_percent)))

            self.color.hsla = (h, s, l, a)
        except ValueError as e:
            print(f"CRITICAL: ValueError in Particle.update() setting HSLA: H={h}, S={s}, L={l}, A={a}. Error: {e}")
            self.hsla_alpha_percent = 0
            self.color.hsla = (self.hue, self.saturation, self.lightness, 0)


    def draw(self, surface):
        if self.hsla_alpha_percent > 0 and self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

    def is_dead(self):
        return self.lifespan <= 0 or self.hsla_alpha_percent <= 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Generative Particle Bloom - Click Me!")
    clock = pygame.time.Clock()

    particles = []
    current_base_hue = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    for _ in range(PARTICLE_COUNT_PER_BLOOM):
                        particles.append(Particle(mouse_x, mouse_y, current_base_hue))
                    current_base_hue = (current_base_hue + COLOR_SHIFT_SPEED * 10) % 360

        for i in range(len(particles) - 1, -1, -1):
            particles[i].update()
            if particles[i].is_dead():
                particles.pop(i)
        
        screen.fill(BLACK)
        for particle in particles:
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()