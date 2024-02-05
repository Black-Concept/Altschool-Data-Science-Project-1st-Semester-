#!/usr/bin/env python
# coding: utf-8

# ### ALTSCHOOL AFRICA, SCHOOL OF DATA
# ### TINYUKA SEMESTER
# ### FIRST SEMESTER PROJECT
# ### SUBMITTED BY: SUNDAY O. OLADOKUN
# 
# ### PROJECT OVERVIEW: A local retail business, dealing with a variety of products, aims to streamline and automate its accounting procedures. The business operates two shifts per day with one worker on each shift. The primary goal is to create a Python project that assists in automating essential accounting tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.
# 
# ### Think of your shift sales as a list.

# ### 1. Calculate Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day.

# In[ ]:


# Since we are to imagine our shift sales as a list, I initialized an empty list to take my values

morning_sales = [] #Initialize an empty list for morning shift

def morning_entry():
    
    """
    This function allows the morning shift operator to enter each of the sales she makes one after the other.
    Her entries are then appended to the morning sales list earlier created.
    """
    
    print("Welcome to morning shift, enter your sales records one after the other")
    print("When you are done entering your sales records, you can exit by entering 'exit'")
    
    # Continuously prompt the user for integer inputs
    while True:
        # Get user input
        user_input = input("Enter your sales records, one after the other: ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            # Convert the input to a float to accommodate both whole and decimal numbers
            user_input = float(user_input)
            # Append the integer to the list
            morning_sales.append(user_input)

        except (ValueError, TypeError, NameError, SyntaxError):
            # If the input is not an integer, notify the user
            print("Please enter a valid integer or 'exit' to stop.")
            
    # Display the final list of integers entered
    print("------------------------------------------------------")
    print("Your sales for morning shift:", morning_sales)
    print(f"Total sales for morning shift: {sum(morning_sales)}")


# In[ ]:


# Since we are to imagine our shift sales as a list, I initialized an empty list to take my values

evening_sales = [] #Initialize an empty list for evening shift

def evening_entry():
    
    """
    This function allows the evening shift operator to enter each of the sales she makes one after the other.
    Her entries are then appended to the evening sales list earlier created.
    """
    
    print("Welcome to evening shift, enter your sales records one after the other")
    print("When you are done entering your sales records, you can exit by entering 'exit'")
    
    # Continuously prompt the user for integer inputs
    while True:
        # Get user input
        user_input = input("Enter your sales records, one after the other: ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            # Convert the input to a float to accommodate both whole and decimal numbers
            user_input = float(user_input)
            # Append the integer to the list
            evening_sales.append(user_input)

        except (ValueError, TypeError, NameError, SyntaxError):
            # If the input is not an integer, notify the user
            print("Please enter a valid integer or 'exit' to stop.")
            
    # Display the final list of integers entered
    print("------------------------------------------------------")
    print("Your sales for evening shift:", evening_sales)
    print(f"Total sales for evening shift: {sum(evening_sales)}")


# In[ ]:


def total_sales():
    
    """
    This function calculates the total sales made for the day by summing up morning and evening shift sales.
    """
    print("You have chosen to calculate the total sales for the day, Find the summary below:")
    print(f"Total sales for morning shift: {sum(morning_sales)}")
    print(f"Total sales for evening shift: {sum(evening_sales)}")
    
    try:
        total_daily_sales = sum(morning_sales) + sum(evening_sales) # Sum up the sales from morning and evening shifts
        print(f"Total daily sales is: ${total_daily_sales}")
        
        
    
    except (ValueError, TypeError, NameError, SyntaxError):  
        return "Invalid input, Kindly enter numeric values."


# This function (total_sales) could have been made to allow the user enter the total values for morning and evening sales but then, the figures could be manipulated by the user and besides, the program flows sequentially so its best it just returns the total thereby saving time too.

# ### 2. Calculate Worker’s Salary: given hourly rate and hours worked by a worker. retrieve the worker’s salary.

# In[ ]:


def worker_salary():
    """
    This function calculates the workers' salary based on the number of hours worked.
    Kindly note that working hours cannot be greater than 8 hours per day. The hourly rate has
    been set to a default of 25 dollars too.
    """

    try:
        print("Welcome to the salary calculator. You are required to enter the number of hours worked.")
        print("Kindly note that the maximum obtainable hours of work is 8 hours.")

        num_hours = float(input("Enter the total number of hours worked: "))

        if num_hours <= 8:  # Ensure the entered working hours are not above 8 hours
            hourly_rate = 25
            salary = hourly_rate * num_hours  # Calculate workers' salary based on hours and hourly rate

            print("------------------------------------------------------")
            print(f"Your total salary is ${salary}")
            print("------------------------------------------------------")

        else:
            print("Invalid number of working hours entered. Please enter the correct figure.")

    except (ValueError, TypeError):
        print("Invalid input. Kindly enter numeric values.")


# The worker's salary function takes the number of hours worked which should not be greater than 8 hours as this is like the maximum daily hours per shift. The hourly rate has been set to a default of 25 dollars too, the reason for this is to ensure that no one manipulates the figures. If changes need to be made, the engineer will handle that at the backend.

# ### 3. Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)

# In[ ]:


def profit_loss():
    
    """
    This function calculates whether the company made profit or
    loss by taking total selling price and total cost price as inputs
    """
    
    try:
    
        total_CP = float(input("Enter the total cost price for items sold: "))
        total_SP = float(input("Enter the total selling price for items sold: "))
        
        if total_SP < 0 or total_CP < 0: # Handle negative inputs
            return "Invalid input, Kindly enter positive numeric values."

        profit_loss = total_SP - total_CP # Calculate profit or loss

        if profit_loss < 0:
            print(f"You made a loss of ${profit_loss}")
        elif profit_loss > 0:
            print(f"You made a profit of ${profit_loss}")
        else:
            print(f"You did not make a loss or profit")
        
    except (ValueError, TypeError, NameError, SyntaxError):  
        return "Invalid input, Kindly enter numeric values."


# ### 4. Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales).

# In[ ]:


def morning_shift_tips(tip_perc=0.02):
    
    """
    This function calculates the tips earned by morning shift workers,
    it takes their total sales and returns 2% of that as the tip.
    """
    
    try:
        morning_shift_sales = sum(morning_sales)
#         if not isinstance(morning_shift_sales, (int, float)): # Handle type error
#             return "Error: morning_shift_sales should be a number."

        morning_tips = morning_shift_sales * tip_perc # Calculate morning tip
        print("------------------------------------------------------")
        print(f"Your tips for the morning shift is ${morning_tips}")
        print("------------------------------------------------------")
    
    except (ValueError, TypeError, NameError, SyntaxError):  
        return "Invalid input, Kindly enter numeric values."


# In[ ]:


def evening_shift_tips(tip_perc=0.02):
    
    """
    This function calculates the tips earned by evening shift workers,
    it takes their total sales and returns 2% of that as the tip.
    """
    
    try:
        evening_shift_sales = sum(evening_sales)

        evening_tips = evening_shift_sales * tip_perc # Calculate evening tip
        print("------------------------------------------------------")
        print(f"Your tips for the evening shift is ${evening_tips}")
        print("------------------------------------------------------")
    
    except (ValueError, TypeError, NameError, SyntaxError):  
        return "Invalid input, Kindly enter numeric values."


# ### 5. Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts).

# In[ ]:


def total_tips_daily(tip_perc=0.02):
    
    """
    This function calculates the total tips earned by earned
    for the day which is an addition of morning tips and evening tips
    """   
    
    morning_shift_sales = sum(morning_sales) # Total morning shift sales
    evening_shift_sales = sum(evening_sales) #Total evening shift sales
    morning_tips = morning_shift_sales * tip_perc # Calculate morning tip
    evening_tips = evening_shift_sales * tip_perc # Calculate evening tip
    
    total_tips = morning_tips + evening_tips # Calculate total tips
    print("------------------------------------------------------")
    print(f"The total tips for the morning shift is ${morning_tips}")
    print(f"The total tips for the evening shift is ${evening_tips}")
    print(f"The total tips for today is ${total_tips}")
    print("------------------------------------------------------")


# ### MAIN PROGRAM

# In[ ]:


# FlowChart For Main Program


# In[ ]:


import base64  # Importing the base64 module for encoding

# Open the image file in binary mode and encode it using base64
with open("Main Program FlowChart.jpg", "rb") as image_file: 
    encoded_string = base64.b64encode(image_file.read())

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

plt.figure(figsize=(15, 12))  # Set the figure size

# Set the title and labels
plt.title("FlowChart For Main Program")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")

# Read and display the image using matplotlib
image = mpimg.imread("Main Program FlowChart.jpg")
plt.imshow(image)
plt.show()


# In[ ]:


# Main program

def business_accounting():
    """
    This program is a mini accounting software developed to:
    1. Allow users to enter sales data into a list for morning and evening shifts.
    2. Calculate workers' salary by taking the number of hours worked and hourly rate
    3. Calculate whether the business made profit or loss or none of the above
    4. Calculate the total tips accrued per shift: Morning and Evening
    5. Calculate sum total of tips for the day: Morning and Evening
    """

    while True:  # Set the while loop for continuous running of the code
        print("------------------------------------------------------")
        print("Welcome To Your Business Accounting Management System")
        print("------------------------------------------------------")
        print("1. Enter sales data")
        print("2. Calculate Worker's Salary")
        print("3. Calculate Profit or Loss")
        print("4. Calculate Tips Per Shift")
        print("5. Calculate Total Tips")
        print("6. Exit")
        print("------------------------------------------------------")

        choice = input('Enter your choice (1-6): ')  # Take user's input for computation

        print("------------------------------------------------------")
        if choice == '1':
            print("You have chosen to enter sales data")
            print("Choose from the options below")
            print("------------------------------------------------------")
            print("1. Resume Morning Shift")
            print("2. Resume Evening Shift")
            print("3. Calculate Total Sales")
            print("4. Back to Main Program: Business Accounting")

            choice = input("Enter your choice (1 or 2 or 3 or 4): ")
            print("------------------------------------------------------")

            if choice == "1":
                print("------------------------------------------------------")
                # Calls function to handle entry of morning sales data
                morning_entry()
                print("------------------------------------------------------")
                choice2 = str(input("Do you want to handover to evening sales operator, y or n: "))
                if choice2.lower() == "y":
                    print("------------------------------------------------------")
                    # Calls function to handle entry of evening sales data
                    evening_entry()
                    print("------------------------------------------------------")
                    calculate_daily_total = str(input("Do you want to calculate the total sales? y or n: "))
                    if calculate_daily_total.lower() == "y":
                        print("------------------------------------------------------")
                        print(f"Total sales for morning shift: {sum(morning_sales)}")
                        print(f"Total sales for evening shift: {sum(evening_sales)}")
                        total_daily_sales = sum(morning_sales) + sum(evening_sales)  # Sum up the sales from morning and evening shifts
                        print(f"Total daily sales is: ${total_daily_sales}")
                        print("------------------------------------------------------")

                else:
                    business_accounting()

            elif choice == "2":
                print("------------------------------------------------------")
                # Calls function to handle entry of evening sales data
                evening_entry()
                print("------------------------------------------------------")
                calculate_daily_total = str(input("Do you want to calculate the total sales? y or n: "))
                if calculate_daily_total.lower() == "y":
                    print("------------------------------------------------------")
                    print(f"Total sales for morning shift: ${sum(morning_sales)}")
                    print(f"Total sales for evening shift: ${sum(evening_sales)}")
                    total_daily_sales = sum(morning_sales) + sum(evening_sales)  # Sum up the sales from morning and evening shifts
                    print(f"Total daily sales is: ${total_daily_sales}")
                    print("------------------------------------------------------")

                else:
                    business_accounting()
            elif choice == "3":
                # Calculates and displays total sales for both shifts
                total_sales()
            elif choice == "4":
                business_accounting()
            else:
                print("Invalid input, please enter a number between 1 and 4")

        elif choice == '2':
            # Calls function to calculate worker's salary
            worker_salary()

        elif choice == '3':
            print("You have chosen to calculate profit or loss made")
            print("Follow the prompt and enter the required inputs")
            # Calls function to calculate profit or loss
            profit_loss()

        elif choice == '4':
            print("You have chosen to calculate the tips accrued per shift")
            print("Choose a shift from the options below")
            print("1. Morning Shift")
            print("2. evening Shift")

            choose_shift3 = input("Enter your choice (1 or 2): ")

            if choose_shift3 == "1":
                # Calls function to calculate tips for the morning shift
                morning_shift_tips()
                calculate_daily_total = str(input("Do you want to calculate the tips for evening shift too? y or n: "))
                if calculate_daily_total.lower() == "y":
                    # Calls function to calculate tips for the evening shift
                    evening_shift_tips()
            elif choose_shift3 == "2":
                # Calls function to calculate tips for the evening shift
                evening_shift_tips()
            else:
                print("Invalid input, please enter a number between 1 and 2")

        elif choice == '5':
            print("You have chosen to calculate the total tips accrued for the day by morning and evening shifts")
            # Calls function to calculate total tips accrued for the day
            total_tips_daily()

        elif choice == "6":
            print("Goodbye and enjoy the rest of your day")
            break

        else:
            print('Invalid choice. please enter a number between 1 and 6.')


# In[ ]:




