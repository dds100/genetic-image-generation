import cv2
import matplotlib.pyplot as plt
import numpy as np

class Genome:

    def __init__(self, genome_size):
        self.genome = self.initialize_genome(genome_size)

    def initialize_genome(self, genome_size):
        return np.random.randint(low=0, high=2, size=(1, genome_size), dtype=np.int8)

    def get_image_score(self, image: np.ndarray):
        height, width = image.shape[:2]
        genome_copy = self.genome
        genome_copy.resize((height, width))
        common_pixels = cv2.bitwise_and(genome_copy, image)
        return np.count_nonzero(common_pixels)
    

class Generation:

    def __init__(self,
            population_size: int,
            mutation_rate: float = .5
        ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_poputlation()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            population.append(Genome())




    def cross(another_genome):
        pass


if __name__ == '__main__':

    genome = Genome()
    print(genome)