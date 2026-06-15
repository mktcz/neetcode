class Solution:
    def __init__(self):
        self.nmap = {}
    
    def getNum(self,n):
        return self.nmap[n]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for n in nums:
            if self.nmap.get(n):
                self.nmap[n] = self.nmap[n] + 1
            else:
                self.nmap[n] = 1

        print(self.nmap)

        result = sorted(self.nmap.keys(), key=self.getNum, reverse=True)

        return result[:k]