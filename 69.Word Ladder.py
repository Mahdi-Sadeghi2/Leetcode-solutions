# Time complexity O(m^2*n) | Space complexity O(n)

from collections import deque



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is in wordList; if not, return 0 immediately
        if endWord not in wordList:
            return 0

        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        queue = deque()
        # Each queue element is a tuple (word, current_length)
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        # BFS loop
        while queue:
            current_word, length = queue.popleft()

            # Generate all possible one-letter transformations of current_word
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue  # Skip the same character to avoid unnecessary checks
                    # Construct the new word by replacing the i-th character
                    new_word = current_word[:i] + c + current_word[i+1:]

                    # Check if the new_word is the endWord
                    if new_word == endWord:
                        return length + 1

                    # Check if new_word is in wordSet and hasn't been visited
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        # If endWord was not reached
        return 0
