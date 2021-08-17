import numpy as np
import utilities
from modelling import transition_matrix, simulate
import xarray as xr

filePath = '/scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

dates = utilities.get_dates(raw_data)

# file_root = './progressions/19_20_binaries/'
# last_prediction = np.load(file_root + 'prediction_' + dates[0].split('T')[0] + '.npy', allow_pickle=True)
# matrix_stack = []
#
# for i in range(1, len(dates)):
#     date = dates[i]
#     date_neat = date.split('T')[0]
#     prediction = np.load(file_root + 'prediction_' + date_neat + '.npy', allow_pickle=True)
#     matrix_stack.append(transition_matrix.create(np.dstack((last_prediction, prediction))))
#     last_prediction = prediction
#
# np.save('./matrices/2019_2020/binary_stack_nanned.npy', matrix_stack)

# matrix_stack = np.load('modelling/matrices/2019_2020/binary_stack_nanned.npy', allow_pickle=True)
# avg_matrix = np.average(matrix_stack, axis=0)
# np.save('modelling/matrices/2019_2020/binary_matrix.npy', avg_matrix)

# needs integer arrays, not objects
matrix = np.load('modelling/matrices/2019_2020/binary_matrix.npy', allow_pickle=True)
start_state = np.load('modelling/start_states/binary_start.npy', allow_pickle=True)
#matrix = [[0.2, 0.8], [0.01, 0.99]]
simulate.markov(start_state, 50, matrix)
# simulate.markov_test((200, 200), 50, matrix)
