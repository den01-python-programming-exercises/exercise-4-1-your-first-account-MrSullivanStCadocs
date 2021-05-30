def main():
    #write your code below this line
    
    Richs_account = Account("Rich's account", 100)

    Richs_account.deposit(20)
    
    print(Richs_account.balance)
    

# Don't edit below this line - this setup is required for testing
if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account
