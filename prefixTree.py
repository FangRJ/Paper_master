import collections

class Node(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(Node)
        # If there is a word, there should not be None.
        self.word = None
        # Count every node frequency.
        self.count = 0

class Trie(object):
    """
    Trie: prefix tree
    """
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            # create a child, count + 1
            current = current.children[letter]
            current.count += 1
        current.word = word
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            # choose the letter in children
            current = current.children.get(letter)
            if current == None:
                return False
        return current.word == word

    def showTrie(self, node):
        if node.children == {}:
            print(node.word)
            return
        elif node.word != None:
            print(node.word)
        for letter in node.children.keys():
            self.showTrie(node.children.get(letter))

    def startWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Print the word with "prefix" in the trie.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current == None:
                return False
        self.showTrie(current)
        return True
    
    def delete(self, word):
        """
        Delete a word from the trie, returns if the word is deleted successfully.
        :type prefix: str
        :rtype: bool
        """
        mission = False
        if self.search(word):
            mission = True
            current = self.root
            for letter in word:
                wNode = current.children.get(letter)
                # delete a node count, if the number of current node is 0, delete it
                wNode.count -= 1
                if wNode.count == 0:
                    # current is Node object, but current.children is dict object
                    # del current will not change [global variable t], though they own the same memory address
                    current.children.pop(letter)
                    break
                current = wNode
        return mission
    
    def deleteTrie(self):
        """
        Delete a trie object.
        """
        nodes = self.root.children
        for k in list(nodes.keys()):
            if k is not None:
                nodes.pop(k)
        del self.root


# if __name__ == "__main__":
#     t = Trie()
#     t.insert('apple')
#     t.insert('apply')
#     t.insert('application')
#     t.insert('adapt')
#     t.insert('add')
#     t.insert('addams')
#     t.insert('addict')
#     t.insert('go')
#     t.insert('god')
#     t.insert('good')
#     t.insert('great')
#     t.insert('ground')
#     t.insert('gradient')
#     print(t.startWith('ad'))
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
if 'Bob' in d:
    ans = d.get('Tracy')
print(ans)