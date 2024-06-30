import random

class Genetic:
    def __init__(self):
        pass

    # Step 1: Generate the initial population
    @staticmethod
    def generate_initial_population(pop_size, individual_length):
        return [[random.randint(0, 1) for _ in range(individual_length)] for _ in range(pop_size)]

    @staticmethod
    def calculate_y(individual):
        return [1 - bit for bit in individual]

    # Step 2: Calculate the fitness function as x*x + x*y + y*y
    @staticmethod
    def calculate_fitness(x, y):
        x_decimal = int("".join(map(str, x)), 2)
        y_decimal = int("".join(map(str, y)), 2)
        return x_decimal * x_decimal + x_decimal * y_decimal + y_decimal * y_decimal

    # Step 3: Select the best parents using rank probability system
    @staticmethod
    def select_best_parents(population, fitnesses, num_parents):
        sorted_population = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
        probabilities = [i/sum(range(1, len(population)+1)) for i in range(1, len(population)+1)]
        selected = random.choices(sorted_population, weights=probabilities, k=num_parents)
        return selected

    # Step 4: Perform single point crossover
    @staticmethod
    def single_point_crossover(parent1, parent2):
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

    # Step 5: Apply mutation
    @staticmethod
    def mutate(individual):
        point = random.randint(0, len(individual) - 1)
        individual[point] = 1 - individual[point]

    def run(self):
        pop_size = 10
        individual_length = 6
        population = self.generate_initial_population(pop_size, individual_length)
        #print("Initial Population: ", population)        
        fitnesses = []
        y = []
        for individual in population:
            y_cal = self.calculate_y(individual)
            y.append(y_cal)
            fitness = self.calculate_fitness(individual, y_cal)
            fitnesses.append(fitness)        
        #print("Corresponding Y : ", y)
        #print("Calculated fitness: ", fitnesses)        
        num_parents = 2
        parents = self.select_best_parents(population, fitnesses, num_parents)
        #print("Selected Parents: ", parents)        
        offspring1, offspring2 = self.single_point_crossover(parents[0], parents[1])
        #print("Offspring 1: ", offspring1)
        #print("Offspring 2: ", offspring2)        
        self.mutate(offspring1)
        self.mutate(offspring2)
        #print("Offspring 1 After Mutation: ", offspring1)
        #print("Offspring 2 After Mutation: ", offspring2)
        return int("".join(map(str, offspring1)), 2)

    @staticmethod
    def main():
        program = Genetic()
        ans = program.run()
        return ans

if __name__ == "__main__":
    ans = Genetic.main()
    print(ans)