def wage_calculator(hour_worked, hourly_rate):
    salary = hour_worked * hourly_rate
    return salary

def wage_checker(salary):
    if salary >= 5000:
        print ('he is a senior employee')

    elif salary < 5000 and  salary >= 2000 :
        print ("he is a mid level employee")

    elif salary < 2000 :
        print ("he is a beginner at the company")

    else :
        print("no answer") 