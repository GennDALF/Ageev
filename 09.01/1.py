# ИСПОЛЬЗОВАТЬ: лучше без псевдонима, чем с плохим псевдонимом
from random import choice
from typing import Optional

codes = [200, 403, 404, 500]


# ДОБАВИТЬ: документацию класса
class Request:
    def __init__(self, requests: list):
        self.code = requests
        self.code = choice(self.code)
        self.answer = None

    def __str__(self):
        return f'Ответ: {self.code}, описание: {self.answer}'
    
        
class CodesHandler:
    """Класс цепочки, запускает обработку данных."""
    def __init__(self, request: Request):
        self.request = request
        self.previous_modifier: Optional[CodesHandler] = None
        self.next_modifier: Optional[CodesHandler] = None

    # ДОБАВИТЬ: документацию метода
    def add_modifier(self, handler: 'CodesHandler'):
        if self.next_modifier is None:
            self.next_modifier = handler
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(handler)

    # ДОБАВИТЬ: документацию метода
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


# ИСПОЛЬЗОВАТЬ: для имён классов используется регистр CamelCase — слова пишутся слитно, каждое с большой буквы
class Code200(CodesHandler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    # ДОБАВИТЬ: документацию метода
    def handle(self):
        if self.request.code == 200:
            self.request.answer = "Запрос выполнен успешно"
        # ИСПРАВИТЬ: а если код ответа на запрос обработан этим классом, то надо ли продолжать обработку?
        super().handle()


# ИСПОЛЬЗОВАТЬ: слишком длинные имена классов очень неудобны
class Code403(CodesHandler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    # ДОБАВИТЬ: документацию метода
    def handle(self):
        if self.request.code == 403:
            self.request.answer = "Сервер понял запрос, но он отказывается его выполнять из-за ограничений доступа для клиента к указанному ресурсу"
        super().handle()


class Code404(CodesHandler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    # ДОБАВИТЬ: документацию метода
    def handle(self):
        if self.request.code == 404:
            self.request.answer = "Сервер не найден"
        super().handle()


class Code500(CodesHandler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    # ДОБАВИТЬ: документацию метода
    def handle(self):
        if self.request.code == 500:
            self.request.answer = "Внутренняя ошибка сервера"
        super().handle()


# КОММЕНТАРИЙ: прописывание документации и комментариев очень помогает систематизировать своё понимание кода, что особенно полезно во время обучения


f = Request(codes)
p = CodesHandler(f)
p.add_modifier(Code200(f))
p.add_modifier(Code403(f))
p.add_modifier(Code404(f))
p.add_modifier(Code500(f))
p.handle()
print(f)


# ИТОГ: очень хорошо — 10/12
