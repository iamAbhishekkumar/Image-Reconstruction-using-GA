import random
from PIL import Image
import cv2
import numpy as np
import imageio  # For gif saving
from src.constants import *
from src.utils import Utils


def info(image, text, coordinates):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 255)
    thickness = 1
    image = cv2.putText(image, text, coordinates, font,
                        fontScale, color, thickness, cv2.LINE_AA)


def combine(img1, img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # create empty matrix
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)

    # combine 2 images
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    return vis


c = 0


def pipleline(path_to_img, shape):

    # Loading image convering to B/W
    target_img = Image.open(path_to_img).convert("L")

    gif_imgs = []  # Creating empty frames list for gif saving at the end

    # Creating first generation
    utils = Utils(target_img, shape)
    print(shape)
    population = utils.create_random_population(POPULATION_NUMBER)
    blck_img = np.zeros(
        (target_img.size[1], target_img.size[0] + 200), dtype=np.uint8)

    # Looping through generations
    for generation in range(0, NUMBER_OF_GENERATIONS):

        # Calculating similarity of each image in population to original image
        fitnesses = []
        for img in population:
            actual_fitness = utils.evaluate_fitness(img)
            fitnesses.append(actual_fitness)

        # Get ids of best images in population
        top_population_ids = np.argsort(fitnesses)[-ELITISM_NUMBER:]

        # Creating new population for next generation
        new_population = []

        # Connect parent into pairs
        parents_list = utils.get_parents(population, fitnesses)

        # Creating childs
        for i in range(0, POPULATION_NUMBER):
            new_img = utils.crossover(parents_list[i][0], parents_list[i][1])
            # Mutate
            if random.uniform(0.0, 1.0) < MUTATION_CHANCE:
                new_img = utils.mutate(new_img, MUTATION_STRENGTH)
            new_population.append(new_img)

        # Elitism transfer
        if ELITISM:
            for ids in top_population_ids:
                new_population.append(population[ids])

        # Get best actual image and show it
        open_cv_image = np.array(population[top_population_ids[0]])
        open_cv_image = combine(open_cv_image, blck_img)
        open_cv_image = combine(open_cv_image, np.asarray(target_img))
        info(open_cv_image,
             f"Generation : {generation}", (target_img.size[0] + 100, 50))
        info(open_cv_image,
             f"Fitness : {top_population_ids[0]}", (target_img.size[0] + 100, 100))
        # Gif creation

        ret, buffer = cv2.imencode('.jpg', open_cv_image)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        if generation % SAVE_FRAME_FOR_GIF_EVERY == 0:
            gif_imgs.append(open_cv_image)

        population = new_population

    # Save gif and best output
    imageio.mimsave(f"outputs/gifs/output.gif", gif_imgs)
    cv2.imwrite(f"outputs/imgs/output.jpg", open_cv_image)
