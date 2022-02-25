class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = {}
        for i in range(len(position)): 
            position[i] = target-position[i]
            l[position[i]] = speed[i]
        position.sort()

        for i in range(len(position)):
            position[i] = position[i]/l[position[i]]

        j = 0
        m = None
        while j < len(position):
            if m == None:
                m = position[0]
                x = 1
            elif m < position[j]:
                x += 1
                m = position[j]
            j += 1
        return x