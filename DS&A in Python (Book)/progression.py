"""
Example of Inheritance.
"""

class Progression:
    """
    Iterator producing a generic progression.
    Yields a sequence of positive integers by default (0, 1, 2, ...).
    """

    def __init__(self, start=0):
        """Initialize current to the first number of the progression."""
        self._current = start

    def _advance(self):
        """
        Updates self._current to a new value, if _current == None,
        this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """
        Returns the current element if possible 
        and advances the progression.
        """
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        """Prints the next n values of the progression."""
        print(' '.join(str(next(self)) for i in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, start=0, increment=1):
        """
        Creates a new arithmetic progression.

        start     -> first term of the progression
        increment -> fixed constant added to each term
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Updates current value by adding increment."""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, start=1, base=2):
        """
        Creates a new geometric progression.

        start       -> first term of the progression
        increment   -> fixed constant multiplied to each term
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by base."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """
        Creates a new Fibonacci progression.

        first   -> first term of the progression
        second  -> second term of the progression
        """
        super().__init__(first)
        self._prev = second - first    # temporary value

    def _advance(self):
        """Update current value by taking the sum of the previous two."""
        self._prev, self._current = self._current, self._prev + self._current

