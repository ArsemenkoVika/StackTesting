import unittest
from Stack import Node, Stack

class TestStack(unittest.TestCase):
    """Класс для тестирования функционала Стека."""

    def setUp(self):
        """Создаем чистый стек"""
        self.stack = Stack(stack_size=3)

    def test_node_creation(self):
        """Тест создания узла."""
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next_node)

    def test_push_and_size(self):
        """Проверяем добавление и размер"""
        self.stack.push("test")
        self.assertEqual(self.stack.size_stack(), 1)
        self.assertEqual(self.stack.top.data, "test")

    def test_pop(self):
        """Проверяем удаление"""
        self.stack.push(10)
        data = self.stack.pop()
        self.assertEqual(data, 10)
        self.assertTrue(self.stack.is_empty())

    def test_pop_empty(self):
        """Тест удаления из пустого стека"""
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_push_overflow(self):
        """Тест переполнения"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        result = self.stack.push(4)
        self.assertEqual(result, "Стэк переполнен")


    def test_counter_int(self):
        """Тест подсчета целых чисел """
        self.stack.push(1)  # int
        self.stack.push("sta")  # str
        self.stack.push(2)  # int
        self.stack.push(2.5)  # float
        self.assertEqual(self.stack.counter_int(), 2)

if __name__ == '__main__':
    unittest.main()