import pytest
from pydu.convert import (boolean,
                          bin2oct, bin2dec, bin2hex,
                          oct2bin, oct2dec, oct2hex,
                          dec2bin, dec2oct, dec2hex,
                          hex2bin, hex2oct, hex2dec)


BIG_NUM_STR = '10'*50
BIG_NUM = 10**50


class TestBoolean:
    def test_accepted_text(self):
        for text in ('yes', 'y', 'on', 'true', 't', '1'):
            assert boolean(text)
            assert boolean(text.upper())

        for text in ('no', 'n', 'off', 'false', 'f', '0'):
            assert not boolean(text)
            assert not boolean(text.upper())

    @pytest.mark.parametrize('text', ('a', 'b'))
    def test_unaccepted_text(self, text):
        with pytest.raises(ValueError):
            boolean(text)

    def test_nonstring(self):
        for obj in (10, [1], {1: 1}):
            assert boolean(obj)

        for obj in (0, [], {}):
            assert not boolean(obj)


def test_bin2oct():
    assert bin2oct('1001') == '11'
    assert 'L' not in bin2oct(BIG_NUM_STR)


def test_bin2dec():
    assert bin2dec('11') == 3


def test_bin2hex():
    assert bin2hex('11010') == '1a'
    assert 'L' not in bin2hex(BIG_NUM_STR)


def test_oct2bin():
    assert oct2bin('11') == '1001'
    assert 'L' not in oct2bin(BIG_NUM_STR)


def test_oct2dec():
    assert oct2dec('11') == 9


def test_oct2hex():
    assert oct2hex('32') == '1a'
    assert 'L' not in oct2hex(BIG_NUM_STR)


def test_dec2bin():
    assert dec2bin(3) == '11'
    assert 'L' not in dec2bin(BIG_NUM)


def test_dec2oct():
    assert dec2oct(9) == '11'
    assert 'L' not in dec2oct(BIG_NUM)


def test_dec2hex():
    assert dec2hex(26) == '1a'
    assert 'L' not in dec2hex(BIG_NUM)


def test_hex2bin():
    assert hex2bin('1a') == '11010'
    assert 'L' not in hex2bin(BIG_NUM_STR)


def test_hex2oct():
    assert hex2oct('1a') == '32'
    assert 'L' not in hex2oct(BIG_NUM_STR)


def test_hex2dec():
    assert hex2dec('1a') == 26
