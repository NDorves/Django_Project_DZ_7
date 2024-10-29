import os
from django.test import TestCase
import unittest
import json
from unittest.mock import patch


def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except TypeError as err:
        raise err
    except IOError as err:
        raise err


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err


test_data = {
    "pk": 4,
    "title": "Test Author",
    "published_date": "2024-06-23",
    "publisher": 6,
    "price": 9.99,
    "discounter_price": 3.56,
    "is_bestseller": True,
    "is_banned": False,
    "genres": [1,]
}
#Задание 1. Тестирование функционала по работе с JSON файлом
# Необходимо протестировать этот функционал, чтобы убедиться, что он работает так, как ожидается.
# Создайте класс TestFileOperations с методами тестирования:


class TestFileOperations(unittest.TestCase):

    def setUp(self):    #Метод для подготовки тестовых данных и создания тестового файла перед каждым тестом.
        self.file_name = 'test_file_json'
        self.empty_file_name = 'empty_file.json'
        self.bad_data = {"pk": set([1, 2, 3])}      # Некорректные данные для теста

    def tearDown(self): #Метод для удаления тестового файла после каждого теста
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        if os.path.exists(self.empty_file_name):
            os.remove(self.empty_file_name)

    # Проверка записи и чтения корректных данных.После чтения проверьте, что все поля соответствуют ожидаемым
    # типам данных, которые были прописаны в значениях словаря test_data
    def test_write_and_read_file(self):
        write_to_file(self.file_name, test_data)
        result = read_from_file(self.file_name)
        self.assertEqual(result, test_data)
        self.assertIsInstance(result['pk'], int)
        self.assertIsInstance(result['title'], str)
        self.assertIsInstance(result['published_date'], str)
        self.assertIsInstance(result['publisher'], int)
        self.assertIsInstance(result['price'], float)
        self.assertIsInstance(result['discounter_price'], float)
        self.assertIsInstance(result['is_bestseller'], bool)
        self.assertIsInstance(result['is_banned'], bool)
        self.assertIsInstance(result['genres'], list)

    def test_write_and_read_empty_file(self):       # Проверка записи и чтения пустого словаря.
        write_to_file(self.empty_file_name, {})
        result = read_from_file(self.empty_file_name)
        self.assertEqual(result, {})

    def test_read_nonexistent_file(self):  #Проверка чтения из несуществ-го файла (должно быть FileNotFoundError).
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file_json')

    def test_write_bad_data_into_file(self):    #Проверка записи некорректных данных (должно выбрасывать TypeError).
        with self.assertRaises(TypeError):
            write_to_file(self.file_name,self.bad_data)


if __name__ == '__main__':
    unittest.main()

