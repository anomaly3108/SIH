import csv
def aviral(number):
    jobs=[]
    with open('jobs.csv', newline='') as File:  
        reader = csv.reader(File)
        for i,row in enumerate(reader):
            if i in number:
                jobs.append(row[1])
    return jobs
                    
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

def inp():
    user_skill = input().split(",")
    return user_skill
