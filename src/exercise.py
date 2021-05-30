def main():
    #write your code below this line
    print("")
    Richs_account = Account("Rich's account", 100)

    print("Initial state")
    print(Richs_account)

    Richs_account.deposit(20)
    
    print("End state")
    print(Richs_account)

# Don't edit below this line - this setup is required for testing
if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account
