import cv2
import matplotlib.pyplot as plt
import numpy as np

# Lectura de imagen
image_path = 'eiffel_tower.jpg'
image = cv2.imread(image_path)

# A escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Umbralizado
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

# Reshape a más pequeña
output = cv2.resize(binary, None, fx=.3, fy=.3)

# # Mostrar imagen
# plt.imshow(output, cmap='gray')
# plt.show()

# Guardar imagen
cv2.imwrite('output.jpg', output)
