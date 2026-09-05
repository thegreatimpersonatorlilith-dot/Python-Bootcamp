names=[]
grades=[]
failed=[]
passed=[]
print("Enter End when done")
while True:
    name=input('Enter the name: ')
    if name=='End':
        break
    grade=float(input(f"Enter {name}'s grade: "))
    if grade<0 or grade>20:
            print("Da Fuck enter again") 
            pass  
    elif name!='End':
        names.append(name)
        grades.append(grade)
        if grade>=10:
             passed.append(name)
        else:
             failed.append(name) 

if len(grades)!=0:
     avrage=sum(grades)/len(grades)
     min=min(grades)
     lowestg=names[grades.index(min)]
     max=max(grades)
     highestg=names[grades.index(max)]
else:
    avrage='undefined'
    min='undefined'
    max='undefined'
    lowestg='undefined'
    highestg='undefined'
     
print(f"report card: \ncount: {len(names)}\navrage: {avrage}\nhighest grade: {max}({highestg})\nlowest grade: {min}({lowestg})\nnumber of failed students: {len(failed)}\nnumber of passed students: {len(passed)}\nfailed students: {failed}\npassed students: {passed}")
