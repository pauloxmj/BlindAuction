from replit import clear
import art

bidders = {}
def silent_auction(name, bid):
  bidders[name] = bid
  clear()
  
print(art.logo)
print("Welcome to the secret auction program.")

should_end = False
while not should_end:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")

  silent_auction(name, bid)

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if other_bidders == "no":
    should_end = True
    highest_bidder = max(bidders, key=lambda x: bidders[x])
    print(f"The highest bidder is: {highest_bidder} with a bid of ${bidders[highest_bidder]}")