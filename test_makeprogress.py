import makeprogress as mp
import unittest


class TestRenderProgressBar(unittest.TestCase):

    def test_basic_progress_bar_render(self):
        self.assertEqual('>---------', mp.render_bar(0, 10))
        self.assertEqual('=====>----', mp.render_bar(5, 10))
        self.assertEqual('==========', mp.render_bar(10, 10))
        self.assertEqual('==========', mp.render_bar(20, 10))

    def test_one_cell_progress_bar(self):
        self.assertEqual('>', mp.render_bar(0, 1))
        self.assertEqual('=', mp.render_bar(1, 1))
        self.assertEqual('=', mp.render_bar(10, 1))

    def test_zero_cell_progress_bar(self):
        self.assertEqual('', mp.render_bar(0, 0))
        self.assertEqual('', mp.render_bar(1, 0))

if __name__ == '__main__':
    unittest.main()
