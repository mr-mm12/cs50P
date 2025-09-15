class Jar:
    def __init__(self, capacity=12):
        """
        Initialize the cookie jar with a given capacity.
        By default, capacity is 12.
        Raise ValueError if capacity is not a non-negative integer.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Initially jar is empty

    def __str__(self):
        """
        Return a string with 🍪 repeated size times.
        Example: if size = 3 → "🍪🍪🍪"
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        Add n cookies to the jar.
        Raise ValueError if this would exceed capacity.
        """
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        """
        Remove n cookies from the jar.
        Raise ValueError if there aren’t enough cookies.
        """
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        """Return the jar’s capacity."""
        return self._capacity

    @property
    def size(self):
        """Return the current number of cookies in the jar."""
        return self._size

# Mohammad_Reza_Mokhtari_Kia
