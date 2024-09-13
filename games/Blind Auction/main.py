#Blind Auction
import art
print(art.logo)
more_bids = True
bids = {}


def add_bid(name,bid):
    bids[name] = bid

while more_bids:
    usr_name = input("What is your name?: ")
    usr_bid = int(input("What is your bid?: $"))
    add_bid(usr_name,usr_bid)
    another_bid = input("Are there any other bidders? 'yes' or 'no'").lower()
    if another_bid == "yes":
        print("\n" * 20)
        continue
    else:
        high_bidder = max(bids.values())
        high_bidder_name = [key for key, value in bids.items() if value == high_bidder]

        print(f"Highest Bid: {high_bidder} by {', '.join(high_bidder_name)}")
        more_bids = False
