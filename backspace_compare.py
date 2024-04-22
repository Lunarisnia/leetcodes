class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a_stack = []
        b_stack = []

        for c in s:
            if c != "#":
                a_stack.append(c)
            else:
                if len(a_stack) > 0:
                    a_stack.pop()

        for c in t:
            if c != "#":
                b_stack.append(c)
            else:
                if len(b_stack) > 0:
                    b_stack.pop()

        return "".join(a_stack) == "".join(b_stack)

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("a##c", "#a#c"))