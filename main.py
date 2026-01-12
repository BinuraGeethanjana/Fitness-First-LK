# Display a welcome message
print("\n")
print(" Welcome to Fitness First LK\n")

#arrays used to store the data
registration_array=[] #the array used to store the Registration Number of the  members
name_array=[] #the array used to store the name of members
gender_array=[] #the array used to store the gender of members
height_array=[] #the array used to store the height of the members
weight_array=[] #the array used to store the weight of the members

#The main menu of the Fitness First
print("Main Menu\n")
print("1-Create Profile")
print("2-Update Profile")
print("3-Delete Profile")
print("4-Advices ")
print("5-Show Data \n")

#advices
underweight_male=("exercises-  1.Focus on compound exercises like squats, deadlifts,"
                  " bench presses, and overhead presses. These exercises promote muscle"
                  " growth and can help you gain healthy weigh\n"
                  "\t\t\t2.Cardio: While it's essential to focus on strength training, "
                  "you can include some cardiovascular exercises to improve your overall"
                  " fitness and appetite. Aim for short, high-intensity sessions, such as HIIT (High-Intensity Interval Training).\n"
                  "Meal-   1.Protein-Rich Foods: Include lean sources of protein in your diet,"
                  " such as chicken, turkey, fish, lean beef, tofu, and beans."
                  " Protein is essential for muscle growth\n "
                  "\t\t2.Healthy Fats: Consume sources of healthy fats like avocados, nuts, seeds, and olive oil to increase your calorie intake.")
underweight_female=("exercises-  1.Strength Training: Like males, focus on compound exercises that target multiple muscle groups."
                    " This will help you build muscle and gain weight.\n"
                    "\t\t\t2.Yoga and Pilates: These exercises can help improve flexibility, posture, and overall well-being."
                    " They can complement strength training.\n"
                    "Meal- 1.Protein: Consume lean sources of protein such as poultry, fish, lean beef, tofu, and legumes "
                    "to support muscle growth.\n"
                    "\t\t2.Healthy Fats: Incorporate avocados, nuts, seeds, and olive oil to add extra calories to your meals.")
normalweight=("Exercises- 1.Aerobic Exercise: Engage in regular aerobic exercises like brisk walking, running, cycling, "
              "or swimming to maintain cardiovascular health. Aim for at least 150 minutes of moderate-intensity aerobic activity per week.\n"
              "\t\t\t2.Strength Training: Include strength training exercises 2-3 times a week to build and maintain muscle mass. This can include weightlifting,"
              " bodyweight exercises, or resistance training.\n"
              "Meals- 1.Balanced Diet: Consume a variety of foods from all food groups, including fruits, vegetables, lean proteins,"
              " whole grains, and healthy fats.\n"
              "\t\t2.Fruits and Vegetables: Aim for a colorful array of fruits and vegetables to ensure you get a wide range of vitamins and minerals.")
overweight=("exercises- 1.Aerobic Exercise: Engage in regular aerobic activities like brisk walking, jogging, cycling, or swimming. Aim for at least 150-300 "
            "minutes of moderate-intensity aerobic exercise per week to promote weight loss and overall health.\n"
            "\t\t2.Flexibility and Balance: Incorporate stretching and balance exercises, such as yoga or Pilates, to improve flexibility and prevent injuries.\n"
            "Meals- 1.Whole Grains: Opt for whole grains like brown rice, whole wheat bread, quinoa, and oats to provide sustained energy and satiety\n"
            "\t\t2.Portion Control: Pay attention to portion sizes, and consider using smaller plates to help with portion control.")
obesity =("1.Medical evaluation- Start by consulting a healthcare professional, such as a doctor or a registered dietitian, to assess your specific health needs "
          "and create a personalized weight management plan. They can help you understand your unique risk factors and provide guidance tailored to your circumstances.\n"
          "2.Calorie reduction- A calorie deficit is necessary for weight loss. To create one, you can reduce portion sizes, choose lower-calorie options, and limit sugary "
          "and highly processed foods.\n"
          "3.Behavior modification-Consider working with a therapist or counselor who specializes in weight management or emotional eating. Behavioral strategies can help you "
          "address underlying issues that contribute to overeating.")


