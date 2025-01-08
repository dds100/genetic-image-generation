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

# Generar una posible solucion
genome_size = height * width
genome = Genome(genome_size)

# Convertirla a tamaño de la imagen original
score = genome.get_image_score(image)
print(score)

# # Mostrar genoma
# plt.imshow(genome, cmap='gray')
# plt.show()