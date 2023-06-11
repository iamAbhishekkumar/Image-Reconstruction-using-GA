import random
from PIL import ImageFont
import string


class Figures:
    def __init__(self, image, target_img) -> None:
        self.image = image
        self.target_img = target_img
        self.T_H, self.T_W = self.target_img.size

    def draw_rectangle(self, size=10):
        """Draw rectangle on image with given size."""
        x = random.randint(0, self.T_W-1)
        y = random.randint(0, self.T_H-1)

        color = (random.randint(0, 255))

        self.image.rectangle([(y, x), (y+size, x+size)], fill=color)

    def draw_line(self):
        """Draw random line on image."""
        x1 = random.randint(0, self.T_W-1)
        y1 = random.randint(0, self.T_H-1)

        x2 = random.randint(0, self.T_W-1)
        y2 = random.randint(0, self.T_H-1)

        color = (random.randint(0, 255))

        self.image.line([(y1, x1), (y2, x2)], fill=color,
                        width=1)

    def draw_text(self, size=20):
        """Draw random text on image with given size."""
        font = ImageFont.truetype("arial.ttf", size)
        text_length = random.randint(1, 3)
        text = "".join(random.choice(string.ascii_letters)
                       for i in range(text_length))

        x = random.randint(0, self.T_W-1)
        y = random.randint(0, self.T_H-1)

        color = (random.randint(0, 255))
        self.image.text((y, x), text, fill=color, font=font)

    def draw_circles(self, r=10):
        x = random.randint(0, self.T_W-2 * r)
        y = random.randint(0, self.T_H-2 * r)
        color = (random.randint(0, 255))
        self.image.ellipse((y, x, y+2 * r, x+2 * r), fill=color)
