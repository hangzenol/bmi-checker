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
    res = round(result, 2)
    r = res
    if r <= 18.4:
        print(str(r) + " kg/m2")
        print("Your result : Underweight")
    elif r >= 18.5 and r <= 24.9:
        print(str(r) + " kg/m2")
        print("Your result : Normal")
    elif r >= 25.0 and r <= 39.9:
        print(str(r) + " kg/m2")
        print("Your result : Overweight")
    else:
        print(str(r) + " kg/m2")
        print("Your result : Obese")


#BMI Chart
def bmi_chart():
    print(" ____________________________________________")
    print("|       BMI         |          Status        |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     < 18.5        |       Underweight      |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     < 25.0        |          Normal        |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|     < 40.0        |        Overweight      |")
    print("|___________________|________________________|")
    print("|                   |                        |")
    print("|    >= 40.0        |          Obese         |")
    print("|___________________|________________________|\n")



#algorithm
bmi_chart()

try :
    a = float(input("What is your weight :"))
    b = float(input("What is your height :"))
    print("\n")
    bmi(b, a)
except:
    print("Input should be a number!")
finally:
    print("THANK YOU FOR USING OUR SERVICE!\n")