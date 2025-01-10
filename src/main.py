import cv2
import matplotlib.pyplot as plt
import numpy as np

from Generation import Generation
from utils import save_score_plot, create_runs_dir


# Leer tamaño de imagen de entrada
image_path = 'images\output_30x34.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convertir a binaria para poder hacer operaciones lógicas
_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
image = image / 255
image = image.astype(np.int8)
height, width = image.shape

# Generar una población de soluciones
genome_size = height * width
population_size = 100
generation = Generation(
    population_size=population_size,
    genome_size=genome_size,
)
print(generation)

# Crear ruta de guardado de experimentos
create_runs_dir()

# Ejecutar algoritmo genético
NUM_GENERACIONES = 301
initial_mutation_rate = 0.01
max_score = genome_size
historic_scores = []
for i in range(NUM_GENERACIONES):
    generation.set_population_score(image=image)
    generation.set_best_genomes()
    if i % 25 == 0: generation.represent_best_genome(image=image, show=False, save=True, save_dir='runs')

    historic_scores.append(generation.best_scores[0])
    save_score_plot(epochs=i+1, scores=historic_scores)
    mutation_rate = initial_mutation_rate * (1 - generation.best_scores[0] / max_score)

    generation = generation.new_generation(mutation_rate=mutation_rate)


