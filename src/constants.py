# Adjust hyperparameters
NUMBER_OF_GENERATIONS = 7500
POPULATION_NUMBER = 50  # How many images in 1 generation (without elitism)
MUTATION_CHANCE = 0.1  # Chance of mutating (adding random shapes)
MUTATION_STRENGTH = 1  # How many shapes to add in mutation
# Turn on/off elitism (transfering best images to next generation without crossover)
ELITISM = True
# How many best images transfer to next generation (elitism)
ELITISM_NUMBER = 4
STARTING_SHAPE_NUMBER = 6  # How many shapes to draw on each image in first generation

PRINT_EVERY_GEN = 25  # Print fitness value every x generations
# Save best image every x generations for gif creation
SAVE_FRAME_FOR_GIF_EVERY = 100
