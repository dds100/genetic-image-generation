import cv2
import matplotlib.pyplot as plt
import numpy as np

from Generation import Generation

# Guardar gráfico de evolución de la puntuación
def save_score_plot(epochs: int):
    n = [x for x in range(epochs)]
    plt.plot(n, historic_scores)
    plt.grid()
    plt.title('Histórico de puntuaciones')
    plt.xlabel('Nº Generación')
    plt.ylabel('Píxeles en común con la imagen original')
    plt.savefig('runs\historic_score.png')
    plt.close()

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

# Ejecutar algoritmo genético
NUM_GENERACIONES = 301
initial_mutation_rate = 0.01
max_score = genome_size
historic_scores = []
for i in range(NUM_GENERACIONES):
    generation.set_population_score(image=image)
    generation.set_best_genomes()
    if i % 25 == 0: generation.represent_best_genome(image=image, show=False, save=False, save_dir='runs')

    historic_scores.append(generation.best_scores[0])
    save_score_plot(epochs=i+1)
    mutation_rate = initial_mutation_rate * (1 - generation.best_scores[0] / max_score)

    generation = generation.new_generation(mutation_rate=mutation_rate)


