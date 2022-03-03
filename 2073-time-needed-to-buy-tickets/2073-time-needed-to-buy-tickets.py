class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        count = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                count += tickets[i]
            elif i > k:
                count += (tickets[k]-1)
            else:
                count += (tickets[k])
        return count