class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        new_tokens = []
        operators = ["+", "-", "*", "/"]
        while len(tokens) > 1:
            for index , n in enumerate(tokens):
                new_tokens = []
                if n == "+":
                    value = int(tokens[index - 2]) + int(tokens[index -1])
                    for i in range(index -2):
                        new_tokens.append(tokens[i])
                    new_tokens.append(value)
                    for token in tokens[index+1:]:
                        new_tokens.append(token)
                    tokens = new_tokens
                    break
                elif n == "-":
                    value = int(tokens[index - 2]) - int(tokens[index -1])
                    for i in range(index -2):
                        new_tokens.append(tokens[i])
                    new_tokens.append(value)
                    for token in tokens[index+1:]:
                        new_tokens.append(token)
                    tokens = new_tokens
                    break
                elif n == "*":
                    value = int(tokens[index - 2]) * int(tokens[index -1])
                    for i in range(index -2):
                        new_tokens.append(tokens[i])
                    new_tokens.append(value)
                    for token in tokens[index+1:]:
                        new_tokens.append(token)
                    tokens = new_tokens
                    break
                elif n == "/":
                    value = int(int(tokens[index - 2]) / int(tokens[index -1]))
                    for i in range(index -2):
                        new_tokens.append(tokens[i])
                    new_tokens.append(value)
                    for token in tokens[index+1:]:
                        new_tokens.append(token)
                    tokens = new_tokens
                    break
        return tokens[0]

    def evalRPN_1(self, tokens: list[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()

                if token == "+":
                    value = left_operand + right_operand
                elif token == "-":
                    value = left_operand - right_operand
                elif token == "*":
                    value = left_operand * right_operand
                else:
                    value = int(left_operand / right_operand)
                stack.append(value)

        return stack[-1]
            




solution = Solution()

test1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(solution.evalRPN_1(test1))
        