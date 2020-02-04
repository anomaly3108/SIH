import library
def bitch(posts):
    skillist = library.skills()
    user_skill = posts.split(',')
    temp,number = library.user(user_skill,skillist)

    print('based on your skills:')
    print(' , '.join(user_skill))

    jobs = library.aviral(number)
    return jobs
'''
if len(jobs)==0:
    print('no job found')
elif len(jobs)==1:    
    print('The Recommended Job is: ')
    print(' , '.join(jobs))
else:
    print('The Recommended Job are: ')
    print(' , '.join(jobs))
'''