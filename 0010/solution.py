#!/usr/bin/env python

from string import ascii_lowercase
from typing import Callable, Dict, Sequence, Set, Tuple, Collection

# Types
""" NFA:
(Q, A, T, q0, F)
Q is a set of states (set of integers)
A is a set of input symbols (the alphabet) (set of characters)
T is a transition function mapping state and input to a set of output states (q, a) -> {q...}
q0 is the start state (integer)
F is a set of final states (set of integers)
"""
NFA = Tuple[Set[int], Set[str], Dict[Tuple[int, str], Set[int]], int, Set[int]]
""" DFA:
(Q, A, T, q0, F)
Q is a set of states (set of integers)
A is a set of input symbols (the alphabet) (set of characters)
T is a transition function mapping state and input to output state (q, a) -> q
q0 is the start state (integer)
F is a set of final states (set of integers)
"""
DFA = Tuple[Set[int], Set[str], Dict[Tuple[int, str], int], int, Set[int]]
""" TestCase:
((s, p), b)
s is string to match
p is pattern to use for matching
b is expected result of match on string
"""
TestCase = Tuple[Tuple[str, str], bool]

def pattern2NFA(pattern: str, alphabet: Collection[str], kleen: str ='*', wildcard: str ='.') -> NFA:
    """
    given a string pattern and an alphabet,
    return a tuple describing the NFA equilivant to the pattern

    alphabet is a set of characters
    pattern is a string consisting of characters from alphabet, kleen, and wildcard
    optional arguments kleen and wildcard are characters which represent the following:
      kleen matches zero or more of the preceeding element
      wildcard matches any single character in alphabet

    return value:
    NFA as described above

    raises ValueError if either:
    - pattern contains a character not included in the given alphabet
    - kleen or wildcard are in given alphabet
    """

def NFA2DFA(automata: NFA) -> DFA:
    """
    given an NFA tuple (described above), output an equilivant DFA tuple

    return value:
    DFA as described above

    note: this representation of is not complete, missing transitions indicate strings not in language
    """

def matchDFA(automata: DFA, s: str) -> bool:
    """
    returns True is given string is matched by given DFA and False if it is not matched
    raises ValueError if string contains a character not included in the DFA's alphabet
    """

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return matchDFA(NFA2DFA(pattern2NFA(p, ascii_lowercase)), s)
               
def test(algorithm: Callable, test_cases: Sequence[TestCase]) -> None:
    for test in test_cases:
        attempt = algorithm(*test[0])
        if attempt != test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')
        else:
            print(f'Test passed ({test[0]}->{attempt})')

if __name__ == '__main__':
    test_cases = [
            (("aa", "a"), False),
            (("aa", "a*"), True),
            (("ab", ".*"), True),
            (("aab", "c*a*b"), True),
            (("mississippi", "mis*is*p*."), False),
            ] # type: Sequence[TestCase]
    test(Solution().isMatch, test_cases)

