from typing import Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word = False
        self.count = 0  # 部分木の単語数

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end_of_word = True
    
    
    def prefix_count(self, prefix: str) -> int:
        node = self._find_node(prefix)
        return node.count if node else 0


    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def __str__(self) -> str:
        def _dfs(node: TrieNode, prefix: str, depth: int) -> str:
            result = "  " * depth + (f"- {prefix} (end)" if node.is_end_of_word else f"- {prefix}") + "\n"
            for char, child in sorted(node.children.items()):
                result += _dfs(child, prefix + char, depth + 1)
            return result

        return _dfs(self.root, "", 0)