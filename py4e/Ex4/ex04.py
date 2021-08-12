def computepay(h,r):
    if h>40:
        p=1.5*r*(h-40)+(40*r)
    else p=h*r
    return p
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h= float(hrs)
r= float(rate)
p = computepay(h,r)
print(p)
