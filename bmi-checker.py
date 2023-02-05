'''
BMI Checker
-------------------------------------------------------------
'''

#Calculating the BMI result by accepting height and weight input
#as oarameters
def bmi(height, weight):

    x = 0.0
    x = weight / ((height/100)**2)
    bmi_result(x)

#Print out BMI result by accepting result as parameter
def bmi_result(result):
    if result <= 18.4:
        print(str(result) + " kg/m2")
        print("Your result : Underweight")
    elif result >= 18.5 and result <= 24.9:
        print(str(result) + " kg/m2")
        print("Your result : Normal")
    elif result >= 25.0 and result <= 39.9:
        print(str(result) + " kg/m2")
        print("Your result : Overweight")
    else:
        print(str(result) + " kg/m2")
        print("Your result : Obese")


#BMI Chart
def bmi_chart():
    print(" ____________________________________________")
    print("|       BMI         |          Status        |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     > 18.4        |       Underweight      |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     > 24.9        |          Normal        |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     > 39.9        |        Overweight      |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|    >= 40.0        |          Obese         |")
    print("|___________________|________________________|")





#algorithm
bmi_chart()

a = float(input("What is your weight :"))
b = float(input("What is your height :"))
bmi(b, a)