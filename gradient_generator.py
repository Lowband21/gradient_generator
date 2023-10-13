import os
import random
from PIL import Image

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def interpolate_color(start_color, end_color, ratio):
    r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
    g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
    b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
    return (r, g, b)

def generate_multi_gradient(colors, image_width, image_height):
    img = Image.new("RGB", (image_width, image_height))
    section_width = image_width // (len(colors) - 1)
    
    for i in range(len(colors) - 1):
        for x in range(section_width):
            ratio = x / section_width
            color = interpolate_color(colors[i], colors[i+1], ratio)
            for y in range(image_height):
                img.putpixel((i * section_width + x, y), color)

    return img

if __name__ == "__main__":
    NUM_IMAGES = 1000
    IMAGE_WIDTH = 1000
    IMAGE_HEIGHT = 100
    MIN_COLORS = 2
    MAX_COLORS = 7
    OUTPUT_DIR = "multi_gradients"

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for i in range(NUM_IMAGES):
        num_colors = random.randint(MIN_COLORS, MAX_COLORS)
        colors = [random_color() for _ in range(num_colors)]
        gradient_image = generate_multi_gradient(colors, IMAGE_WIDTH, IMAGE_HEIGHT)
        gradient_image.save(os.path.join(OUTPUT_DIR, f"gradient_{i+1}.png"))
