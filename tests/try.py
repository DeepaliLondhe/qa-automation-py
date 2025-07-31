

def totaltoys(amount,price): 
    return amount//price


amount = float (input("Enter the amount"))
price = float (input("Enter the price:"))

if price==0 :
    print("Price of the toy can not be zero")
    exit (0)
if amount==0:
    print("Amount is zero we can not buy anything")
    exit (0)
if ValueError:
    print ("Enter valid values")
print(totaltoys(amount,price))