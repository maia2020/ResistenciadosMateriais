# Fiquei confuso como a gente lida com o torque/momento, já que não é uma forca e a orientacao fica estranha

class Beam():

    def __init__(self, length, pos) -> None:
        self.length = length
        self.pos = pos

        self.supports = []
        self.forces = []

    def make_support(self, support_pos, type):
        new_support = Support(support_pos, type, self)
        self.supports.append(new_support)

    def make_force(self, force_pos, orientation, magnitude):
        new_force = Force(force_pos, orientation, magnitude)
        self.forces.append(new_force)

# Adicionar classes para apoios e esforcos. 