# Fiquei confuso como a gente lida com o torque/momento, já que não é uma forca e a orientacao fica estranha

class Beam():

    def __init__(self, pos, length) -> None:
        self.length = length
        self.pos = pos

        self.supports = []
        self.forces = []

    def make_support(self, support_pos, sup_type):
        new_support = Support(support_pos, sup_type, self)
        self.supports.append(new_support)

    def make_force(self, force_pos, orientation, magnitude):
        new_force = Force(force_pos, orientation, magnitude)
        self.forces.append(new_force)

# Adicionar classes para apoios e esforcos. 

class Support():

    def __init__(self, pos, sup_type, beam) -> None:
        self.pos = pos

        self.type = sup_type
        self.beam = beam

        # Mais atributos a serem definidos pelo tipo?

        self.set_type()

    def set_type(self):
        if self.type == '':
            pass
        elif self.type == '':
            pass
        elif self.type == '':
            pass
    # Definir os tipos de apoios e determinar atributos

class Force:
    
    def __init__(self, pos, orientation, magnitude) -> None:
        self.pos = pos
        self.orient = orientation
        self.mag = magnitude

        #self.type = type ??? Caso seja forca ou torque
    #def set_type(self):
    #   if self.type == 'force ou f ou F':
    #       pass
    #   elif self.type == 'torque ou t ou T':
    #       pass