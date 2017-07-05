"""
Example of an iterator. Note that Python provides an automatic iterator implementation
for any class that defines both  __len__ and __getitem__ methods.
"""

class Range:
    """A class that mimics Python's built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """
        Initializes a Range instance.

        start -> starting #
        stop  -> # to stop at
        step  -> skip distance
        """
        if (step == 0):
            raise ValueError('step cannot be zero.')

        if stop is None:    # treated as range(0, n)
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)    # formula for number of elements in range
        self._start = start
        self._step = step

    def __len__(self):
        """Returns number of elements in the range."""
        return self._length

    def __getitem__(self, k):
        """Returns entry at index k."""
        if k < 0:
            k += len(self)  # same as len(self) - k
        if not 0 <= k < self._length:
            raise IndexError('index is out of range.')

        return self._start + (k * self._step)

