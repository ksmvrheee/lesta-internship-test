import collections


class CircularBufferFIFO(object):
    """Creates a circular buffer that works implying the FIFO principle."""
    def __init__(self, capacity):
        """Initializes an object with one given argument: the capacity of the buffer (must be integer)."""
        self.capacity = capacity
        self.data = [None] * capacity  # creating a list that we will be using for storage purposes
        self.size = 0

        self.head_coord = 0
        self.tail_coord = 0

    def enqueue_an_item(self, item):
        """Adds one element to the buffer."""
        if not self.size == self.capacity:
            if self.size:  # making sure there are items so head and tail are not the same item
                if self.tail_coord + 1 < self.capacity:  # making sure that the index won't be out of range
                    self.tail_coord += 1
                else:
                    self.tail_coord = 0

            self.data[self.tail_coord] = item
            self.size += 1

            print('The element is successfully enqueued.')
        else:
            print('Error: Cannot enqueue the element, the buffer is full.')

    def dequeue_an_item(self):
        """Deletes one element from the buffer and returns it."""
        if self.size:  # if there is at least one element
            el = self.data[self.head_coord]
            self.data[self.head_coord] = None

            if self.head_coord + 1 < self.capacity:  # making sure that the index won't be out of range
                self.head_coord += 1
            else:
                self.head_coord = 0

            self.size -= 1

            print('The element is successfully dequeued.')

            if not self.size:  # returning to the beginning to avoid the confusion
                self.head_coord = self.tail_coord = 0

            return el
        else:
            print('Error: Cannot dequeue the element, the buffer is empty.')

    def check_current_state(self):
        """Allows to check the structure current state."""
        if 0 < self.size < self.capacity:
            print(f'The buffer now has {self.size} of {self.capacity} elements filled.')
            print(f'Head is now an element number {self.head_coord+1}.')
            print(f'Tail is now an element number {self.tail_coord+1}.')
        elif self.size == self.capacity:
            print('The buffer is now full.')
        elif not self.size:
            print('The buffer is now empty.')

    def __str__(self):
        """Magic method for printing."""
        return str(self.data)

    def __bool__(self):
        """Magic method for the fast emptiness checking."""
        return self.size != 0


class CircularBufferUsingDeque(collections.deque):
    """
    That's just a case of using built-in class collections.deque.

    An example:

    >>ar = []
    >>buffer = CircularBufferUsingDeque(ar, maxlen=5)
    >>buffer.append(1)
    >>buffer.pop()
    1
    """
    pass
