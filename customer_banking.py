# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE ---  reference exercise 03.3.08
    savings_balance = float(input('What is the initial balance of the savings account? '))
    savings_interest = float(input('What is the savings interest rate? '))
    savings_months = float(input('How many months will the savings account be in use? '))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Your savings account earned ${savings_interest_earned} and the new balance is ${updated_savings_balance} after {savings_months} months')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE ---  reference exercise 03.3.08
    cd_balance = float(input('What is the initial balance of the CD account? '))
    cd_interest = float(input('What is the CD interest rate? '))
    cd_months = float(input('How many months will the CD account be in use? '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Your savings account earned ${cd_interest_earned} and the new balance is ${updated_cd_balance} after {cd_months} months')


if __name__ == "__main__":
    # Call the main function.
    main()
