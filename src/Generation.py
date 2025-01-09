import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

from Genome import Genome

class Generation:

    def __init__(self,
            population: list = None,
            population_size: int = None,
            genome_size: int = None,
            generation_number: int = 0
        ):
        if population is None:
            self.population_size = population_size
            self.population = self.initialize_population(genome_size=genome_size)
        else:
            self.population = population
            self.population_size = len(population)
        self.generation_number = generation_number
        self.scores = []
        self.best_genomes = []
        self.best_scores = []

    def __repr__(self):
        return f'Generation object with {self.population_size} genomes'

    # Generar una población de soluciones
    def initialize_population(self, genome_size: int):
        population = []
        for _ in range(self.population_size):
            genome = Genome(genome_size=genome_size)
            population.append(genome)
        return population

    # Medir la puntuación de cada solución
    def set_population_score(self, image: np.ndarray):
        scores = []
        for genome in self.population:
            score = genome.get_image_score(image)
            scores.append(score)
        self.scores = scores
        
    # Ordenar la población para obtener los dos mejores genomas
    def set_best_genomes(self):
        population_scores = zip(self.population, self.scores)
        population_scores = sorted(population_scores, key=lambda item: -item[1])
        best_items = population_scores[:2]
        self.best_genomes = [item[0] for item in best_items]
        self.best_scores = [item[1] for item in best_items]

    # Cruzar esos dos genomas para crear una nueva generación
    def new_generation(self, mutation_rate: float = .1) -> "Generation":
        population = []
        for _ in range(self.population_size):
            genome = self.best_genomes[0].reproduce(self.best_genomes[1], mutation_rate=mutation_rate)
            population.append(genome)
        return Generation(
            population=population,
            generation_number=self.generation_number + 1
        )
    
    # Representar mejor genoma
    def represent_best_genome(
            self, 
            image: np.ndarray = None,
            show: bool = True,
            save: bool = False,
            save_dir: str = ''
        ):
        height, width = image.shape[:2]
        best_genome = self.best_genomes[0].genome.astype(np.int8).copy()
        best_genome.resize((height, width))
        if show:
            plt.subplot(1, 2, 1)
            plt.imshow(image, cmap='gray')
            plt.subplot(1, 2, 2)
            plt.imshow(best_genome, cmap='gray')
            plt.title(f'Número de píxeles coincidentes: {self.best_scores[0]}')
            plt.show()
        if save:
            save_name = f'best_generation_{self.generation_number}.png'
            save_path = os.path.join(save_dir, save_name)
            cv2.imwrite(save_path, best_genome.astype(np.int32)*255)
