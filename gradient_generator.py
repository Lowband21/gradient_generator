import os
import random
from PIL import Image

def random_color():
    """
    Generate a random RGB color.

    :return: Tuple containing RGB values of a random color.
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_gradient(start_color, end_color, image_width, image_height):
    """
    Generate a gradient image from start_color to end_color.

    :param start_color: Tuple containing RGB values of the start color.
    :param end_color: Tuple containing RGB values of the end color.
    :param image_width: Width of the output image.
    :param image_height: Height of the output image.
    :return: A gradient image.
    """
    img = Image.new("RGB", (image_width, image_height))

    for y in range(image_height):
        for x in range(image_width):
            ratio = x / image_width
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            img.putpixel((x, y), (r, g, b))

    return img

if __name__ == "__main__":
    NUM_IMAGES = 1000
    IMAGE_WIDTH = 1000
    IMAGE_HEIGHT = 100
    OUTPUT_DIR = "random_gradients"

    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Generate and save random gradient images
    for i in range(NUM_IMAGES):
        start = random_color()
        end = random_color()
        gradient_image = generate_gradient(start, end, IMAGE_WIDTH, IMAGE_HEIGHT)
        gradient_image.save(os.path.join(OUTPUT_DIR, f"gradient_{i+1}.png"))
