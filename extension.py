""" 1.Find the sum of the digits of a two-digit number."""
n=45 
print (n//10+n%10)
n=67
print (n//10+n%10)
n=38
print (n//10+n%10)

"""2.Repdigit is a positive number composed out of the same digit. 
Create a function that takes an two-digit integer and returns whether it's a repdigit or not."""
n=44

print (n//10==n%10)
n=45
print (n//10==n%10)
n=-44
print (n//10==n%10)



"""3.Write a function that takes an integer minutes and converts it to seconds."""
a= 5
print (a*60)
a=2
print (a*60)



"""4.Create a function that takes the age in years and returns the age in days."""

a=65
print (a*365)
a=0
print (a*365)
a=20
print (a*365)




"""5.Write a function that takes two integers (hours, minutes), 
converts them to seconds, and adds them"""
def sum(x, y):
   sum= x*3600 + y*60
   return sum
print(sum(1, 3))
print(sum(2, 0))

    



    
     
 