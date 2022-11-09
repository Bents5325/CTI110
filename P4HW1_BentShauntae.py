# CTI-110
# P4HW1 - Score List
# Shauntae Bent
# 11/9/22
#

score_list = []
num_scores = int(input('How many scores do you want to enter? '))
counter = 1

while counter <= num_scores:
    score = float(input(f'Enter Score #{counter}: '))
    if score < 0 or score > 100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score = float(input(f'Enter score #{counter} again: '))
        counter = counter + 1
        score_list.append(score)
    else:
        score_list.append(score)
        counter = counter + 1

print()
print(f'-------------Results------------')
print(f'Lowest Score   :   {min(score_list)}')
score_list.remove(min(score_list))
print(f'Modified List  :   {score_list}')
avg = sum(score_list)/len(score_list)
print(f'Scores Average :   {avg:.2f}')

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Grade          :   {grade}')

