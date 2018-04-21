'''
    Implementors often use the facade design pattern when a system is very complex or difficult to understand because the system has a large number of interdependent classes 
    or because its source code is unavailable. This pattern hides the complexities of the larger system and provides a simpler interface to the client. 
    It typically involves a single wrapper class that contains a set of members required by the client. 
    These members access the system on behalf of the facade client and hide the implementation details.

    https://en.wikipedia.org/wiki/Facade_pattern

    Component
        Leaf Leaf Composite
                Leaf Leaf Leaf Composite Leaf
                            Leaf Leaf Leaf

'''


class ComponentA:
    def draw(self):
        print('drawA')


class ComponentB:
    def draw(self):
        print('drawB')


class ComponentC:
    def draw(self):
        print('drawC')


class Facade: # entry point to access subclasses, they can't be access by themselves
    comp_a = ComponentA()
    comp_b = ComponentB()
    comp_c = ComponentC()

    def draw(self):
        self.comp_a.draw()
        self.comp_b.draw()
        self.comp_c.draw()


if __name__ == '__main__':
    facade = Facade()
    facade.draw()
