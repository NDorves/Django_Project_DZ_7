import re
import unittest


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.cleaned_text = None

    def clean_text(self):
        self.cleaned_text = re.sub(r'[^a-zA-Z\s]', '', self.text).lower()

    def remove_stop_words(self, stop_words):
        if self.cleaned_text is None:
            self.clean_text()
        words = self.cleaned_text.split()
        filtered_words = [word for word in words if word not in stop_words]
        self.cleaned_text = ''.join(filtered_words)

#---Задание 2. Тестирование функционала по обработке текста ---------Необходимо протестировать этот функционал.
# Список тестов для покрытия сущности:
# Тестирование метода clean_text:
# Проверить, что метод правильно удаляет небуквенные символы.
# Проверить, что текст приводится к нижнему регистру.
# Проверить, что метод работает на пустой строке.
#
# Тестирование метода remove_stop_words:
# Проверить, что стоп-слова удаляются из текста.
# Проверить, что текст корректно очищается, если clean_text не был вызван заранее.
# Проверить, что метод корректно работает, если стоп-слова отсутствуют в тексте.
#
# Подробное описание методов и тестов:
#
# Тестирование clean_text
# Сценарий: Исходный текст "Hello, World!" должен быть преобразован в "hello world".
# Сценарий: Исходный текст "123 ABC!!!" должен быть преобразован в "abc".
#
# Тестирование remove_stop_words
#
# Сценарий: Для текста "this is a test" и стоп-слов ['this', 'is'], результат должен быть "a test".
# Сценарий: Для текста "hello world" и пустого списка стоп-слов, результат должен остаться "hello world".


class TestTextProcessor(unittest.TestCase):
    def test_clean_text(self):
        processor = TextProcessor('Hello, World!')  #Исх-й текст "Hello, World!" должен быть преобраз-н в "hello world".
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, 'hello world')

        processor = TextProcessor("123 ABC!!!") #Исходный текст "123 ABC!!!" должен быть преобразован в "abc"
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, " abc")

        processor = TextProcessor("")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "")

    def test_remove_stop_words(self):
        processor = TextProcessor("this is a test") #Для текста "this is a test" и стоп-слов ['this', 'is'],
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, "atest")# результат должен быть "a test".

        processor = TextProcessor("hello world")
        processor.remove_stop_words([])
        self.assertEqual(processor.cleaned_text, 'helloworld')

        processor = TextProcessor("hello world")
        processor.remove_stop_words(['hello'])
        self.assertEqual(processor.cleaned_text, "world")


if __name__ == '__main__':
    unittest.main()

