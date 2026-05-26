class Solution():
    def buildArray(self, target, n):
        # Initialize counter to track position in target array
        tracker = 0
        # Initialize counter to track position in answer array
        counter = 0
        # Initialize answer list
        difference = max(target) - len(target)
        answer = [0] * ((difference * 2) + (len(target)))
        # Initialize stack
        stack = [0] * len(target)
        # Iterate over range 0 through n
        for i in range(1, n + 1):
            # If target[tracker] == i
            if target[tracker] == i:
                # Append "push" to answer
                answer[counter] = "Push"
                stack[tracker] = i
                counter += 1
                tracker += 1
                # if answer list is equal to target
                if stack == target:
                    #return answer
                    return answer
            # Otherwise
            else:
                # Append "Push", "Pop" to answer
                answer[counter] = "Push"
                counter += 1
                answer[counter] = "Pop"
                counter += 1


tests = [{"target":[1,3], "n":3}, {"target":[1,2,3], "n":3}]
test_answers = [["Push","Push","Pop","Push"], ["Push","Push","Push"]]

solution = Solution()
for t, a in zip(tests, test_answers):
    ans = solution.buildArray(t["target"], t["n"])
    if ans == a:
        print("pass")
    else:
        print("fail")