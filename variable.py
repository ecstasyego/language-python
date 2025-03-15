class Variable:
    cls_variable = "CLASS"

    def change_on_instance(self):
        self.cls_variable = "Instance"

    @classmethod
    def change_on_class(cls):
        cls.cls_variable = "Class"


print(Variable.cls_variable) # "CLASS"
print(Variable().cls_variable) # "CLASS"

Variable.change_on_class()
print(Variable.cls_variable) # "Class"
print(Variable().cls_variable) # "Class"

variable = Variable()
variable.change_on_instance()
print(variable.cls_variable) # "Instance"
print(Variable.cls_variable) # "Class"
