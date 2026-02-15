import os
os.environ['PYPHI_WELCOME_OFF'] = 'yes'
import collections.abc
import collections

import ModelInterpreter
import RenderController

collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.Sequence = collections.abc.Sequence
collections.MutableMapping = collections.abc.MutableMapping

import pyphi
import numpy as np

pyphi.config.PROGRESS_BARS = True
pyphi.config.VALIDATE_SUBSYSTEM_STATES = True
pyphi.config.PARALLEL_CONCEPT_EVALUATION = False
pyphi.config.PARALLEL_CUT_EVALUATION = False
pyphi.config.PARALLEL_COMPLEX_EVALUATION = False

if __name__ == '__main__':
    model_interpreter = ModelInterpreter.ModelInterpreter(
        'C:/Users/Tim/Desktop/Computer_Vision/Computer-Vision/Version_Results/Model_2/Models/model_epoch5.pth')

    tpm = np.array([
        [0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1],
        [1, 0.6, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 1],
        [0, 1, 1, 1], [0, 1, 0, 0], [1, 0, 1, 1], [1, 1, 0, 0],
        [1, 0, 0, 0], [0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0]
    ])

    cm = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 1]
    ])

    labels = ('A', 'B', 'C', 'D')

    network = pyphi.Network(tpm, cm=cm, node_labels=labels)
    state = (1, 0, 1, 1)
    sys_irreducibility_analysis = pyphi.compute.major_complex(network, state)

    render_controller = RenderController.RenderController(network, sys_irreducibility_analysis)
