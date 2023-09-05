import unittest
from unittest.mock import patch, MagicMock
from connection import app, ser

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_connection(self):
        self.assertTrue(ser.isOpen())

    @patch('your_flask_app.ser.read')
    @patch('your_flask_app.ser.write')
    def test_get_data(self, mock_write, mock_read):
        mock_read.return_value = b'test_data'
        response = self.app.post('/send_command', data={'command': 'get_data'})
        mock_write.assert_called_with(b'get_data\r\n')
        self.assertEqual(response.data, b'test_data')

    @patch('your_flask_app.requests.post')
    @patch('your_flask_app.ser.read')
    @patch('your_flask_app.ser.write')
    def test_send_data(self, mock_write, mock_read, mock_post):
        mock_read.return_value = b'test_data'
        self.app.post('/send_command', data={'command': 'send_data'})
        mock_write.assert_called_with(b'send_data\r\n')
        mock_post.assert_called_with('https://yourserver.com/data', data=b'test_data')

    def test_web_interface(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Send Command', response.data)

if __name__ == '__main__':
    unittest.main()
