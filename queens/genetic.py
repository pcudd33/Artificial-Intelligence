from random import *


def random_state(n):
    # putting the list in front of range creates a list instead of range which is
    # a generator and returns one value at a time
    state = list(range(n))
    shuffle(state)
    return state


def genetic_algorithm(mutation_rate, population_size):
    generation_count = 1
    best_state = []
    prev_generation = []
    next_generation = []
    weight = []

    while len(prev_generation) < population_size:
        # There is now a generation that is the size population_size full of random states
        prev_generation.append(random_state(16))

    while generation_count < 3000:
        temp_best = 0
        for j in range(len(prev_generation) - 1):
            # Checking for goal state
            if 0 == h(prev_generation[j]):
                return generation_count, prev_generation[j]
            else:
                # this is the comparison of the best state to any other state in current generation
                if fitness(prev_generation[j]) >= fitness(prev_generation[temp_best]):
                    # temp_best is the index of the best state within prev_gen
                    temp_best = j

        # Assign the best state based on the index within prev_gen
        best_state = prev_generation[temp_best]
        for k in prev_generation:
            weight.append(fitness(k))

            # Add the best state to the next generation
        next_generation.append(best_state)

        while len(next_generation) <= population_size:
            # Take the randomly chosen parents based on their fitness value and push them into the crossover
            # Function in order to preform the mutation and create the children for the next generation
            parent1, parent2 = choices(prev_generation, weights=weight, k=2)
            child1, child2 = crossover(parent1, parent2, mutation_rate)
            next_generation.append(child1)
            next_generation.append(child2)

        # Cleared the weight and prev_gen lists so they can be used again within the next iteration
        weight.clear()
        prev_generation.clear()

        # moving all states from next_gen into prev_gen to preform the functions above
        for e in next_generation:
            prev_generation.append(e)

        prev_generation.append(best_state)
        # This is clearing the next_gen after everything has been stored within prev_gen In order to redo the process
        next_generation.clear()
        generation_count += 1

    return generation_count, best_state


# This function will preform the crossover function for creating new generations as well as mutating the children
def crossover(parent1, parent2, mutation_rate):
    cross_index = randint(0, 15)

    # Created a child1/2 list the takes in the first half of the cross over and indexes through the second half to
    # append each element within the second half to the correct child
    child1 = parent1[0: cross_index]
    for element in parent2[cross_index: len(parent1)]:
        child1.append(element)

    child2 = parent2[0: cross_index]
    for element2 in parent1[cross_index: len(parent2)]:
        child2.append(element2)

    # Preform the mutation by generating a random integer to store within the child based off the mutation_rate
    for m in range(len(child1) - 1):
        if uniform(0, 1) <= mutation_rate:
            g = randint(0, 16)
            child1[m] = g

    for n in range(len(child2) - 1):
        if uniform(0, 1) <= mutation_rate:
            e = randint(0, 16)
            child2[n] = e

    # Return the two children that have been mutated in order to repopulate the next_gen
    return child1, child2


def fitness(state):
    n = len(state)
    fitness_rate = 0

    for r1 in range(n):
        c1 = state[r1]
        for r2 in range(r1 + 1, n):
            c2 = state[r2]
            # the fitness algorithm is counting the number of pairs that are not in conflict
            if c1 != c2 and abs(r1 - r2) != abs(c1 - c2):
                fitness_rate += 1

    return int(fitness_rate)


def h(state):
    n = len(state)
    pairs = 0

    for r1 in range(n):
        c1 = state[r1]
        for r2 in range(r1 + 1, n):
            c2 = state[r2]
            if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                pairs += 1

    return pairs


for test in range(10):
    gen_count, best_state1 = genetic_algorithm(0.05, 5)
    print("The number of attacking pairs of the best found state is", (h(best_state1)), "in", gen_count, "generations.")

