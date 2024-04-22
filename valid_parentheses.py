class Solution:
    close_bracket = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        sterile = True
        stack = []

        open_bracket_stack = ["{", "[", "("]
        for c in s:
            if c in open_bracket_stack:
                sterile = False
                stack.append(c)
            else:
                if len(stack) > 0:
                    popped_bracket = stack.pop()
                    if self.close_bracket[c] != popped_bracket:
                        return False
                else:
                    return False

        return not sterile and len(stack) <= 0


if __name__ == '__main__':
    s = Solution()
    # () Valid
    # ([) invalid
    # ([]) valid
    # ([)] invalid
    print(s.isValid("){"))
