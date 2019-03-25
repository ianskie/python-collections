# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(teachers):
    count = 0
    for teacher in teachers:
        count+=1
    return count

def num_courses(teachers):
    list_of_courses = []
    for course in teachers.values():
        list_of_courses += course               ,
    return len(list_of_courses)

def courses(d):
  out = []
  for teacher in d:
    out.extend(d[teacher])
  return out

def most_courses(teacher_dict):
    max_count = 0
    rockstar = ""
    for teacher, course_list in teacher_dict.items():
        if len(course_list) > max_count:
            max_count = len(course_list)
            rockstar = teacher
    return rockstar

def stats(teachers):
    namelist = [] #empty list
    for teacher, courses in teachers.items(): #for loop to go through the dictionary
        namelist.append([teacher, len(courses)]) #adding stats to the empty list
    return namelist
