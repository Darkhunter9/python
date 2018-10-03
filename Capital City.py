class Singleton(object):
    def __new__(cls, city_name):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

class Capital(Singleton):
    Name = ""
    
    def __init__(self,city_name):
        if not Capital.Name:
            Capital.Name = city_name

    def name(self):
            return Capital.Name

'''
Alternative
class Capital(object):
    Name = ""

    def __new__(cls, city_name):
        if not hasattr(cls, '_instance'):
            Capital.Name = city_name
            orig = super(Capital, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

    def name(self):
            return Capital.Name
'''


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")