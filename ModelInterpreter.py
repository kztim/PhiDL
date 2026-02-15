import torch

class ModelInterpreter:

    def __init__(self, file_location):
            self.file_location = file_location

            self.model = torch.load(self.file_location, map_location=torch.device('cpu'))

            for layer_name, tensor in self.model.items():
                print(f"Layer: {layer_name} | Shape: {tensor.size()}")

            print(self.model['backbone.body.conv1.weight'])