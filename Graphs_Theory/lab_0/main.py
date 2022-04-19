"""
This program checks isomorphic characteristics of two different graphs
"""
from itertools import permutations


MATRIX_SIZE = 3


def generator_numbers(n: int) -> list[int]:
    return [i for i in range(0, n)]


def is_isomorphic(a1: list[list[int]], a2: list[list[int]], v) -> bool:
    """
    :param a1: first graph
    :type a1: list[list[int]]
    :param a2: second graph
    :type a2: list[list[int]]
    :return: are two graphs isomorphic? (bool)
    """

    for i in range(len(v)):
        for j in range(len(v)):
            print(a1[i][j], a2[v[i]][v[j]])
            if a1[i][j] != a2[v[i]][v[j]]:
                return False
    return True


if __name__ == '__main__':
    graph1 = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    graph2 = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
    p = permutations([i for i in range(MATRIX_SIZE)])

    for k in p:
        if is_isomorphic(graph1, graph2, k):
            print("True")
            break
