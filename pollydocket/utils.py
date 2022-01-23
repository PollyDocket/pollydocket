"""Various useful utilities."""
from itertools import islice, tee
from typing import Iterable, Iterator


def pairwise(iterable: Iterable) -> Iterator:
    """Return pairwise iterator (sliding window).

    Args:
        iterable: Iterable to create pairwise iterator from

    Returns:
        Iterator: Pairwise iterator over the input iterable

    e.g. s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    return zip(a, islice(b, 1, None))
