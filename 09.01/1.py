from random import choice as ran
from typing import Optional
cod = [200, 403, 404, 500]
class Request:
    def __init__(self,request: list):
        self.request = request
        self.request = ran(self.request)
        self.answer = None
    def __str__(self):
        return f'Ответ: {self.request}, описание: {self.answer}'
    
        
class Handler:
    """Класс цепочки, запускает обработку данных."""
    def __init__(self, requwstt: Request):
        self.requwstt = requwstt
        self.previous_modifier: Optional[Handler] = None
        self.next_modifier: Optional[Handler] = None

    def add_modifier(self, handler: 'Handler'):
        if self.next_modifier is None:
            self.next_modifier = handler
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(handler)

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()



class Request_completed_successfully(Handler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    def handle(self):
        if self.requwstt.request == 200:
            self.requwstt.answer = "Запрос выполнен успешно"
        super().handle()
class Refuses_to_authorize_it(Handler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    def handle(self):
        if self.requwstt.request == 403:
            self.requwstt.answer = "Сервер понял запрос,но он отказывается его выполнять из-за ограниченийв доступе для клиента к указанному ресурсу"
        super().handle()
class The_server_cannot_find_the_data(Handler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    def handle(self):
        if self.requwstt.request == 404:
            self.requwstt.answer = "Сервер не найден"
        super().handle()
class The_server_encountered_an_unexpected_error(Handler):
    """Элемент цепочки, проверяет и обрабатывает данные."""
    def handle(self):
        if self.requwstt.request == 500:
            self.requwstt.answer = "Внутренняя ошибка сервера"
        super().handle()
f = Request(cod)
p = Handler(f)
p.add_modifier(Request_completed_successfully(f))
p.add_modifier(Refuses_to_authorize_it(f))
p.add_modifier(The_server_cannot_find_the_data(f))
p.add_modifier(The_server_encountered_an_unexpected_error(f))
p.handle()
print(f)

