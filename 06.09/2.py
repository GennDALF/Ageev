import datetime
class Time_belt:
    """Класс который принимает в качестве аргумента
        часовой пояс в котором необходимо узнать период суток"""
    def __init__(self,hourr):
        self.hourr = hourr
        
            
    

    def check_belt(self):
        """Метод класса вовращающий период суток"""
        time_now = datetime.datetime.now()
        hour_now = time_now.hour
        if int(self.hourr) > 12 or int(self.hourr) < -12:
            False
        else:
            s = int(hour_now) - int(self.hourr)
        
            if s < 0:
                s = 24 - -s
            elif s > 24:
                s = s - 24
        
            if 6 <= s <= 11:
                return "В это часовом поясе сейчас - утро"
        
            elif 12 <= s <= 17:
                 return "В это часовом поясе сейчас - день"
            elif 18 <= s <= 24:
                 return "В это часовом поясе сейчас - вечер"
            elif s <= 5:
                 return "В это часовом поясе сейчас - ночь"
       
        
        


#Создание экземпляра класса
y = input("Напишите ваш часовой пояс относительно Лондона(Напр. '+2', '-2'): ")
z = Time_belt(y)
m = z.check_belt()
print(m)


# Напишите ваш часовой пояс относительно Лондона(Напр. '+2', '-2'): 5
# В это часовом поясе сейчас - вечер
