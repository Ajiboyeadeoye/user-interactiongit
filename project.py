loop = 1
while (loop < 10):
	print("..................")
	#all the questions that the program asks the user
	noun = input("choose a noun:")
	p_noun = input("choose a plural noun:")
	noun2 = input("choose a noun:")
	place = input("name a place:")
	adjective = input("choose an adjective (describing word):")
	noun3 = input("choose a noun:")
	#Displays the story based on the user imput
	print("............................")
	print("Be kind of your", noun, "-footed", p_noun)
	print("For a duck may be somebody's", noun2,",")
	print("Be kind of your", p_noun,"in", place)
	print("where the weather is always", adjective,",")
	print()
	print("you may think that is the", noun3, ",")
	print("well it is,")
	print(".............................")
	#loop back to "loop = 1"
	loop = loop +1