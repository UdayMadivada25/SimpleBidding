from art import logo

print(logo)
new_bid="yes"
d = {}

# method 2
def find_highest_bidder(bid_dict):
    winner=("")
    amount=0
    for key in bid_dict:
        if bid_dict[key]>amount:
            winner=key
            amount=bid_dict[key]


    print(f"The winner is {winner} with a bid of ${amount}")

while new_bid=="yes":
    name= input("What's your name? : ")
    price = int(input("Enter bidding amount: $"))
    d.update({name:price})
    new_bid=input("Are there any other bidders? Type 'yes or 'no'.").lower()
    print("\n"*30)
    # method 1
    if new_bid=="no":
        winner=max(d,key=d.get)
        print(f"The winner is {winner} with a bid of ${d[winner]}")
    else:
        new_bid="yes"

    # method 2
    if new_bid=="no":
       find_highest_bidder(d)
    else:
        new_bid="yes"






