# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('What is the initial balance of the savings account? '))
    savings_interest = float(input('What is the APR for your savings account? '))
    savings_months = int(input('How many months will the savings account be earning interest? '))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Your savings account earned ${savings_interest_earned:,.2f} over {savings_months} months and the new balance is ${updated_savings_balance:,.2f}.')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('What is the initial balance of the CD account? '))
    cd_interest = float(input('What is the APR for your CD account? '))
    cd_months = int(input('What is the length of your CD account (in months)? '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'Your CD account earned ${cd_interest_earned:,.2f} over {cd_months} months and the new balance is ${updated_cd_balance:,.2f}.')

if __name__ == "__main__":
    # Call the main function.
    main()
