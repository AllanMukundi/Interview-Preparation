"""
An implementation of a Trie.
"""

class Trie:
    """Trie implementation."""

    class _Node:
        """A lightweight, non-public class used for storing a node."""
        __slots__ = '_letter', '_data', '_children'    # streamline memory usage

        def __init__(self, letter=None, data=None):
            """Initializes a Node."""
            self._letter = letter
            self._data = data
            self._children = {}

        def add(self, letter):
            """Adds a letter to the Trie."""
            self._children[letter] = Trie._Node(letter)

    def __init__(self):
        """Initializes the Trie."""
        self._root = self._Node()

    def add(self, word):
        """Adds a word to the Trie."""
        curnode = self._root
        for i in range(len(word)):
            if word[i] in curnode._children:
                curnode = curnode._children[word[i]]
            else:
                break
        while i < len(word): # create a new node for every letter
            curnode.add(word[i])
            curnode = curnode._children[word[i]]
            i += 1
        curnode._data = word    # stores the completed word in the node

    def has_word(self, word):
        """Returns 'True' if the Trie contains the specified word and 'False' otherwise."""
        if not isinstance(word, str):
            raise ValueError('word must be a string.')
        if (word == ''):
            return False
        curnode = self._root
        for letter in word:
            if letter in curnode._children:
                curnode = curnode._children[letter]
            else:
                return False
        return curnode._data == word

    def prefix_words(self, prefix):
        """Returns a list of all the words in the Trie that start with prefix."""
        if not isinstance(prefix, str):
            raise ValueError('prefix must be a string.')
        words = []
        curnode = self._root
        for letter in prefix:
            if letter in curnode._children:
                curnode = curnode._children[letter]
            else:
                return words
        stack = [curnode]
        while stack:
            curnode = stack.pop()
            if curnode._data != None:
                words.append(curnode._data)
            stack += [child for child in curnode._children.values()]
        return words

