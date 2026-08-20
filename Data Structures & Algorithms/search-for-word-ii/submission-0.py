from typing import List, Dict


class TrieNode:
    def __init__(self):
            self.children: Dict[str, "TrieNode"] = {}
            self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children.setdefault(char, TrieNode())
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(row: int, col: int, node: TrieNode) -> None:

            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] == "#"
            ):
                return
            
            char = board[row][col]
            next_node = node.children.get(char)

            if next_node is None:
                return

            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None

            board[row][col] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(row + dr, col + dc, next_node)

            board[row][col] = char

            if not next_node.children and next_node.word is None:
                del node.children[char]
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result
        

        