import cv2
import matplotlib.pyplot as plt
import numpy as np

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
genome = np.random.randint(low=0, high=2, size=(1, genome_size), dtype=np.int8)
print(genome)
print(type(genome))

# Convertirla a tamaño de la imagen original
genome.resize((height, width))
print(genome.shape)

# Contar los píxeles en común con la imagen a generar
common_pixels = cv2.bitwise_and(genome, image)
fitness = np.count_nonzero(common_pixels)
print(fitness)

# Mostrar genoma
plt.imshow(common_pixels, cmap='gray')
plt.show()