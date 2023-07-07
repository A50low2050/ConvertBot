import unittest
from utils.handler_title import convert_video_title


class TestConvertVideoTitle(unittest.TestCase):

    def test_convert_video_title(self):
        result_func = convert_video_title('video.mp4')
        self.assertEqual(result_func, 'video.mp3')


if __name__ == '__name__':
    unittest.main()
