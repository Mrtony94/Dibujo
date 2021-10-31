class Canvas:
    def __init__(self):
        self.shapes = {}

    def add_shape(self, shape):
        self.shapes[shape.id] = shape

    def remove_shape(self, id):
        return self.shapes.pop(id, None)

    def print_shapes(self):
        # for k, v in self.shapes.items():
        # for k in self.shapes.keys():
        for v in self.shapes.values():
            print(v)
