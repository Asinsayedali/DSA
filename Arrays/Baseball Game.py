class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for element in operations:
            if element == "+":
                result.append(result[-1]+result[-2])
            elif element =="C":
                result.pop()
            elif element == "D":
                result.append(2*result[-1])
            else:
                result.append(int(element))

        return sum(result)