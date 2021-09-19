from itertools import permutations
from unittest import main, TestCase


def tsp(graph, s=0, V=4):
    v = []
    for i in range(V):
        if i != s:
            v.append(i)
    min_ = float("inf")
    next_ = permutations(v)
    for i in next_:
        weight = 0
        k = s
        for j in i:
            weight += graph[k][j]
            k = j
        weight += graph[k][s]
        min_ = min(min_, weight)
    return min_


class Test(TestCase):

    data = (
        [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ],
    )


    def test_tsp(self):
        self.assertEqual(tsp(self.data[0]), 80)


if __name__ == "__main__":
    main()