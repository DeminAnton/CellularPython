from random import choices, sample, random, choice


def gen_individual(lenght: int) -> list:
    return choices((0, 1), k=lenght)


def gen_population(size: int, lenght: int) -> list:
    return [gen_individual(lenght) for _ in range(size)]


def fitness(individual):
    return sum(individual)


def selection(population, k=5):
    s = sample(population, k)
    d = {}
    for individual in s:
        d[fitness(individual)] = individual
    max_key = max(d)
    return d[max_key]


def mutation(individual, prob: float = 0.01):
    mutant = []
    for gen in individual:
        if random() < prob:
            mutant.append(choice((0, 1)))
        else:
            mutant.append(gen)
    return mutant


def breeding(ind_1, ind_2):
    point = len(ind_1) // 2
    child = ind_1[:point] + ind_2[point:]
    return mutation(child)


def remake(population):
    size = len(population)
    new_population = []
    for _ in range(size):
        ind_1 = selection(population, k=20)
        ind_2 = selection(population, k=20)
        child = breeding(ind_1, ind_2)
        new_population.append(child)
    return new_population


population = gen_population(2000, 1000)
print(*population, sep="\n")
loop_flag = input()
while loop_flag == "":
    avg_fitness = sum([fitness(ind) for ind in population]) / len(population)
    print(avg_fitness)
    population = remake(population)
    loop_flag = input()

print(max([fitness(ind) for ind in population]), sep="\n")
