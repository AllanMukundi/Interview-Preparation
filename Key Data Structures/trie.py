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

        def add(self, letter, word=None):
            """Adds a letter or a node to the Trie."""
            if not isinstance(letter, type(self)):
                self._children[letter] = Trie._Node(letter, word)
            else:
                node = letter
                self.children[node._letter] = node

    def __init__(self):
        """Initializes the Trie."""
        self._root = self._Node()

    def add(self, word):
        """Adds a word to the Trie."""
        cur_node = self._root
        finished = True

        for i in range(len(word)):
            if word[i] in cur_node._children:
                cur_node = cur_node._children[word[i]]
            else:
                finished = False
                break

        if not finished:    # create a new node for every letter
            while i < len(word):
                cur_node.add(word[i])
                cur_node = cur_node._children[word[i]]
                i += 1

        cur_node._data = word    # stores the completed word in the node

    def has_word(self, word):
        """Returns 'True' if the Trie contains the specified word and 'False' otherwise."""
        if not isinstance(word, str):
            raise ValueError('word must be a string.')
        if (word == ''):
            return False

        cur_node = self._root
        exists = True
        for letter in word:
            if letter in cur_node._children:
                cur_node = cur_node._children[letter]
            else:
                exists = False
                break

        if exists:
            if (cur_node._data == None):
                exists = False

        return exists

    def prefix_words(self, prefix):
        """Returns a list of all the words in the Trie that start with prefix."""
        if not isinstance(prefix, str):
            raise ValueError('prefix must be a string.')
        words = []
        cur_node = self._root
        for letter in prefix:
            if letter in cur_node._children:
                cur_node = cur_node._children[letter]
            else:
                return words
        queue = [cur_node]
        while queue:
            cur_node = queue.pop()
            if cur_node._data != None:
                words.append(cur_node._data)
            queue += [node for letter, node in cur_node._children.items()] 
        return words

