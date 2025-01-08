import cv2
import matplotlib.pyplot as plt
import numpy as np

from Genome import Genome

'''Implementación de diferentes algoritmos de reproducción.'''

genome_size = 10
genome1 = Genome(genome_size=genome_size)
genome2 = Genome(genome_size=genome_size)

print(genome1)
print(genome2)

child_genome = genome1.reproduce(genome2)

print('Child genome:', child_genome)
print('Child genome:', type(child_genome))
