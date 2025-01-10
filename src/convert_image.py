import cv2
import matplotlib.pyplot as plt
import numpy as np

# Lectura de imagen
# image_path = 'images\eiffel_tower.jpg'
image_path = 'images\pikachu.png'
image = cv2.imread(image_path)

# A escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Umbralizado
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# # Reshape a más pequeña
# output = cv2.resize(binary, None, fx=.05, fy=.05)
output = binary

# # Mostrar imagen
# plt.imshow(gray, cmap='gray')
# plt.show()

# Guardar imagen
height, width = output.shape[:2]
cv2.imwrite(f'images\output_{height}x{width}.jpg', output)
