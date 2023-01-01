class Solution:
    def wordPattern(self, pattern: str, a: str) -> bool:
        a = a.split()
        return (len(set(pattern)) ==
                 len(set(a)) ==
                  len(set(zip_longest(pattern,a))))
