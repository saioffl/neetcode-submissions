class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only letters and numbers, then lowercase them
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        # Compare to its reversed version
        return cleaned_str == cleaned_str[::-1]
