import bisect
from utils import distance


def simulate(body, rounds=100000, verify_points=False):
    simulation = []
    for _ in range(rounds):
        a = body.get_random_point()
        b = body.get_random_point()
        if verify_points:
            assert body.is_inside(a)
            assert body.is_inside(b)
        simulation.append(distance(a, b))
    simulation.sort()
    return simulation


def cumulative_function(simulation, x):
    return bisect.bisect_right(simulation, x) / len(simulation)


def cumulative_function_graph(body, simulation, steps=1000):
    delta_x = body.diameter / steps
    x_coords = [i * delta_x for i in range(steps + 1)]
    y_coords = [cumulative_function(simulation, x) for x in x_coords]
    return x_coords, y_coords
