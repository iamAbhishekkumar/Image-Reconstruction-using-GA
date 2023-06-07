import random
import numpy as np
from src.figures import Figures
from src.constants import *
from PIL import ImageDraw, Image
from skimage.metrics import peak_signal_noise_ratio as psns
from src.imageProcessing import ImageProcessing


class Utils:
    def __init__(self, target_img, fig: str) -> None:
        self.target_img = target_img
        self.T_H, self.T_W = self.target_img.size
        self.fig = fig

    def add_random_shape_to_image(self, image, number_of_shapes):
        """Add shape with random proporties to image number_of_shapes times."""
        image_filled = image.copy()

        for _ in range(0, number_of_shapes):
            draw = ImageDraw.Draw(image_filled)
            figure = Figures(draw, self.target_img)
            if self.fig == 'circle':
                figure.draw_circles()
            elif self.fig == 'rectangle':
                figure.draw_rectangle()
            elif self.fig == 'line':
                figure.draw_line()
            elif self.fig == 'text':
                figure.draw_text()
        return image_filled

    def create_random_population(self, size):
        """Create first generation with random population."""
        first_population = []
        for _ in range(0, size):
            blank_image = Image.new("L", (self.T_H, self.T_W))
            filled_image = self.add_random_shape_to_image(
                blank_image, MUTATION_STRENGTH)
            first_population.append(filled_image)
        return first_population

    def evaluate_fitness(self, image):
        """Evaluate similarity of image with original."""
        return psns(np.array(image), np.array(self.target_img))

    def crossover(self, image1, image2):
        """Make crossover operation on two images."""
        return ImageProcessing(self.target_img).random_horizontal_swap(image1, image2)

    def mutate(self, image, number_of_times):
        """Mutate image adding random shape number_of_times."""
        mutated = self.add_random_shape_to_image(image, number_of_times)
        return mutated

    def get_parents(self, local_population, local_fitnesses):
        """Connect parents in pairs based on fitnesses as weights using softmax."""
        fitness_sum = sum(np.exp(local_fitnesses))
        fitness_normalized = np.exp(local_fitnesses) / fitness_sum
        local_parents_list = []
        for _ in range(0, len(local_population)):
            parents = random.choices(
                local_population, weights=fitness_normalized, k=2)
            local_parents_list.append(parents)
        return local_parents_list
