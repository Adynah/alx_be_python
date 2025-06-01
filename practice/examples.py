# purchase_amount = float(input("Enter your purchase amount: "))

# if purchase_amount >= 1000:
#   discount = 0.1  # 10% discount
# elif purchase_amount >= 500:
#   discount = 0.05  # 5% discount
# else:
#   discount = 0  # No discount

# final_price = purchase_amount * (1 - discount)
# print("Final price after discount: $" + str(final_price))

adjective1 = input("Choose an adjective: ")
adjective2 = input("Choose an adjective: ")
adjective3 = input("Choose an adjective: ")
adjective4 = input("Choose an adjective: ")

story = (
      f"On a beautiful {adjective1} day, I went to the zoo. "
      f"I saw a funny {adjective2} monkey swinging from the trees. " 
      f"Then, I spotted a majestic {adjective3} lion lounging in the sun. "
)

if adjective4 in ["exciting, fun, beautiful"]:
    story += f"What an {adjective4} experience. I can't wait to go back."
elif adjective4 in ["strange, boring, dull"]:
    story += f"What an {adjective4} experience. It was a waste of time."
else:
    story += f"What a weird experince. I wonder what other colored animals exist."

print("\nHere is your story: ")
print(story)
      