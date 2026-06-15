class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        result = []
        for n in nums:
            if nmap.get(n):
                nmap[n] = nmap[n] + 1
            else:
                nmap[n] = 1

        print(nmap)

        result = sorted(nmap.keys(), key=lambda x: nmap[x], reverse=True)

        return result[:k]