class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        pre = [0]
        for day in days:
            pre.append(pre[-1] + day)
        def to_days(s):
            mon, day = map(int, s.split('-'))
            return pre[mon-1] + day
        st = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))
        return max(0, end - st + 1)