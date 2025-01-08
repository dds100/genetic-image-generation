import cv2
import matplotlib.pyplot as plt
import numpy as np

from Genome import Genome

'''Implementación de diferentes algoritmos de reproducción.'''

genome_size = 100
genome1 = Genome(genome_size).genome
genome2 = Genome(genome_size).genome

print(genome1)
print(genome2)

child_genome = []
reasons = []
mutation_rate = .1
for i in range(genome_size):
    random_number = np.random.random()
    if random_number < mutation_rate:
        new_gen = np.random.randint(low=0, high=2)
        reason = 'mutation'
    elif random_number > 1 - (1 - mutation_rate)/2:
        new_gen = genome1[0][i]
        reason = 'genome1'
    else:
        new_gen = genome2[0][i]
        reason = 'genome2'
    child_genome.append(new_gen)
    reasons.append(reason)

print('Child genome:', child_genome)
print('Child genome:', type(child_genome))
print('Reasons:', reasons)
