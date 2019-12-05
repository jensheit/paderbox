import unittest

import numpy as np

from paderbox.io.audioread import audioread
# from scipy import signal

import paderbox.testing as tc
import paderbox.transform as transform
# from pymatbridge import Matlab

from paderbox.io.data_dir import testing as testing_dir


class TestSTFTMethods(unittest.TestCase):

    def test_fbank(self):
        path = testing_dir / 'timit' / 'data' / 'sample_1.wav'
        y = audioread(path)[0]
        feature = transform.fbank(y)

        tc.assert_equal(feature.shape, (291, 23))
        tc.assert_isreal(feature)
        tc.assert_array_greater_equal(feature, 0)

    def test_hz2mel(self):
        tc.assert_equal(transform.module_fbank.hz2mel(6300), 2595)
        tc.assert_equal(transform.module_fbank.hz2mel(
            np.array([6300, 6300, 6300])), 2595)

    def test_mel2hz(self):
        tc.assert_equal(transform.module_fbank.mel2hz(2595), 6300)
        tc.assert_equal(transform.module_fbank.mel2hz(
            np.array([2595, 2595, 2595])), 6300)

    def test_mel2hzandhz2mel(self):
        rand = np.random.rand(5, 5) * 1000
        tc.assert_almost_equal(
            rand, transform.module_fbank.mel2hz(
                transform.module_fbank.hz2mel(rand)))
        tc.assert_almost_equal(rand, transform.module_fbank.hz2mel(transform.module_fbank.mel2hz(rand)))
