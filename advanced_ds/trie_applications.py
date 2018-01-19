# Applications of TRIE

from trie import Trie

def getLongestPrefixMatch(root, key):
    pCrawl = root
    length = len(key)
    max_prefix_len = 0

    for level in range(length):
        if pCrawl.isEndOfWord:
            max_prefix_len = level

        index = ord(key[level]) - ord("a")
        if not pCrawl.children[index]:
            break
        pCrawl = pCrawl.children[index]

    return key[:max_prefix_len]


def app1():

    # Input keys (using only lower case)
    keys = ["the", "a", "there", "answer", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    t = Trie()

    for i in keys:
        t.insert(i)

    print getLongestPrefixMatch(t.root, "therefore")


class TrieBinaryNode:
    def __init__(self):
        self.children = [None]*2
        self.isEndOfRow = False

class customTrie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieBinaryNode()

    def insertRow(self, row):
        pCrawl = self.root

        for item in row:
            if not pCrawl.children[item]:
                pCrawl.children[item] = self.getNode()
            pCrawl = pCrawl.children[item]
            if pCrawl.isEndOfRow:
                return False
        pCrawl.isEndOfRow = True

        return True

def printRow(row):
    for i in row:
        print i,
    print

def printUniqueRows(matrix):

    t = customTrie()

    for i in matrix:
        if t.insertRow(i):
            printRow(i)


def app2():
    # matrix = [[0], [1], [0], [1]]
    matrix = [[0, 1, 0, 0, 1],
              [1, 0, 1, 1, 0],
              [0, 1, 0, 0, 1],
              [1, 1, 1, 0, 0],
              [1, 0, 1, 1, 0]]

    printUniqueRows(matrix)

def app3():
    ipAdds = ["74.125.200.106", "107.108.11.123", "107.109.123.255"]
    urls = ["www.google.in", "www.samsung.com", "www.samsung.net"]



if __name__ == '__main__':
    app2()
