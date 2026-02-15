import os
os.environ['PYPHI_WELCOME_OFF'] = 'yes'
import collections.abc
import collections

import ModelInterpreter
import RenderController

# This fixes the issue for ALL pyphi files at once
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
        [0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1],  # States 0-3
        [1, 0.6, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 1],  # States 4-7
        [0, 1, 1, 1], [0, 1, 0, 0], [1, 0, 1, 1], [1, 1, 0, 0],  # States 8-11
        [1, 0, 0, 0], [0, 0, 1, 1], [1, 1, 1, 0], [1, 0, 1, 0]  # States 12-15
    ])

    cm = np.array([
        [0, 1, 1, 0],  # A influences B, C
        [1, 0, 1, 0],  # B influences A, C
        [1, 1, 0, 1],  # C influences A, B, D
        [0, 0, 1, 1]  # D influences C
    ])

    labels = ('A', 'B', 'C', 'D')
    state = (1, 0, 1, 1)

    network = pyphi.Network(tpm, cm=cm, node_labels=labels)


    sys_irreducibility_analysis = pyphi.compute.major_complex(network, state)
    print(sys_irreducibility_analysis)
    print(sys_irreducibility_analysis.subsystem)


    render_controller = RenderController.RenderController(network, sys_irreducibility_analysis)



