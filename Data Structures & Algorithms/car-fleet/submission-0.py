class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(x,y) for x,y in zip(position,speed)]
        combined.sort(key=lambda x : x[0])

        stack = []

        for i in range(len(combined)-1,-1,-1):
            stack.append(combined[i])
            if len(stack) >= 2:
                time_last = (target - stack[-1][0]) / stack[-1][1]
                time_sec_last = (target - stack[-2][0]) / stack[-2][1]

                if time_last <= time_sec_last:
                    stack.pop()
        return len(stack)
        
        