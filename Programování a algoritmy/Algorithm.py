print("Algorithm")

print("Welcome to training plan")
name = input("Enter your name:")
print("Hello,", name, "once again welcome to my first algorithm. This will be just simple training algorithm for school.")

while True:
    print("Choose Upper body, lower body, or skills:")
    print("1 - Upper body")
    print("2 - Lower body")
    print("3 - skills")

    trainer = input("Choose 1, 2, or 3: ")

    if trainer == "1": 
        print("Monday and Friday are for upper body training, Sunday's rest day.")
        print("For upper body days, you will need to consume 2300 calories, 170 grams of protein, and 250 grams of carbs.")
        print("Your workout will be as follows: Push-ups - 3x10, Pull-ups - 3 x 5, Dips - 3 x 8, and Plank - 3 x 30 seconds.")
        
        choice = input("Do you want to continue with this trainer? Y/N: ")
        if choice == "Y":
            print("Opening stat tracker.")
            calorie_goal = 2300
            protein_goal = 170
            carbs_goal = 250

            calories = int(input("How many calories did you consume: "))
            
            calories_left = calorie_goal - calories
            
            if calories_left > 0:
                print(calories_left, "calories left to consume.")
            elif calories_left == 0:
                print("Congratulations, you meet your calorie goal.")
            elif calories_left < 0:
                print("You overate", -calories_left, "calories.")
            
            protein = int(input("How much protein did you consume: "))
            
            protein_left = protein_goal - protein
            
            if protein_left > 0:
                print(protein_left, "protein left to consume")
            else:
                print("Congratulations, you meet your protein goal.")
            
            carbs = int(input("How many carbs did you eat: "))
        
            carbs_left = carbs_goal - carbs

            if carbs_left > 0:
                print(carbs_left, "carbs left to consume.")
            else:
                print("Congratulations, you meet your carb goal.")
            print("Thank you for using my algorithm for the upper body workout.")
        
            back = input("Do you want to go back to the workout choice? Y/N: ")
            if back == "Y":
                continue
            elif back == "N":
                break

        elif choice == "N":
            print("Returning to trainer options.")
        
            continue

    elif trainer == "2":
        print("Wednesday and Saturday are for lower body workout.")
        print("For lower body days, you need to consume 2400 calories, 170 grams of protein, and 275 grams of carbs.")
        print("Your lower body workout is as follows: Squats - 3 x 15, Lunges - 3 x 10 each leg, Glute bridges - 3 x 15, and Calf raises - 3 x 20.")

        choice = input("Do you want to continue with this trainer? Y/N: ")
        if choice == "Y":
            print("Opening stat tracker.")
            calorie_goal = 2400
            protein_goal = 170
            carbs_goal = 275

            calories = int(input("How many calories did you consume: "))
            
            calories_left = calorie_goal - calories
            
            if calories_left > 0:
                print(calories_left, "calories left to consume.")
            elif calories_left == 0:
                print("Congratulations, you meet your calorie goal.")
            elif calories_left < 0:
                print("You overate", -calories_left, "calories.")            
            
            protein = int(input("How much protein did you consume: "))
            
            protein_left = protein_goal - protein
            
            if protein_left > 0:
                print(protein_left, "protein left to consume")
            else:
                print("Congratulations, you meet your protein goal.")            
            
            carbs = int(input("How many carbs did you eat: "))
        
            carbs_left = carbs_goal - carbs
                                                
            if carbs_left > 0:
                print(carbs_left, "carbs left to consume.")
            else:
                print("Congratulations, you meet your carb goal.")
            print("Thank you for using my algorithm for the lower body workout.")
        
            back = input("Do you want to go back to the workout choice? Y/N: ")
            if back == "Y":
                continue
            elif back == "N":
                break
            
        elif choice == "N":
            print("Returning to trainer options.")

            continue

    elif trainer == "3":
        print("Tuesday and Thursday are for skill training.")
        print("For skill training days, you will need to consume 2200 calories, 170 grams of protein, and 225 grams of carbs.")
        print("Your skill training exercises are as follows: Handstand practice - 10 min, L-sit practice - 5 min, Crow pose - 5 min, and Hollow body hold - 3 x 20 sec.")
        choice = input("Do you want to continue with this trainer? Y/N: ")
        if choice == "Y":
            print("Opening stat tracker.")
            calorie_goal = 2200
            protein_goal = 170
            carbs_goal = 225

            calories = int(input("How many calories did you consume: "))
            
            calories_left = calorie_goal - calories
            
            if calories_left > 0:
                print(calories_left, "calories left to consume.")
            elif calories_left == 0:
                print("Congratulations, you meet your calorie goal.")
            elif calories_left < 0:
                print("You overate", -calories_left, "calories.")            
            
            protein = int(input("How much protein did you consume: "))
            
            protein_left = protein_goal - protein
            
            if protein_left > 0:
                print(protein_left, "protein left to consume")
            else:
                print("Congratulations, you meet your protein goal.")            
            
            carbs = int(input("How many carbs did you eat: "))
        
            carbs_left = carbs_goal - carbs                                          

            if carbs_left > 0:
                print(carbs_left, "carbs left to consume.")
            else:
                print("Congratulations, you meet your carb goal.")
            print("Thank you for using my algorithm for the skill training.")
        
            back = input("Do you want to go back to the workout choice? Y/N: ")
            if back == "Y":
                continue
            elif back == "N":
                break

        elif choice == "N":
            print("Returning to trainer options.")

            continue