class Variable:
    var = "CLASS"

    def change_on_instance(self):
        self.var = "Instance"

    @classmethod
    def change_on_class(cls):
        cls.var = "Class"


print(Variable.var) # "CLASS"
print(Variable().var) # "CLASS"

Variable.change_on_class()
print(Variable.var) # "Class"
print(Variable().var) # "Class"

variable = Variable()
variable.change_on_instance()
print(variable.var) # "Instance"
print(Variable.var) # "Class"
