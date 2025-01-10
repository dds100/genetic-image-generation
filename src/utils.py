import os
import matplotlib.pyplot as plt


def create_runs_dir():
    os.makedirs('runs', exist_ok=True)


# Guardar gráfico de evolución de la puntuación
def save_score_plot(epochs: int, scores: list):
    n = [x for x in range(epochs)]
    plt.plot(n, scores)
    plt.grid()
    plt.title('Histórico de puntuaciones')
    plt.xlabel('Nº Generación')
    plt.ylabel('Píxeles en común con la imagen original')
    plt.savefig('runs\historic_score.png')
    plt.close()