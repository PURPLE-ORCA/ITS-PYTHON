import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
FPS = 60

NUM_HEARTS = 7
BASE_SCALE = 15
SCALE_VARIATION = 1.5
MAX_POINTS = 150
LINE_THICKNESS = 3
ANIMATION_SPEED = 1
HUE_CYCLE_SPEED = 1
INITIAL_DELAY_FACTOR = 5

def heart_parametric(t, scale):
    x = scale * 16 * (math.sin(t) ** 3)
    y = -scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
    return x, y

def get_heart_points(scale, num_points, center_x, center_y):
    points = []
    for i in range(num_points + 1):
        t = (i / num_points) * 2 * math.pi
        x, y = heart_parametric(t, scale)
        points.append((center_x + x, center_y + y))
    return points

def get_rainbow_color(hue_offset, segment_idx, total_segments):
    hue = (hue_offset + (segment_idx / total_segments) * 360 * 2) % 360
    color = pygame.Color(0)
    color.hsla = (hue, 100, 60, 100)
    return color

class AnimatedHeart:
    def __init__(self, center_x, center_y, base_scale, delay_idx):
        self.center_x = center_x
        self.center_y = center_y
        self.scale = base_scale * (1 + random.uniform(-SCALE_VARIATION/base_scale/2, SCALE_VARIATION/base_scale/2))
        self.points = get_heart_points(self.scale, MAX_POINTS, self.center_x, self.center_y)
        self.current_point_idx = 0
        self.max_points_to_draw = len(self.points)
        self.hue_offset = random.randint(0, 360)
        self.drawing_started = False
        self.start_delay = delay_idx * INITIAL_DELAY_FACTOR

    def update(self, frame_count):
        if not self.drawing_started:
            if frame_count >= self.start_delay:
                self.drawing_started = True
            else:
                return False

        if self.current_point_idx < self.max_points_to_draw -1:
            self.current_point_idx = min(self.current_point_idx + ANIMATION_SPEED, self.max_points_to_draw -1)
            return True
        return False

    def draw(self, surface):
        if not self.drawing_started or self.current_point_idx < 1:
            return

        current_hue_offset = (self.hue_offset + pygame.time.get_ticks() * HUE_CYCLE_SPEED / 50) % 360

        for i in range(min(self.current_point_idx, len(self.points) - 1)):
            start_pos = self.points[i]
            end_pos = self.points[i+1]
            color = get_rainbow_color(current_hue_offset, i, self.max_points_to_draw)
            try:
                pygame.draw.line(surface, color, start_pos, end_pos, LINE_THICKNESS)
            except TypeError as e:
                print(f"Error drawing line: {e}, color: {color}, start: {start_pos}, end: {end_pos}")

    def is_fully_drawn(self):
        return self.drawing_started and self.current_point_idx >= self.max_points_to_draw - 1

    def reset(self, delay_idx):
        self.current_point_idx = 0
        self.hue_offset = random.randint(0, 360)
        self.scale = BASE_SCALE * (1 + random.uniform(-SCALE_VARIATION/BASE_SCALE/2, SCALE_VARIATION/BASE_SCALE/2))
        self.points = get_heart_points(self.scale, MAX_POINTS, self.center_x, self.center_y)
        self.drawing_started = False
        self.start_delay = delay_idx * INITIAL_DELAY_FACTOR

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Animated Neon Heart")
    clock = pygame.time.Clock()

    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30

    hearts = [AnimatedHeart(center_x, center_y, BASE_SCALE + i * (SCALE_VARIATION / NUM_HEARTS) - SCALE_VARIATION/2, i)
              for i in range(NUM_HEARTS)]

    running = True
    frame_count = 0
    all_hearts_drawn_once = False
    reset_timer = 0
    RESET_DELAY_FRAMES = FPS * 3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        still_drawing_any = False
        all_currently_drawn = True

        for heart in hearts:
            if heart.update(frame_count):
                still_drawing_any = True
            heart.draw(screen)
            if not heart.is_fully_drawn():
                all_currently_drawn = False

        if all_currently_drawn and not all_hearts_drawn_once:
            all_hearts_drawn_once = True
            reset_timer = frame_count

        if all_hearts_drawn_once and frame_count > reset_timer + RESET_DELAY_FRAMES:
            for i, heart in enumerate(hearts):
                heart.reset(i)
            all_hearts_drawn_once = False
            frame_count = -1
            reset_timer = 0

        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()

if __name__ == '__main__':
    main()