#main menu as the function to come back as a particular operation is ended
def main_menu():
    print("Main Menu")
    print("1-Create Profile")
    print("2-Update Profile")
    print("3-Delete Profile")
    print("4-Advices")
    print("5-Show Data \n")
    user_in = input("Enter your choice : ")
    if user_in == "1":
        create()
    elif user_in == "2":
        update()
    elif user_in == "3":
        delete()
    elif user_in == "4":
        advice()
    elif user_in=="5":
        show()
    else:
        print("Invalid Choice")
#Basic variables used
reg_no_base = 1000             #The number which the registration number starts

def create():
    global reg_no_base
    #Generation of registration numbers
    reg_no = reg_no_base + 1
    registration_array.append(reg_no)
    reg_no_base=reg_no
    name=input(" Enter the name of the member : ")  #name of the member
    name_array.append(name)
    gender=input(" Enter the gender of the member : ")  #gender of the member
    gender_array.append(gender)
    height=float(input("Enter the height in meters: "))  #height of the member
    height_array.append(height)
    weight= float(input("Enter the weight in kilograms : "))  #kilograms of the member
    weight_array.append(weight)
    print("Your Register No is:",reg_no,"\n")
    main_menu()


def update():
    update_choice=int(input("Enter the 4-digit register number that you want to update :")) #which member you need to make the changes
    if update_choice in registration_array:
            position=registration_array.index(update_choice) #getting the index of registration number
            update_record=input("Which data you need to change (Height/Weight) : ")
            if update_record=="weight" or update_record=="Weight": #changing the weight of the member
                new_weight=float(input(" Enter your New weight : "))
                weight_array[position]=new_weight
                print(" Your Weight is Successfully updated \n")
            if update_record=="height" or update_record=="Height" : #changing the height of the member
                new_height=float(input(" Enter your New Height : "))
                height_array[position]=new_height
                print(" Your Height is Successfully updated \n")
    else:
        print("Your Registration number doesn't exist \n")
        go_back=input("Do you want to go to main menu? (y/n) : ")
        if go_back=="y" or go_back=="Y":
            main_menu()
        elif go_back == "n" or go_back == "N":
            update()
        else:
            print("Enter a Valid Input")
    main_menu()

def delete(): # the function which is used to delete the records of a particular member
    delete_choice=int(input("Enter the Registration Number of your Member : "))
    if delete_choice in registration_array:
        position = registration_array.index(delete_choice)
        registration_array.pop(position)
        name_array.pop(position)
        gender_array.pop(position)
        height_array.pop(position)
        weight_array.pop(position)
        print("Your records has been deleted successfully")
    else:
        print("Your Registration number doesn't exist/Enter a valid Reg No \n")
        go_back = input("Do you want to go to main menu? (y/n) : ")
        if go_back == "y" or go_back == "Y":
            main_menu()
        elif go_back == "n" or go_back == "N":
            delete()
        else:
            print("Enter a Valid Input")
    main_menu()

def advice(): #the function which is used to calculate BMI & give the required Excercises and Diet plan according to there categories
    advice_reg=int(input(" Enter your registration number : "))
    position=registration_array.index(advice_reg)
    height=height_array[position]
    weight=weight_array[position]
    gender=gender_array[position]
    bmi = weight / (height ** 2)
    print("Your Body-Mass-Index(BMI) is",bmi)
    if (bmi <= 18.5) and gender == "male" or gender=="Male":
        print(" The member is underweight")
        print(underweight_male)
    elif (bmi <= 18.5) and gender == "female" or gender=="Female":
        print(" The member is underweight")
        print(underweight_female)
    elif (18.5 < bmi < 24.9 and gender == "male" or gender=="Male"):
        print("The member is normal weight")
        print(normalweight)
    elif ((18.5 < bmi < 24.9) and gender == "female" or gender=="Female"):
        print("The member is normal weight")
        print(normalweight)
    elif ((25 < bmi < 29.9) and gender == "male" or gender=="Male"):
        print("The member is Overweight")
        print(overweight)
    elif ((25 < bmi < 29.9) and gender == "female" or gender=="Female"):
        print("The member is Overweight")
        print(overweight)
    else:
        print("The member is Obesity")
        print(obesity)
    main_menu()

def show():
    print("Reg no:: ",registration_array)
    print(name_array)
    print(gender_array)
    print(height_array)
    print(weight_array)
    print("\n")
    main_menu()


user_in=input("Enter your choice : ")
if user_in=="1":
    create()
elif user_in=="2":
    update()
elif user_in=="3":
    delete()
elif user_in=="4":
    advice()
elif user_in=="5":
    show()
else:
    print("Invalid Choice")