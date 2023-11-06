n=int(input("enter total nos"));
n1,n2=0,1
print(n1)
for i in range(1,n):
    
    print(n2)
    new=n1+n2
    n1=n2
    n2=new

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if n<= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence in recursive:")
   for i in range(n):
       print(recur_fibo(i))