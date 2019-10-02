#!/usr/bin/env python3

import yaml, sys, json

student = """
assignments:
    1: 3
    2: 2
    3: 2
    4: 2
    5: 2
    6: 2
    7: 2
    8: 2
    9: 2
    10: 2
presentation: 2
absences: 0
distractions: 0
"""
print()

try:
    with open(sys.argv[1].split('.')[0] + '.yaml') as f:
        print(sys.argv[1].upper().split('.')[0])
        print()
        student = yaml.load(f.read())
except IndexError:
    print('[student]')
    print()
    print('EXAMPLE')
    print()
    student = yaml.load(student)
except Exception as e:
    print(e)
    exit()

# print()
# print(json.dumps(student, indent=4))
# print()


"""
    1: unsatisfactory sketches fail to fulfill the basic requirements of the exercise
    2: satisfactory sketches are functional and conceptually sound as expected
    3: exemplary sketches show a level of refinement and/or experimentation beyond the basic requirements

"""
assignment_grade = sum(student['assignments'].values()) / (len(student['assignments']) * 3) + .15
print('Sketches: %.2f%%' % (assignment_grade * 100))


"""
    1: unsatisfactory presentation (missing work or basic context)
    2: satisfactory presentation (basic info on artist and work shown)
    3: excellent presentation (conceptual aspects well-outlined)

"""

if 'presentation' in student:
    presentation_grade = student['presentation'] / 3
    print('Presentation: %.2f%%' % (min( (presentation_grade * 100), 100)))

    raw_grade = (assignment_grade * .9) + (presentation_grade * .1)
else:
    raw_grade = assignment_grade

raw_grade = min(raw_grade, 1.0)
print('Raw grade: %.2f%%' % (raw_grade * 100))
print()

"""
    absence -5%
    distraction (late or social media use) -2.5%

"""

final_grade = raw_grade
final_grade *= 1.0 - (student['absences'] * 0.05)
final_grade *= 1.0 - (student['distractions'] * 0.025)
print(student['absences'], 'absences')
print(student['distractions'], 'distractions')
print()


print('Course so far: %.2f%%' % (final_grade * 100))
print()


"""
to get an A, you need two 3s on the assignments (plus the first one you get for free), plus a 2 presentation, and no absences

a 1 on any assignment or on the presentation without any additional 3s is a C
with a 3 it cancels out, and it's a B

"""