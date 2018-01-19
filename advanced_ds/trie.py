# Using trie to insert, delete and search a word.
# Time complexity O(key_length)
# Space complexity O(ALPHABET_SIZE*key_length*N), N is the no of keys in trie.  

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

    def leafNode(self):
        return self.isEndOfWord

    def isItFreeNode(self):
        for c in self.children:
            if c:
                return False
        return True

class Trie:
    # Trie node class

    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def wordCount(self, root):
        pCrawl = root
        count = 0

        if pCrawl.isEndOfWord:
            count += 1
        for i in range(26):
            if pCrawl.children[i]:
                count += self.wordCount(pCrawl.children[i])

        return count

    def display(self, root, level, string):
        pCrawl = root
        if pCrawl.isEndOfWord:
            # print level,
            print "".join(string[:level])
            # string[level] = None
            # s = ''
            # i = 0
            # while string[i]:
            #     s += string[i]
            #     i += 1 
            # print s

        for i in range(26):
            if pCrawl.children[i]:
                string[level] = chr(i+ord('a'))
                self.display(pCrawl.children[i], level+1, string)


    def delete(self, key):
        length = len(key)
        if length > 0:
            self._deleteHelper(self.root, key, 0, length)

    def _deleteHelper(self, pNode, key, level, length):
        if pNode:
            if level == length:
                if pNode.isEndOfWord:
                    pNode.isEndOfWord = False
                return pNode.isItFreeNode()
            else:
                index = self._charToIndex(key[level])
                if self._deleteHelper(pNode.children[index], key, level+1, length):
                    del pNode.children[index]
                    return (not pNode.leafNode() and pNode.isItFreeNode())

        return False
def main():

    # Input keys (using only lower case)
    keys = ["the", "a", "there", "answer", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    t = Trie()

    for i in keys:
        t.insert(i)

    print "The no of words:", t.wordCount(t.root)
    print "All words:"
    t.display(t.root, 0, [None]*20)

    print "{}.....{}".format("there", output[t.search("there")])
    print "{}.....{}".format("thew", output[t.search("thew")])
    print "{}.....{}".format("ans", output[t.search("ans")])
    print "{}.....{}".format("the", output[t.search("the")])

    t.delete("the")

    print "{}.....{}".format("there", output[t.search("there")])
    print "{}.....{}".format("thew", output[t.search("thew")])
    print "{}.....{}".format("ans", output[t.search("ans")])
    print "{}.....{}".format("the", output[t.search("the")])

    print "All words:"
    t.display(t.root, 0, [None]*20)


if __name__ == '__main__':
    main()
