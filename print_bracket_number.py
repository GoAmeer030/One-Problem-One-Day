class Solution:
	def bracketNumbers(self, string):
	    stack = []
        answer = []
        bracket_counter = 0
        bracket_map = {}

        for char in string:
            if char == '(':
                bracket_counter += 1
                stack.append(bracket_counter)
                answer.append(bracket_counter)
                bracket_map[bracket_counter] = bracket_counter
            elif char == ')':
                if stack:
                    matching_bracket = stack.pop()
                    answer.append(bracket_map[matching_bracket])
        
        return answer
