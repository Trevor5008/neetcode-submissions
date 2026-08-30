class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        # Frequency of each character in the window
        freq = {}
        # Best length of the substring
        best = 0
        # Left pointer of the window
        l = 0

        # Right pointer of the window
        for r in range(len(s)):
            # Update the frequency of the current character
            freq[s[r]] = freq.get(s[r], 0) + 1
            # Window size
            window = r - l + 1
            # If the window is larger than the best length, update the best length
            # To make the whole window one letter, replace everything that is not
            # the majority letter: window - max(freq) replacements.
            while window - max(freq.values()) > k:
                # Update the frequency of the left character
                freq[s[l]] -= 1
                # If the frequency of the left character is 0, delete it
                if freq[s[l]] == 0:
                    del freq[s[l]]
                    # Move the left pointer to the right
                l += 1
                # Update the window size
                window = r - l + 1

            best = max(best, window)

        return best
