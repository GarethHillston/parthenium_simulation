import numpy as np

from imaging import render
from modelling import simulate

matrix = np.load('lulc_parth_combined_model/transition_matrix.npy', allow_pickle=True)
start_state = np.load('lulc_parth_combined_model/start_state.npy', allow_pickle=True)
land_classes = np.load('lulc_parth_combined_model/19_20_rawalpindi_land_classes.npy', allow_pickle=True)
land_classes = land_classes[0]

# lulc_proportions = np.load('lulc_parth_combined_model/parth_lulc_proportions_19_20.npy', allow_pickle=True)
# print(lulc_proportions)

lulc_proportions = [0.8, 0.7, 0.3, 0.2, 0.1, 0.1, 0, 0]

# render.single_plot(land_classes, '', render.eight_colours, '')

simulate.markov_lulc(start_state, matrix, land_classes, lulc_proportions, 20, 'lulc_parth_combined_model/testing')
