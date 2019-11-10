# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

class TrieNode:
    def __init__(self, data: str):
        self.data = data
        self.children = [None] * 26
        self.is_ending_char = False


class Trie:
    def __init__(self):
        self.root = TrieNode("/")

    def insert(self, text: str) -> None:
        node = self.root
        for index, char in map(lambda x: (ord(x) - ord("a"), x), text):
            if node.children[index] is None:
                node.children[index] = TrieNode(char)
            node = node.children[index]
        node.is_ending_char = True

    def find(self, pattern: str) -> bool:
        p = self.root
        for index in map(lambda x: ord(x) - ord("a"), pattern):
            if p.children[index] is None: return False
            p = p.children[index]
        return p.is_ending_char


if __name__ == "__main__":

    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(trie.find(s))

    print(trie.find("swift"))
