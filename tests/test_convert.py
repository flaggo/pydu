import pytest
from pydu.convert import boolean


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