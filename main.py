import os
import warnings
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

if __name__ == '__main__':
    dataset_generator = DatasetGenerator()
    #model_interpreter = ModelInterpreter('C:/Users/Tim/Desktop/Computer_Vision/Computer-Vision/Version_Results/Model_2/Models/model_epoch5.pth')

    network, state = dataset_generator.generate_network_and_state()
    sys_irreducibility_analysis = pyphi.compute.major_complex(network, state)

    render_controller = RenderController(network, sys_irreducibility_analysis)
