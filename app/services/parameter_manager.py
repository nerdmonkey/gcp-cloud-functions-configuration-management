

class ParameterManager:
    def __init__(self, parameters):
        self.parameters = parameters

    def get_parameter(self, key, default=None):
        return self.parameters.get(key, default)

    def set_parameter(self, key, value):
        self.parameters[key] = value

    def remove_parameter(self, key):
        if key in self.parameters:
            del self.parameters[key]

    def list_parameters(self):
        return self.parameters.keys()
