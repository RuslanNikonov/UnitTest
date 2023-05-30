import unittest
from main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
# тест: главная страница возвращает код ответа 200
    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
# тест: отправляет POST-запрос с данными формы и проверяет, что на странице отображается правильный результат.
    def test_form_post(self):
        response = self.app.post('/', data=dict(name1=1000, name2=10, name3=1), follow_redirects=True)
        self.assertIn(b'1100', response.data)  # Проверяем, что на странице отображается ожидаемое значение


if __name__ == '__main__':
    unittest.main()
