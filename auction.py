import os
print("\n**************WELCOME TO ONE TIME BID AUCTION**************\n\n")
auction_bidder = dict()
highest_bid = 0
while True:
    name = input("Enter your name :: ")
    bid_amt = input("Bid amount :: $")
    if int(bid_amt) > int(highest_bid):
        highest_bid = bid_amt
        new_bidder = name
    auction_bidder[name] = bid_amt
    next = input("Is there any other bidder? Y/N :: ").lower()
    if(next == 'y'):
        if os.name == 'nt':
            os.system('cls')
        # Clear screen for Linux or Mac
        else:
            os.system('clear')

        # print("\n "*30)
    else:
        if os.name == 'nt':
            os.system('cls')
        # Clear screen for Linux or Mac
        else:
            os.system('clear')
        print(f'''
            \nWinner of this Auction is :: {new_bidder.upper()} with the highest bid of ${highest_bid}
              ''')
        input()
        exit()


