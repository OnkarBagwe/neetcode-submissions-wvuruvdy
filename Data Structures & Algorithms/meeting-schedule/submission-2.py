"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort(key=lambda i:i.start)
        # if len(intervals) == 0:
        #     return True
        # prevEnd = intervals[0].end
        # for i in range(1, len(intervals)):
        #     if intervals[i].start < prevEnd:
        #         return False
        #     prevEnd = intervals[i].end
            
        # return True

        intervals.sort(key=lambda i:i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
            
        return True