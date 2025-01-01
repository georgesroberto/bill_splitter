import random

# Step 1: Get the number of people joining the party
num_of_people = int(input("Enter the number of friends joining (including you): "))

# Step 2: Check if the input number is valid (greater than 0)
if num_of_people <= 0:
    print("No one is joining for the party")
else:
    # Step 3: Create an empty dictionary to store names
    friends_dict = {}
    
    # Step 4: Get the names of each friend
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_people):
        name = input()  # Take the name input
        friends_dict[name] = 0  # Initialize their bill value to 0
    
    # Step 5: Get the total bill value
    total_bill = float(input("Enter the total bill value: "))
    
    # Step 6: Ask if they want to use the "Who is lucky?" feature
    use_lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    
    if use_lucky_feature == "Yes":
        # Step 7: Choose a random name
        lucky_person = random.choice(list(friends_dict.keys()))
        print(f"{lucky_person} is the lucky one!")
        
        # Step 8: Calculate the split amount for others
        split_value = round(total_bill / (num_of_people - 1), 2)
        for person in friends_dict:
            if person != lucky_person:
                friends_dict[person] = split_value
            else:
                friends_dict[person] = 0  # Lucky person pays 0
    else:
        print("No one is going to be lucky")
        
        # Step 9: Calculate the split amount equally
        split_value = round(total_bill / num_of_people, 2)
        for person in friends_dict:
            friends_dict[person] = split_value
    
    # Step 10: Print the updated dictionary with the split bill
    print(friends_dict)
