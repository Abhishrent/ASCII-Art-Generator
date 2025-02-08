from PIL import Image
import os

class ASCIIArt:
    ASCII_CHARS = ["@", "#", "8", "&", "%", "o", ":", "*", "+", ";", ",", ".", " "]
    
    def __init__(self, image_path, width=200, correction=2.5):
        self.image_path = image_path
        self.width = width
        self.correction = correction
        self.image = Image.open(self.image_path)
        
    def resize_img(self):
        width, height = self.image.size
        aspect_ratio = width / height
        new_height = int(self.width / (aspect_ratio * self.correction))
        self.image = self.image.resize((self.width, new_height))
    
    def get_pixels(self):
        grayscale_img = self.image.convert("L")
        return list(grayscale_img.getdata())
    
    def map_pixels(self, pixels):
        scale_factor = 256 / len(self.ASCII_CHARS)
        return [self.ASCII_CHARS[min(int(x / scale_factor), len(self.ASCII_CHARS) - 1)] for x in pixels]
    
    def format_art(self, ascii_pixels):
        ascii_lines = []
        for i in range(0, len(ascii_pixels), self.width):
            ascii_lines.append(''.join(ascii_pixels[i:i + self.width]))
        return "\n".join(ascii_lines)
    
    def generate_ascii_art(self, output_file="art.txt"):
        self.resize_img()
        pixels = self.get_pixels()
        ascii_pixels = self.map_pixels(pixels)
        output = self.format_art(ascii_pixels)
        
        with open(output_file, "w") as f:
            f.write(output)
        print(f"ASCII art saved to {output_file}")

if __name__ == "__main__":
    image_path = os.path.join(os.getcwd(), "images", "sample.jpg")
    ascii_art = ASCIIArt(image_path)
    ascii_art.generate_ascii_art()
