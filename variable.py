class Variable:
    value = "CLASS"

    def change_on_instance(self):
        self.value = "Instance"

    @classmethod
    def change_on_class(cls):
        cls.value = "Class"


print(Variable.value) # "CLASS"
print(Variable().value) # "CLASS"

Variable.change_on_class()
print(Variable.value) # "Class"
print(Variable().value) # "Class"

variable = Variable()
variable.change_on_instance()
print(variable.value) # "Instance"
print(Variable.value) # "Class"
