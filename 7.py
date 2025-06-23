#Enhance your coding skills, start writing your code here!!
def is_leaf(n):
  return (n%4==0 and n%100!=0) or (n%400==0)
  
n=int(input())
if is_leaf(n):
  print("Leap Year")
else:
  print("Not a Leap Year")
