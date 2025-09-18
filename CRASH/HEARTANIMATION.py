import turtle
import math
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")  # Black background
screen.title("Sleek Modern Heart Animation")
screen.tracer(0)  # Turn off animation for manual updates

# Create the main heart turtle
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)

# Create the glow effect turtle
glow = turtle.Turtle()
glow.hideturtle()
glow.speed(0)

def draw_heart_curve(t, size, color, pen_size=2):
    """Draw a heart using a mathematical curve with specified parameters"""
    t.clear()
    t.pensize(pen_size)
    t.color(color)
    t.penup()
    t.goto(0, -size/3)
    t.pendown()
    t.begin_fill()
    
    # Use parametric equation to draw a heart
    for angle in range(0, 360, 1):
        rad = math.radians(angle)
        x = size * 16 * math.sin(rad) ** 3
        y = size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
        t.goto(x, y)
    
    t.end_fill()

def pulse_effect(ratio):

    eased_ratio = (math.sin(ratio * math.pi * 2 - math.pi/2) + 1) / 2
    return eased_ratio

def get_red_shade(ratio):
    """Get a shade of red based on ratio"""
    intensity = int(255 * ratio)
    return f"#{intensity:02x}0000"

# Animation parameters
base_size = 10
max_size = 15
min_glow_size = 14
max_glow_size = 18
animation_speed = 0.01
pulse_speed = 0.005

# Main animation loop
pulse_ratio = 0.0
heartbeat_stage = 0  # 0 = normal, 1 = first beat, 2 = brief pause, 3 = second beat
heartbeat_timer = 0
heartbeat_sequence = [0.3, 0.1, 0.3, 1.0] 
heartbeat_scale = [1.0, 1.3, 1.1, 1.6] 

try:
    while True:
        heartbeat_timer += animation_speed
        if heartbeat_timer >= heartbeat_sequence[heartbeat_stage]:
            heartbeat_timer = 0
            heartbeat_stage = (heartbeat_stage + 1) % 4
        
        current_pulse = pulse_effect(pulse_ratio)
        size_factor = heartbeat_scale[heartbeat_stage]
        heart_size = base_size + (max_size - base_size) * size_factor * current_pulse
        glow_size = min_glow_size + (max_glow_size - min_glow_size) * current_pulse
        
        pulse_ratio += pulse_speed
        if pulse_ratio > 1.0:
            pulse_ratio = 0.0
        
        # Create glowing effect
        draw_heart_curve(glow, glow_size, "#3d0000", 10)  # Dark red glow
        
        # Draw the main heart
        red_intensity = 0.7 + current_pulse * 0.3  # Vary between 70% and 100% red
        red_color = get_red_shade(red_intensity)
        draw_heart_curve(heart, heart_size, red_color, 2)
        
        # Stamp the center for extra effect
        stamp = turtle.Turtle()
        stamp.hideturtle()
        stamp.penup()
        stamp.shape("circle")
        stamp.color("#ff1a1a")  # Bright red
        stamp.shapesize(heart_size/10)
        stamp.goto(0, heart_size/3)
        stamp.stamp()
        stamp.hideturtle()
        del stamp
        
        # Update screen
        screen.update()
        time.sleep(animation_speed)
        
except KeyboardInterrupt:
    print("Animation stopped")