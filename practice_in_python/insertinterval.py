# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        res = []
        p = newInterval
        for itvl in intervals:
            if itvl.end < p.start:
                res.append(itvl)
            elif itvl.start > p.end:
                res.append(itvl)
            elif itvl.start < p.start and itvl.end > p.end:
                return intervals
            elif itvl.start >= p.start and itvl.end > p.end:
                p.end = itvl.end
            elif itvl.start < p.start and itvl.end <= p.end:
                p.start = itvl.start
        res.append(p)
        return sorted(res, key=lambda itvl: itvl.start)

s = Solution()
intervals = []
newInterval = Interval(5, 7)
print(s.insert(intervals, newInterval))
