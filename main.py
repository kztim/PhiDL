import os
import warnings

import pandas as pd

from numpy.exceptions import VisibleDeprecationWarning
os.environ['PYPHI_WELCOME_OFF'] = 'yes'
warnings.filterwarnings("ignore", category=VisibleDeprecationWarning)

import collections.abc
import collections
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.Sequence = collections.abc.Sequence
collections.MutableMapping = collections.abc.MutableMapping

from ModelInterpreter import ModelInterpreter
from RenderController import RenderController
from DatasetGenerator import DatasetGenerator

import pyphi
import numpy as np

pyphi.config.PROGRESS_BARS = True
pyphi.config.VALIDATE_SUBSYSTEM_STATES = False
pyphi.config.PARALLEL_CONCEPT_EVALUATION = False
pyphi.config.PARALLEL_CUT_EVALUATION = True
pyphi.config.PARALLEL_COMPLEX_EVALUATION = False
pyphi.config.CUT_ONE_APPROXIMATION = True

def save_to_csv(network, state, sia, weights, filename):
    tpm_flat = network.tpm.flatten()
    weights_flat = np.array(weights).flatten()
    is_null_cut = getattr(sia.cut, 'is_null', False)

    data = {
        "num_nodes": [len(network.node_indices)],
        "state": [str(state)],
        "phi": [sia.phi],
        "complex_nodes": [str(sia.subsystem.node_indices)],
        "MIP_from_nodes": [str(sia.cut.from_nodes) if not is_null_cut else "None"],
        "MIP_to_nodes": [str(sia.cut.to_nodes) if not is_null_cut else "None"],
    }

    print(sia.subsystem.node_indices)

    for i, val in enumerate(tpm_flat):
        data[f"tpm_{i}"] = [val]

    for i, val in enumerate(weights_flat):
        data[f"weight_{i}"] = [val]

    df = pd.DataFrame(data)
    print(df)

    file_exists = os.path.isfile(filename)
    df.to_csv(filename, mode='a', index=False, header=not file_exists)


if __name__ == '__main__':

    #model_interpreter = ModelInterpreter('C:/Users/Tim/Desktop/Computer_Vision/Computer-Vision/Version_Results/Model_2/Models/model_epoch5.pth')

    dataset_generator = DatasetGenerator()

    network, state, weights = dataset_generator.generate_network_and_state()
    sys_irreducibility_analysis = pyphi.compute.major_complex(network, state)

    if hasattr(sys_irreducibility_analysis.cut, 'from_nodes') and hasattr(sys_irreducibility_analysis.cut, 'to_nodes'):
        render_controller = RenderController(network, sys_irreducibility_analysis)
        save_to_csv(network, state, sys_irreducibility_analysis, weights, 'Data/phi_dataset.csv')

        for i in range(2000):

            network, state, weights = dataset_generator.generate_network_and_state()
            sys_irreducibility_analysis = pyphi.compute.major_complex(network, state)


            render_controller.render(network, sys_irreducibility_analysis, i)
            save_to_csv(network, state, sys_irreducibility_analysis, weights, 'Data/phi_dataset.csv')

            print('graphs made and Phi computed: ' + str(i))