import random
import time
from math import exp


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def calculate_cost(route):
    cost = 0
    for i in range(0, n):
        city_A = route[i - 1]
        city_B = route[i]
        cost = cost + cities[city_A][city_B]
    return cost


def generate_random_route(number_of_cities):
    l = list(range(number_of_cities))
    random.shuffle(l)
    return l


def generate_random_cities(number_of_cities):
    cities = [[0 for i in range(number_of_cities)] for j in range(number_of_cities)]
    for i in range(0, number_of_cities):
        for j in range(0, number_of_cities):
            if i > j:
                random_number = random.randint(1, 50)
                cities[i][j] = random_number
                cities[j][i] = random_number
    return cities


def generate_neighbors(route, n):
    my_neighbors = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            new_neighbor = swapPositions(route, i, j).copy()
            my_neighbors.append(new_neighbor)

    return my_neighbors


n = int(input("Please Insert the number of cities: "))
cities = generate_random_cities(n)
random_route = generate_random_route(n)
cost = calculate_cost(random_route)
best_route = random_route
steps = 0
tic = time.time()

T = 100.0
reduction_rate = 0.999

while steps == 100:
    cost = calculate_cost(best_route)
    neighbors = generate_neighbors(best_route, n)
    best_cost = cost
    T = T * reduction_rate
    random_neighbor_index = random.randint(0, len(neighbors))
    new_route_cost = calculate_cost(neighbors[random_neighbor_index])
    deltaE = new_route_cost - best_cost
    # print(exp(deltaE / T))
    if new_route_cost < best_cost or exp(deltaE / T) > random.uniform(0, 1):
        best_route = neighbors[random_neighbor_index].copy()
        best_cost = new_route_cost
        break
    steps += 1


toc = time.time()
sec = toc - tic

print("Best Route is: " + str(best_route))
print("Best Cost is: " + str(best_cost))
print(f"This Algorithm Solved this Problem in {steps} steps")
print(f"We reached this route in {sec} second")
print(f"Final T is {T}")
