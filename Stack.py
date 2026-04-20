class Node:
    """Класс для представления узла стека"""
    def __init__(self, data, next_node=None):
        """Инициализация узла данными и ссылкой на следующий узел"""
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для реализации структуры данных Стек"""
    def __init__(self, stack_size=5, top=None):
        """Инициализация стека заданным размером"""
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Добавление данных в начало стека"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Удаление и возвращение данных из начала стека"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """проверка, пуст ли стек"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Проверка, заполнен ли стек"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Полная очистка стека"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Получение данных по индексу"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Возвращает тукущее количество элементов в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Подсчет количества целых чисел в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


