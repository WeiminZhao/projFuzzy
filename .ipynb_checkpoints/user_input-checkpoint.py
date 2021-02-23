# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
def get_input(question,min_range,max_range):
    try:
        user_in = int(input(question))
        if user_in > max_range:
            return max_range,user_in
        elif user_in < min_range:
            return min_range,user_in
        else:
            return user_in,user_in
    except:
        print('input error')
        # get_input(question,min_range,max_range)



questions = [
                ['Ente your age: ',16,50],
                ['Ente the age differences between you and your siginificant other: ',0,50],
                ['What is the level of agreement on having kid in the future betweem you can your siginificant other? (1 - 10): ',0,10],
                ['How many kids do you have from precvious relationships?: ',0,10],
                ['What is the total yearly income of you and your spouse?: ',0,200000],
                ['What is the total networth of you and your spouse?: ',-800000,1400000],
                ['How many years have you been in relationship with your significant others: ',0,40],
                ['How many previous marriages you have had?: ',0,10],
                ['How effective would you rate your comunication with your spouse? (1 - 10): ',0,10],
                ['How satisfy are you with your shared values? (1 - 10): ',0,10],
                ['How many days in a year would you be living apart from each other?: ',0,365],
                ['What is the level of your education? (1 - 10): ',0,10],
                ['How would you rate your relationship with your parents? (1 - 10): ',0,10]
            ]

print('Welcome To Marriage Success Rate Calculator')
Userinputs = []
for i in range(len(questions)):
   Userinputs.append(get_input(questions[i][0],questions[i][1],questions[i][2]))

Userinputs = np.array(Userinputs)

print('Please Review You Anwsers')
print()
for i in range(len(questions)-1): 
    print('Question<'+str(i)+'>: ',questions[i][0],)
    print('Your Anwser: ',Userinputs[i,1])



# %%
