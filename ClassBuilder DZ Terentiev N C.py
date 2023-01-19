# Задачу со строителем выполнил. Надеюсь понял правильно. Старался.
# В силу задолженностей и того что время поджимает, а мне нужно побыстрее перекрыть домашки, чтобы углубляться в дальнейшие,
# более интересные на мой взгляд темы, я вынужден отправлять по одной задаче. Если буду успевать, то буду делать по две. Я привык углубляться в задачу и экспериментировать.
# В силу экспериментов и несостыковок у меня на одну задачу подобного рода ушло два полных дня. Мне нужно нагнать эти домашки и закрыть долги по предыдущей группе.
# Проблемы мои. Просьба в случае чего, не судить строго с человеческой точки зрения. Оценки же можете ставить соответствующие, как посчитаете нужным.
# Моя цель в первую очередь знания, поэтому и углубляюсь в домашки. Как по мне, лучше углубиться хотябы в одну задачу, чем спешно пробежаться по всем.
# Все задолженности по домашкам я вышлю, пусть и не в полном виде. Оценки меня мало волнуют, главное не кол и выпуститься.

class CreateModelClass:
        # Данный класс отвечается за создание модели класса.

        def __init__ (self, name: str):
                self.Designation = 'class'
                self.name = name
                self.nested = []

        def add_field(self, name: str, value: str = ''): # Принимает на вход имя name и значение value, для поля
                # Метод, позволяет добавить новое поле в класс
                self.final_value = f'{name} = {value}\n'
                self.nested += [self.final_value]

        def __str(self) -> str:
                # Класс создающий итоговое строковое представление
                margin = ' ' * 4
                space = ' '
                result = f'{self.Designation}{space}{self.name}:\n' \
                         f'{margin}def __init__(self):\n'
                if self.nested:
                        for pole in self.nested:
                                result += f'{margin*2}self.{pole}'
                else: result += f'{margin*2}pass'
                return result

        def __str__(self):
                return self.__str()

class classBuilder:
        # Класс строитель
        def __init__(self, name_class:  str): # Принимает на вход имя класса
                self.name_class = name_class
                self.add = CreateModelClass
                self.root = CreateModelClass(name_class)

        def add_field(self, name: str, value: str = '') -> 'classBuilder': # Принимает на вход имя и значение для добавления поля.
                # Класс осуществляет добавление поля внутрь класса. Возвращает classBuilder.
                # В CreateModelClass передаём имя и значение, после чего фиксируем его в переменной класса строителя и возвращаем её с помощью класса строителя.
                self.cls_build = self.add.final_value = f'{name} = {value}\n'
                self.root.nested += [self.cls_build]
                return classBuilder(self.cls_build)

        def __str__(self) -> CreateModelClass:
                return self.root

print(f'Пример выполняет работу класса без строителя \n')

p = CreateModelClass("BUILDER")
p.add_field("Bob", "Bob")
p.add_field("Roma", "Roma")
p.add_field("Ivan", "Ivan")
p.add_field("Dima", "Dima")
print(p.__str__())

print(f'Пример выполняет работу класса по строителю \n')

cb = classBuilder('green')
cb.add_field('Sveta', '35 лет')
cb.add_field('Vova', '20 лет')
cb.add_field('Ivan', '40 лет')
cb.add_field('Timur', 'Не родился')
print(cb.__str__())