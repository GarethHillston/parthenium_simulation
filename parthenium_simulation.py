import numpy as np
from modelling import utilities, simulate

progress = np.load('./progressions/progress_indexed.npy', allow_pickle=True)

num_clusters = np.max(progress) + 1
transition_matrix = np.zeros((num_clusters, num_clusters), dtype=int)
start_classes = progress[0].flatten()
end_classes = progress[-1].flatten()

for i in range(len(start_classes)):
    transition_matrix[start_classes[i]][end_classes[i]] += 1

normalised_matrix = utilities.normalise_matrix(transition_matrix)

simulate.basic_markov_sim((2180, 2340), 50, normalised_matrix)
# simulate.basic_markov_sim((500, 500), 50, [[0.8, 0.2], [0.0, 1.0]])
