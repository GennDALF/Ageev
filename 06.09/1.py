import math
class Tetra:
    """Класс для вычисления  площади поверхности и объёма тетраидра"""
    def __init__(self, side):
        self.side =  side

    
        
    
    def square_tetr(self):
        """Метод вычисляющий площадь"""
        s = math.sqrt(3 * (int(self.side) * int(self.side)))
        
        print(s)

    def volume_tetr(self):
        """Метод вычисляющий обЪём"""
        v = (1/12) * (int(self.side) ** 3) * math.sqrt(2)
        print(v)

#Экземпляр класса        
d = Tetra(4) 
d.square_tetr()
d.volume_tetr()


# 6.928203230275509
# 7.542472332656507
