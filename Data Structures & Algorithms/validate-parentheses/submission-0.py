class Solution:
    def isValid(self, s: str) -> bool:
        temp = ""
        for ch in s:
            if ch in "({[":
                temp += ch
            else:
                if not temp:
                    return False
                if (ch == ")" and temp[-1] == "(") or \
                   (ch == "]" and temp[-1] == "[") or \
                   (ch == "}" and temp[-1] == "{"):
                    temp = temp[:-1]
                else:
                    return False
        return temp == ""
