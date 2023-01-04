class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freqs = Counter(tasks).values()
        rounds = 0
        for f in freqs:
            if f == 1:
                return -1
            rounds += floor((f+2)/3)
        return rounds
