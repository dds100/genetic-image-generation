# Genetic Algorithm for Image Generation

![Example](assets\output.gif)

## About
**This project has no practical applications at all. Its only purpose was coding for fun and make a first approach to genetic algorithms with Python.**

This project is an implementation of a Genetic Algorithm. What it does is:

- From a binary image, generate a random population of binary images of the same size than the original binary image.
- Every genome gets a score based on the similarity with the original image.
- The best genomes in every generation are combined or reproduced in order to create sucessive generations. There are random mutations in this reproduction process, which helps adding variability (avoiding local maximums).

In reality, this kind of algorithms just change its parameters just to optimize a given score function.


## How to use
You can simply run "main.py" and you will see plots of score through generations. You will see that output images are completely random in first generations and randomness disappears little by little.

You can also vary some parameters, as the population size in every generation, mutation rate in reproduction process; or maybe try some more complex images or code some other reproduction methods.