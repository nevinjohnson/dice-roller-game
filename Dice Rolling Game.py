#Loop
#Ask:Roll the dice
#If user enters:y
# Generate two random numbers
#If the user enters:n
# print a thankyou message
#Terminate
#Else
# Print invalid choice

import random

roll_count = 0
total_sum = 0

while True:
    choice = input('Do you wanna roll the dice? (y/n): ').strip().lower()
    
    if choice == 'y':
        try:
            num_dice = int(input('How many dice would you like to roll? (1 or more): '))
            if num_dice < 1:
                print("You need to roll at least one die.\n")
                continue
            
            roll_count += 1
            results = [random.randint(1, 6) for _ in range(num_dice)]
            roll_sum = sum(results)
            total_sum += roll_sum

            print(f'You rolled: {results} | Sum of this roll: {roll_sum}\n')
        
        except ValueError:
            print("Please enter a valid number.\n")
    
    elif choice == 'n':
        print(f'\nThank you for playing!')
        print(f'You rolled the dice {roll_count} time(s).')
        print(f'Total sum of all the dice rolled: {total_sum}')
        break
    
    else:
        print('Invalid choice. Please enter "y" or "n".\n')


# import random

# run = True

# while run:
#     choice = input('Do you wanna roll the dice? (y/n): ').lower()
    
#     if choice == 'y':
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         print(f'({die1}, {die2})')
    
#     elif choice == 'n':
#         print('Thank you for playing!')
#         break 
    
#     else:
#         print('Invalid choice')