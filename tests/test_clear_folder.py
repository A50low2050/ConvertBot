import unittest
from utils.clear_media import clear_media


class TestClearFolder(unittest.TestCase):

    def test_convert_video_title(self):
        result_func = clear_media()
        self.assertEqual(result_func, 'Clear folder is success ✅')


if __name__ == '__name__':
    unittest.main()
