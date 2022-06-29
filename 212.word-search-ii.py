#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visited, foundWords = set(), set()

        root = TrieNode()

        for w in words:
            root.addWord(w)

        def dfs(r, c, node, word):
            if (
                r >= ROWS or
                c >= COLS or
                r < 0 or
                c < 0 or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))

            word += board[r][c]
            node = node.children[board[r][c]]

            if node.isWord:
                foundWords.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(foundWords)

        # @lc code=end
