def permute(s, result):
	if len(s) == 0:
		print(result, end=" ")
		return

	for i in range(len(s)):
		char = s[i]
		left_str = s[0: i]
		right_str = s[i+1: ]

		other_str = left_str + right_str
		permute(other_str, result + char)

permute("naruto", "")
		
