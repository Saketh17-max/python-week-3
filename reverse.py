list = [ ]
n=int(input("Enter size of list: "))
for i in  range(n):
	ele=int(input("Enter the Element: "))
	list.append(ele)
list.reverse()	
print("The list is",list)
