import csv
def aviral(number):
    jobs=[]
    with open('jobs.csv', newline='') as File:  
        reader = csv.reader(File)
        for i,row in enumerate(reader):
            if i in number:
                jobs.append(row[1])

        if len(jobs)==0:
            print('no job found')
        elif len(jobs)==1:    
            print('The Recommended Job is: ')
            print(' , '.join(jobs))
        else:
            print('The Recommended Job are: ')
            print(' , '.join(jobs))
                    
def skills():
    array=[]
    with open('jobs.csv', newline='') as File:  
        reader = csv.reader(File)
        for i,row in enumerate(reader):
            array.append(row[3][1:][:-1].split(","))
    return array


def user(inp,skillist):
    array=[]
    number=[]
    for x in inp:
        for i,y in enumerate(skillist):
            if x in y:
                if y not in array:
                    array.append(y)
                    number.append(i)
    return array,number

skillist = skills()
user_skill =input().split(",")
temp,number = user(user_skill,skillist)
print('based on your skills:')
print(' , '.join(user_skill))
aviral(number)
