from typing import List

class _2025_09_30_Solution:
    @staticmethod
    def delimeter():
        return "||"

    def encode(self, strs: List[str]) -> str:
        """
        Encode a lit of strings such that it can be decoded later

        Key idea: need a delimeter plus a number of characters to scan
        Input: ["hello", "world", "longstring"]
        Output: "5||hello5||world10||longstring"
        """
        output = ""

        for s in strs:
            l = len(s)
            # encode length + delimeter + string
            encoding = str(l) + Solution.delimeter() + s
            output = output + encoding
        
        print(f"output: {output}")
        return output

    def decode(self, s: str) -> List[str]:
        """
        decode a list of strings
        Input: "5||hello"
        Output: ["hello"]
        Input: "5||hello10||longstring"
        Output:["hello", "longstring"]
        """
        n = len(s)
        cursor = 0
        output: List[str] = []

        while cursor < n:
            # find length of string
            digits = s[cursor:].find(Solution.delimeter())
            _length = int(s[cursor:cursor+digits])
            cursor += digits + len(Solution.delimeter())
            # read string
            cur = s[cursor:cursor+_length]
            output.append(cur)
            # advance cursor
            cursor += _length

        return output

class OldSolution:

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

Solution = _2025_09_30_Solution
