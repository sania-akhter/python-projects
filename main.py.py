marks = []
mark1 = int(input("Enter marks 1: "))
marks.append(mark1)

mark2 = int(input("Enter marks 2: "))
marks.append(mark2)

mark3 = int(input("Enter marks 3: "))
marks.append(mark3)

mark4 = int(input("Enter marks 4: "))
marks.append(mark4)

mark5 = int(input("Enter marks 5: "))
marks.append(mark5)

mark6 = int(input("Enter marks 6: "))
marks.append(mark6)
print("Marks: ",marks )

highest = max(marks)
print("Highest marks: ", highest)

lowest = min(marks)
print("Lowest marks: ", lowest)

avg =sum(marks)/6
print(avg)

count = 0
for mark in marks:
    if mark>80:
        count +=1

print("Students above 80 marks: ", count)
    


