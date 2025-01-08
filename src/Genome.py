import cv2
import matplotlib.pyplot as plt
import numpy as np


class Genome:

    def __init__(self, brute_genome=None, genome_size=None):
        if brute_genome is not None:
            self.genome = np.array(brute_genome)
            if len(self.genome.shape) == 1: self.genome_size = self.genome.shape[0]
            else: self.genome_size = self.genome.shape[0] * self.genome.shape[1]
        else:
            self.genome_size = genome_size
            self.genome = self.initialize_random_genome(genome_size)

    def __repr__(self):
        return f'Genome({self.genome})'

    def initialize_random_genome(self, genome_size):
        return np.random.randint(low=0, high=2, size=(genome_size,), dtype=np.int8)

    def get_image_score(self, image: np.ndarray) -> int:
        height, width = image.shape[:2]
        genome_copy = self.genome
        genome_copy.resize((height, width))
        common_pixels = cv2.bitwise_and(genome_copy, image)
        return np.count_nonzero(common_pixels)
    
    def reproduce(self, another_genome: "Genome", mutation_rate: float = .1) -> "Genome":
        child_genome = []
        for i in range(self.genome_size):
            random_number = np.random.random()
            if random_number < mutation_rate:
                new_gen = np.random.randint(low=0, high=2)
            elif random_number > 1 - (1 - mutation_rate)/2:
                new_gen = self.genome[i]
            else:
                new_gen = another_genome.genome[i]
            child_genome.append(new_gen)
        return Genome(child_genome)
        
    
class Generation:

    def __init__(self,
            population_size: int,
            mutation_rate: float = .5
        ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            population.append(Genome())


if __name__ == '__main__':

    brute_genome = np.array([0, 1, 1, 0])
    # genome = Genome(brute_genome)
    genome = Genome(genome_size=10)
    print(genome)