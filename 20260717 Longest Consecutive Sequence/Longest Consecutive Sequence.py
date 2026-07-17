# =========================== original solution(right) ==================================
class Solution(object):
    def longestConsecutive(self, nums):
        snums = sorted(list(set(nums)))
        if len(snums) == 1:
            series = snums
        else:
            series = []
            for i in range(len(snums) - 1):
                series.append(snums[i])
                if snums[i + 1] - snums[i] == 1:
                    if len(series) >= 2 and series[-1] == series[-2]:
                        series.pop()
                    series.append(snums[i + 1])
                else:
                    series.pop()
                    if len(series) == 0:
                        series.append(snums[i + 1])
        a = 0
        print(series)
        series_len = []
        if len(series) == 1:
            series_len.append(1)
        elif not series:
            series_len.append(0)
        else:
            for i in range(len(series) - 1):
                if series[i + 1] - series[i] != 1:
                    series_len.append(i + 1 - a)
                    a = i + 1
                elif series[i + 1] == series[-1]:
                    series_len.append(i + 2 - a)

        return max(series_len)
# ========================== optimal solution================================================
class Solution(object):
    def longestConsecutive(self, nums):

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Find sequence starting points only
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

# Do not simulate the problem. Find the smallest information needed to solve it.