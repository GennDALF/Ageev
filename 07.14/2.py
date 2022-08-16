class Builder:
    """Наследуемый строитель"""
    def __init__(self):
        self.name = None
        self.inst_fields = None
        self.tab = None
        self.field_name = None
        self.def_value = None
        self.inst_fields = {}
    
    def __str__(self):
        """Построения кода с отступами"""
        lines = () 
        lines += (f'class {self.name}',)
        self.inst_fields[self.field_name] = self.def_value
        if self.inst_fields:
            lines += (f'{self.tab}def __init__(self):',)
            for name, value in self.inst_fields.items():
                lines += (f'{self.tab*2}{name} = {value}',)
        else:
            lines += (f'{self.tab}pass',)
        return '\n'.join(lines)


class Builder_Builder:
    """Взаимодействует с классами и создаёт екземпляр Builder()"""
    def __init__(self, date = None):
        self.date = Builder()
    def build(self):
        return self.date
    
class Name_value(Builder_Builder):
     """Дочерний класс методы которого передают данные в родительский класс"""
     def name_class(self, name_class_arg: str):
        self.date.name = name_class_arg
        return self
    
class Initiss(Name_value):
    """Дочерний класс методы которого передают данные в родительский класс"""
    def initis(self, field_name: str, def_value: str):
        self.date.field_name = field_name
        self.date.def_value = def_value
        return self
        
class Ttab(Initiss):
    """Дочерний класс методы которого передают данные в родительский класс"""
    def fg(self, indent_length = 4):
        tat = ' ' * indent_length
        self.date.tab = tat
        return self
#Создаём экземпляр класса и вызываем методы с данными для 'генерации кода'         
d = Ttab()\
    .fg()\
    .name_class('fgf')\
    .initis('ff','00')\
    .build()
print(d)


#class fgf
#    def __init__(self):
#        ff = 00
