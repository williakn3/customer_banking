# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from Account import Account
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter your savings balance: "))
    savings_interest = float(input("Please enter your interest savings rate: "))
    savings_months = float(input("Please enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    results_savings = create_savings_account(savings_balance, savings_interest, savings_months)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    if results_savings is not None:
        updated_savings_balance, interest_earned = results_savings
        print(f"interest earned on savings: {interest_earned}")
        print(f"updated savings acount balance: {savings_balance}")
    else:
        print("Error.")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Please enter the CD inteest rate: "))
    cd_months = float(input("Pleae enter the number of months for the CD account: "))
    # Call the create_cd_account function and pass the variables from the user.
    results_cd = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The amount of interest earned on the CD is: {interest_earned}")
    print(f"account balance including the interest earned{updated_savings_balance}")

if __name__ == "__main__":
    main()
    # Call the main function.
