# Регистр сдвига с линейной обратной связью
class LFSR:
    def __init__(self, input_values, steps=1):
        """
        Инициализация регистра
        @param input_values: введенные значения
        @param steps: кол-во шагов итерации
        """
        self.input_values = input_values
        self.steps = steps

    def start(self):
        """
        Запускает регистр
        """
        total_value = []  # Хранит сгенерированное значение
        print("Исходное значение: {0}".format(''.join(self.input_values)))  # Печатает введенные данные
        for i in range(self.steps):  # Пробегает столько шагов, сколько мы ввели
            last_value = self.input_values[len(self.input_values) - 1]  # Запоминает последнее (вытолкнутое) значение
            total_value += last_value  # Записываем вытолкнутое значение в итоговый вариант
            count_of_one = 0  # Считает кол-во единиц
            for index, value in reversed(list(enumerate(self.input_values))):  # Проходит по всем значениям в обратном порядке
                if value == '1':  # Если значение 1, то счетчик запоминает
                    count_of_one += 1  # Увеличивает значение кол-ва единиц
                # Начинаем передвигать значения вправо начиная с предпослденего элемента.
                # Иначе будет ошибка
                if index != len(self.input_values) - 1:
                    self.input_values[index + 1] = value  # Передвигает элемент вправо
            if count_of_one % 2 == 0:  # Если кол-во единиц четное, то
                self.input_values[0] = '0'  # в начало списка добавляем 0
            else:  # иначе
                self.input_values[0] = '1'  # в начало списка добавляем 1
            values_srt = ''.join(self.input_values)  # Делаем из списка строку
            print("{0}_{1}".format(values_srt, last_value))  # Печатаем 
        print("Сгенерированное значение: {0}".format(''.join(total_value)))


input_data = input("Введите данные (например 10100101): ")
input_step = int(input("Введите кол-во шагов: "))

input_data_list = list(input_data.replace(" ", ""))

lfsr_register = LFSR(input_data_list, input_step)
lfsr_register.start()
