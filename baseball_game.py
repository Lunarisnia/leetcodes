class Solution:
    def callPoints(self, operations: list[str]) -> str:
        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        record_sum = 0
        for r in record:
            record_sum += int(r)
        return record_sum


if __name__ == "__main__":
    s = Solution()
    print(s.callPoints(["5", "2", "C", "D", "+"]))
