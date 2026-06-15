class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for st in s:
            if st.isalnum():
                cleaned.append(st.lower())
        
        print("".join(cleaned), "".join(reversed(cleaned)))
        
        if "".join(cleaned) == "".join(reversed(cleaned)):
            return True
        return False