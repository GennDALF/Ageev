"""Фабрика"""

class FilmCard:
    class FilmCardFactory:
        def __init__(self):
            self.id = 1
        
        def create_person(self, name):
            p = FilmCard(self.id, name)
            self.id += 1
            return p

    factory = FilmCardFactory()
    def __init__(self, id, name):
        ## то есть, вы считаете, что идентификатора и имени фильма достаточно в онлайн-кинотеатре? я вроде предлагал около десяти атрибутов - но вы, очевидно, не поняли, что такое атрибут
        self.id = id
        self.name = name
        ## self.release_date: datetime.date = 
        ## self.countries: list[str] = 
        ## self.director: str = 
        ## self.writer: str = 
        ## self.cast: list[str] = 
        ## self.runtime: datetime.timedelta = 
        ## self.genres: list[str] = 
        ## self.synopsis: str = 
    
    def __repr__(self):
        return f"<Фильм {self.id}: {self.name}>"


pers1 = FilmCard.factory.create_person('Тор: Любовь и гром')
pers2 = FilmCard.factory.create_person('Миньоны: Грювитация')
pers3 = FilmCard.factory.create_person('Топ Ган: Мэверик')
pers4 = FilmCard.factory.create_person('Элвис')
pers5 = FilmCard.factory.create_person('Пес-самурай и город кошек')
pers6 = FilmCard.factory.create_person('Чёрный телефон')
pers7 = FilmCard.factory.create_person('Мир Юрского периода: Госпотство')
pers8 = FilmCard.factory.create_person('Миссис Харрис едет в Париж')
pers9 = FilmCard.factory.create_person('Базз Лайтер')
pers10 = FilmCard.factory.create_person('Марсель, ракушка в ботинках')
print(pers1, pers2, pers3,pers4,pers5,pers6,pers7,pers8,pers9,pers10, sep='\n')

## films = [obj for name, obj in globals().items() if name.startswith('pers')]
## print(*films, sep='\n\n')
