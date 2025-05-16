from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings into a single string with length||string format."""
        return ''.join(f'{len(s)}||{s}' for s in strs)

    def decode(self, encoded: str) -> List[str]:
        """Decodes a string in length||string format into a list of strings."""
        result = []
        i = 0
        while i < len(encoded):
            j = encoded.find('||', i)
            if j == -1:
                raise ValueError("Invalid encoded string")
            length = int(encoded[i:j])
            result.append(encoded[j+2:j+2+length])
            i = j + 2 + length
        return result
