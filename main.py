import library
def jobs(posts):
    skillist = library.skills()
    user_skill = posts.split(',')
    temp,number = library.user(user_skill,skillist)
    # print('based on your skills:')
    # print(' , '.join(user_skill))
    jobs = library.aviral(number)
    return jobs

<<<<<<< HEAD
=======
def from_intrests(intrests):
    skillist = library.skills()
    user_intrests = intrests.split(',')
    temp,number = library.user(user_intrests,skillist)
    jobs_basedon_intrests = library.aviral(number)
    return jobs_basedon_intrests

def from_parents(parents):
    skillist = library.skills()
    user_parents = parents.split(',')
    temp,number = library.user(user_parents,skillist)
    jobs_basedon_parents = library.aviral(number)
    return jobs_basedon_parents


>>>>>>> 6079f980d124966bf88341ab461689bbb9e53282
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
