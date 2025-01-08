import cv2
import matplotlib.pyplot as plt
import numpy as np

from Genome import Genome

# Leer tamaño de imagen de entrada
image_path = 'images\output.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convertir a binaria para poder hacer operaciones lógicas
_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
image = image / 255
image = image.astype(np.int8)
height, width = image.shape

# Generar una población de soluciones
genome_size = height * width
population_size = 100
population = []
for i in range(population_size):
    genome = Genome(genome_size=genome_size)
    population.append(genome)
print('Población de soluciones:', population)

# Medir la puntuación de cada solución
scores = []
for genome in population:
    score = genome.get_image_score(image)
    scores.append(score)
print('Scores:', scores)

# Ordenar la población para obtener los dos mejores genomas
population_scores = zip(population, scores)
population_scores = sorted(population_scores, key=lambda item: -item[1])
best_items = population_scores[:2]
print('Dos mejores genomas:', best_items)

# Cruzar esos dos genomas para crear una nueva generación
population = []
for i in range(population_size):
    genome = best_items[0][0].reproduce(best_items[1][0])
    population.append(genome)
print('Generación nueva:', population)

# Medir la puntuación de cada solución
scores = []
for genome in population:
    score = genome.get_image_score(image)
    scores.append(score)
print('Scores:', scores)


# # Mostrar genoma
# plt.imshow(genome, cmap='gray')
# plt.show()