from PIL import Image
import os

ASCII = ["@", "#", "8", "&", "%", "o", ":", "*", "+", ";", ",", ".", " "]

def resize_img(img, new_width = 200, correction = 2.5):
    width, height = img.size
    aspect_ratio = width / height
    new_height = int(new_width / (aspect_ratio * correction))
    return img.resize((new_width, new_height))

def get_pixels(img):
    grayscale_img = img.convert("L")
    pixels = list(grayscale_img.getdata())
    return pixels

def map_pixels(pixels):
    ascii_pixels = [ASCII[min(x // 18, len(ASCII) - 1)] for x in pixels]
    return ascii_pixels

def format_art(ascii_pixels, width = 200):
    ascii_lines = []
    for i in range(0, len(ascii_pixels), width):
        ascii_lines.append(''.join(ascii_pixels[i:i + width]))
    return "\n".join(ascii_lines)

def main():
    img_name = "sample.jpg"
    img = Image.open(os.path.join(os.getcwd(), "images", img_name))
    img = resize_img(img, 200)
    pixels = get_pixels(img)
    ascii_pixels = map_pixels(pixels)
    output = format_art(ascii_pixels, 200)
    
    with open("art.txt", "w") as f:
        f.write(output)

main()
