class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans,values = "",self.store.get(key,[])
        lp , rp = 0 , len(values) - 1
        while lp <= rp:
            m = lp + (rp - lp) // 2
            if values[m][1] <= timestamp:
                ans = values[m][0]
                lp = m + 1
            else:
                rp = m - 1
        return ans