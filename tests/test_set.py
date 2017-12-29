from pydu.set import OrderedSet


def test_ordered_set():
    ordered_set = OrderedSet([1, 3, 1, 2])
    assert list(ordered_set) == [1, 3, 2]
    assert 1 in ordered_set
    assert bool(ordered_set)

    ordered_set.add(1)
    assert 1 in ordered_set

    ordered_set.remove(1)
    assert 1 not in ordered_set

    for i in range(4):
        ordered_set.discard(i)
    assert not bool(ordered_set)
