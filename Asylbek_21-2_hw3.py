import random


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return (self.cpu + self.memory) / 2

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __str__(self):
        return f'Cpu: {self.cpu} Memory: {self.memory}'


class Phone:
    def __init__(self, sim_card_list: list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value: list):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        print(
            f'Идет звонок с номера "{call_to_number}" с сим карты №{sim_card_number}-'
            f'{self.__sim_card_list[sim_card_number]}')

    def __str__(self):
        return f'Sim-Card list: {self.__sim_card_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    @staticmethod
    def use_gps(location):
        print(f'Построен маршрут до {location}: {random.randint(3, 10)}km')

    def __str__(self):
        return Computer.__str__(self) + ' ' + Phone.__str__(self)


# Computer objects
# Сpu измеряется в модели процессора а Memory в гигабайтах
asus = Computer(10080, 980)
# Phone objects
nokia = Phone(['Beeline'])
# SmartPhone objects
poko = SmartPhone(9800, 512, ['MegaCom', 'O! NurTelecom'])
iphone = SmartPhone(12000, 256, ['Starlink'])

print(asus)
print(nokia)
print(poko)
print(iphone)

print('Make Computation:', asus.make_computations())
poko.call(0, '+996708869616')

iphone.use_gps('БЦ Victory')

print('Сравнение:')
print(asus > poko)
print(iphone < poko)
print(asus >= iphone)
print(poko <= asus)
print(poko == asus)
print(asus != iphone)
