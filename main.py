import collections.abc
import collections

import Render_Controller

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
pyphi.config.PARALLEL_CUT_EVALUATION = True
pyphi.config.PARALLEL_COMPLEX_EVALUATION = True
pyphi.config.WELCOME_OFF = True

if __name__ == '__main__':
    tpm = np.array([
        [1,0,1],
        [0,1,0],
        [0,1,1],
        [0,0,1],
        [0,0,0],
        [1,1,1],
        [1,0,1],
        [1,1,0]
    ])

    cm = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ])

    labels = ('A', 'B', 'C')

    network = pyphi.Network(tpm, cm=cm, node_labels=labels)
    state = (1, 0, 1)

    sys = pyphi.Subsystem(network, state)

    sys_irreducibility_analysis = pyphi.compute.sia(sys)
    print(sys_irreducibility_analysis)

    print(sys_irreducibility_analysis.phi)
    print(sys_irreducibility_analysis.cut)
    print(len(sys_irreducibility_analysis.ces))
    render_controller = Render_Controller.RenderController(network, sys_irreducibility_analysis)
