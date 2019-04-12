import os
import unittest

import numpy as np

from gnes.indexer import BIndexer


class TestFIndexer(unittest.TestCase):
    def setUp(self):
        self.toy_data = np.array([[1, 2, 1, 2],
                                  [2, 1, 3, 4],
                                  [1, 2, 1, 2],
                                  [2, 1, 4, 3],
                                  [2, 1, 3, 4],
                                  [23, 32, 21, 33],
                                  [123, 132, 1, 1]]).astype(np.uint8)
        self.toy_label = [234, 432, 123, 321, 1, 2, 6]

        self.toy_query = np.array([[1, 2, 1, 2],
                                   [2, 1, 3, 4],
                                   [3, 2, 1, 2]]).astype(np.uint8)

        self.toy_exp = [[(234, 0), (123, 0)], [(432, 0), (1, 0)], [(234, 1), (123, 1)]]

        dirname = os.path.dirname(__file__)
        self.dump_path = os.path.join(dirname, 'indexer.bin')

    def tearDown(self):
        if os.path.exists(self.dump_path):
            os.remove(self.dump_path)

    def test_nsw_search(self):
        fd = BIndexer(self.toy_data.shape[1])
        fd.add(self.toy_label, self.toy_data.tobytes())
        rs = fd.query(self.toy_query.tobytes(), 2, method='nsw')
        for i in range(len(rs)):
            rs[i] = sorted(rs[i], key=lambda x:(x[1], -x[0]))
        self.assertEqual(rs, self.toy_exp)

    def test_force_search(self):
        fd = BIndexer(self.toy_data.shape[1])
        fd.add(self.toy_label, self.toy_data.tobytes())
        rs = fd.query(self.toy_query.tobytes(), 2, method='force')
        for i in range(len(rs)):
            rs[i] = sorted(rs[i], key=lambda x:(x[1], -x[0]))
        self.assertEqual(rs, self.toy_exp)

    def test_dump_load(self):
        fd = BIndexer(self.toy_data.shape[1], data_path='./BIndexer.bin')
        fd.add(self.toy_label, self.toy_data.tobytes())
        fd.dump(self.dump_path)

        fd2 = BIndexer.load(self.dump_path)
        rs = fd2.query(self.toy_query.tobytes(), 2)
        for i in range(len(rs)):
            rs[i] = sorted(rs[i], key=lambda x:(x[1], -x[0]))
        self.assertEqual(rs, self.toy_exp)