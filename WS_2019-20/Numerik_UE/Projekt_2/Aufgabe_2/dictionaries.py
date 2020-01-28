import numpy as np
from random import shuffle

# playing around with dics ... no, dictionaries you pervert!!!

eigen_pairs_unsorted = {}
eigen_pairs_sorted = {}

n = 3
random_list = [i+1 for i in range(n)]

for _ in range(n):
    shuffle(random_list)

for i, key in enumerate(random_list):
    eigen_pairs_unsorted[key] = np.eye(len(random_list))[i, :]

eigen_pairs_unsorted.update([(0, np.zeros((len(random_list))))])

print(eigen_pairs_unsorted, "\n")

for eigen_value in sorted(eigen_pairs_unsorted.keys()):
    eigen_pairs_sorted[eigen_value] = eigen_pairs_unsorted[eigen_value]

print(eigen_pairs_sorted, "\n")

for eigen_pair in list(eigen_pairs_sorted.items()):
    print(eigen_pair)

print("")

for eigen_value in eigen_pairs_sorted.keys():
    print(eigen_value)
    eigen_vector = eigen_pairs_sorted[eigen_value]
    print(eigen_vector)