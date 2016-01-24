import makeprogress as mp
import unittest


class TestRenderProgressBar(unittest.TestCase):

    def test_render_progress(self):
        self.assertEqual('>---------', mp.render_bar(0, 10))
        self.assertEqual('=====>----', mp.render_bar(5, 10))
        self.assertEqual('==========', mp.render_bar(10, 10))


if __name__ == '__main__':
    unittest.main()
