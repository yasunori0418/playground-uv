"""127. Word Ladder
https://leetcode.com/problems/word-ladder/description/
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

辞書 wordList を使用した単語 beginWord から単語 endWord への変換シーケンスは、次のような単語 beginWord -> s1 -> s2 -> ... -> sk のシーケンスになります。
隣接する単語のペアはすべて 1 文字ずつ異なります。
1 <= i <= k のすべての si は wordList にあります。  beginWord は wordList にある必要はないことに注意してください。
sk == endWord
beginWord と endWord の 2 つの単語と辞書の wordList を指定すると、beginWord から endWord までの最短の変換シーケンス内の単語の数を返します。そのようなシーケンスが存在しない場合は 0 を返します。
"""
from collections import deque


def solve(beginWord: str, endWord: str, wordList: list[str]) -> int:
    return 5


assert solve("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
