from random import randrange

"""
3.6 - An animal shelter, which holds only dogs and cats, operates
on a strictly FIFO basis. People must adopt either the 'oldest'
(based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will
receive the oldest animal of that type). They cannot select which
specific animal they would like.

--

Create the data structures to maintain this system and implement
operations such as enqueue, dequeue_any, dequeue_dog, and
dequeue_cat. 
"""

class Queue:

    INITIAL_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.INITIAL_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, i):
        if len(self._data) >= len(self._data) // 2:
            self._resize(len(self._data) * 2)
        index = (self._front + self._size) % len(self._data)
        self._data[index] = i
        self._size += 1

    def dequeue(self):
        if not self.is_empty():
            val = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            if (0 < self._size) and (self._size <= len(self._data) // 4):
                self._resize(len(self._data) // 2)
            return val
        raise IndexError('Sorry, there are no more of the requested animal.')

    def front(self):
        if not self.is_empty():
            return self._data[self._front]
        raise IndexError('Sorry, there are no more of the requested animal.')

    def _resize(self, num):
        old = self._data
        self._data = [None] * num
        start = self._front
        for i in range(len(self)):
            self._data[i] = old[start]
            start = (start + 1) % len(old)
        self._front = 0


class Cat:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Dog:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class AnimalShelter:

    def __init__(self):
        self._dogs = Queue()
        self._cats = Queue()

    def __len__(self):
        return len(self._dogs) + len(self._cats)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, animal):
        if not isinstance(animal, Cat) and not isinstance(animal, Dog):
            raise ValueError('Sorry, this shelter only houses cats and dogs.')
        if isinstance(animal, Cat):
            self._cats.enqueue(animal)
        elif isinstance(animal, Dog):
            self._dogs.enqueue(animal)

    def dequeue(self):
        selection = randrange(100) 
        if (selection < 50):
            try:
                return self._cats.dequeue()
            except:
                return self._dogs.dequeue()
        else:
            try:
                return self._dogs.dequeue()
            except:
                return self._cats.dequeue()

    def dequeue_dog(self):
        return self._dogs.dequeue()

    def dequeue_cat(self):
        return self._cats.dequeue()

    def front_dog(self):
        return self._dogs.front()

    def front_cat(self):
        return self._cats.front()


# Unit Tests:
if __name__ == '__main__':
    shelter = AnimalShelter()
    assert(shelter.is_empty() == True)
    assert(len(shelter) == 0)
    shelter.enqueue(Cat('Harold'))
    assert(shelter.dequeue().name() == 'Harold')
    shelter.enqueue(Cat('Allan'))
    shelter.enqueue(Dog('Ereneo'))
    assert(shelter.dequeue_dog().name() == 'Ereneo')
    assert(shelter.dequeue_cat().name() == 'Allan')
    shelter.enqueue(Cat('Barnes'))
    shelter.enqueue(Cat('Yatin'))
    shelter.enqueue(Dog('Kyler'))
    assert(shelter.front_cat().name() == 'Barnes')
    assert(shelter.front_dog().name() == 'Kyler')
    assert(len(shelter) == 3)
    shelter.dequeue_dog()
    assert(shelter.dequeue().name() == 'Barnes')
    assert(shelter.dequeue().name() == 'Yatin')
    assert(shelter.is_empty() == True)




    
