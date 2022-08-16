## ==========  1  ========== ##

## это не класс строитель (builder), а тот класс, который мы конструируем с помощью строителя
class Builder:
    """Комбинированный строитель"""
    def __init__(self):
        ## следует обдумать типы значений по умолчанию
        self.name = None
        self.inst_fields = None
        self.tab = None
        ## зачем эти поля?
        self.field_name = None
        self.def_value = None
        ## зачем переприсваивание?
        self.inst_fields = {}

    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __str__(self):
        """Построения кода с отступами"""
        lines = ()
        ## в конце заголовка класса должно быть двоеточие
        lines += (f'class {self.name}',)
        ## здесь вы формируете словарь из одного атрибута
        ## и формирование словаря inst_fields должно происходить никак не здесь, а как раз в строителе
        self.inst_fields[self.field_name] = self.def_value
        if self.inst_fields:
            lines += (f'{self.tab}def __init__(self):', )
            for name, value in self.inst_fields.items():
                lines += (f'{self.tab*2}{name} = {value}', )
        else:
            lines += (f'{self.tab}pass', )
        return '\n'.join(lines)


## а вот это класс строитель
class Hub:
    """Взаимодействует с классами и создаёт екземпляр Builder()"""
    ## лучше так:
    """Управляющий строителя для конструирования объектов класса Builder()"""
    ## может быть data (данные), а не date (календарная дата)?
    def __init__(self, date = None):
        if date is None:
            self.date = Builder()
        else:
            self.date = date

    ## свойства должны быть документированы и аннотированы (помимо self)
    @property
    def vvalue(self):
        return Name_value(self.date)
    
    ## свойства должны быть документированы и аннотированы (помимо self)
    @property
    def ttabb(self):
        return Ttab(self.date)
    
    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def build(self):
        return self.date


class Name_value(Hub):
    ## а какие данные передаются?
    """Дочерний класс методы которого передают данные в родительский класс"""
    ## лучше так
    """Подчинённый строителя для инициализации атрибутов имени и полей объектов класса Builder()"""
    def __init__(self, date: str):
        super().__init__(date)

    ## обычные методы должны быть документированы (помимо self) 
    def name_class(self, name_class_arg: str):
        self.date.name = name_class_arg
        return self

    ## обычные методы должны быть документированы (помимо self) 
    def initis(self, field_name: str, def_value: str):
        self.date.field_name = field_name
        self.date.def_value = def_value
        return self


class Ttab(Hub):
    ## а какие данные передаются?
    """Дочерний класс методы которого передают данные в родительский класс"""
    ## лучше так
    """Подчинённый строителя для инициализации атрибутов имени и полей объектов класса Builder()"""

    ## магические методы не документируются (потому что их назначение определено), но их параметры (когда они есть помимо self) подлежат аннотации
    def __init__(self, date):
        super().__init__(date)

    ## обычные методы должны быть документированы и аннотированы (помимо self) 
    def fg(self, indent_length = 4):
        tat = ' ' * indent_length
        self.date.tab = tat
        return self


# создаём экземпляр класса и вызываем методы с данными для 'генерации кода'        
d = Hub()\
    .vvalue\
        .name_class('Fgf')\
        .initis('ff', '00')\
    .ttabb\
        .fg()\
    .build()
print(d)

#class fgf
#    def __init__(self):
#        ff = 00

## проверьте генерацию пустого объекта:
## print(d2)

## и проверьте генерацию объекта с несколькими полями:
## d3 = Hub().vvalue.name_class('Test_2').initis('first_attr', '1').initis('sec_attr', '2').ttabb.fg().build()
## print(d3)



## ==========  2  ========== ##

## всё то же самое, что и в предыдущей задаче
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
            lines += (f'{self.tab}def __init__(self):', )
            for name, value in self.inst_fields.items():
                lines += (f'{self.tab*2}{name} = {value}', )
        else:
            lines += (f'{self.tab}pass', )
        return '\n'.join(lines)


class Builder_Builder:
    """Взаимодействует с классами и создаёт екземпляр Builder()"""
    def __init__(self, date = None):
        self.date = Builder()
    def build(self):
        return self.date
    
    
class Name_value(Builder_Builder):
    ## такая строка документации никак не позволяет отличить один класс от другого
    """Дочерний класс методы которого передают данные в родительский класс"""
    def name_class(self, name_class_arg: str):
        self.date.name = name_class_arg
        return self


class Initiss(Name_value):
    ## такая строка документации никак не позволяет отличить один класс от другого
    """Дочерний класс методы которого передают данные в родительский класс"""
    def initis(self, field_name: str, def_value: str):
        self.date.field_name = field_name
        self.date.def_value = def_value
        return self


class Ttab(Initiss):
    ## такая строка документации никак не позволяет отличить один класс от другого
    """Дочерний класс методы которого передают данные в родительский класс"""
    def fg(self, indent_length = 4):
        tat = ' ' * indent_length
        self.date.tab = tat
        return self


# создаём экземпляр класса и вызываем методы с данными для 'генерации кода'         
d = Ttab()\
    .fg()\
    .name_class('fgf')\
    .initis('ff', '00')\
    .build()
print(d)

#class fgf
#    def __init__(self):
#        ff = 00

## проверьте генерацию пустого объекта:
## d2 = Ttab().build()
## print(d2)

## и проверьте генерацию объекта с несколькими полями:
## d3 = Ttab().fg().name_class('Test_2').initis('first_attr', 1).initis('sec_attr', 2).build()
## print(d3)
