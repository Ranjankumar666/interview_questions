class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
            
        curr.isWord = True
        
        
            
if __name__ == '__main__':
    root = TrieNode()
    words = ['app', 'ape', 'ace']
    
    for w in words:
        root.addWord(w)
        
    
    