from replit import clear
import art
print(art.logo)
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")
auctioneers = {}
Continue = True
n = 0
while Continue == True:
  Name = input("What is your name?: ")
  Bid = input("What's your bid?: ")
  auctioneers[Name] = Bid
  go = input("Are there any other bidders? Type yes or no. ")
  if go == "no":
    Continue = False
  else:
    clear()
for price in auctioneers:
  value = int(auctioneers[price])
  if value > n:
    winner = price
    n = value
print(f"The winner is {winner} with a bid of {n}")