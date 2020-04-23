
import csv
from PrimitivePoints import findPrimitivePoint

# Extended Euclidean algorithm
def extended_gcd(aa, bb):
   lastremainder, remainder = abs(aa), abs(bb)
   x, lastx, y, lasty = 0, 1, 1, 0
   while remainder:
       lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
       x, lastx = lastx - quotient*x, x
       y, lasty = lasty - quotient*y, y
   return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# calculate `modular inverse`
def modinv(a, m):
   g, x, y = extended_gcd(a, m)
   if g != 1:
       raise ValueError
   return x % m

# double function
def ecc_double(x1, y1, p, a):
   s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
   x3 = (s**2 - x1 - x1)%p
   y3 = (s*(x1-x3) - y1)%p
   return (x3, y3)

# add function
def ecc_add(x1, y1, x2, y2, p, a):
   s = 0
   if (x1==x2):
       s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
   else:
       s = ((y2-y1) * modinv(x2-x1, p))%p
   x3 = (s**2 - x1 - x2)%p
   y3 = (s*(x1 - x3) - y1)%p
   return (x3, y3)

def double_and_add(multi, generator, p, a):
   (x3, y3)=(0, 0)
   (x1, y1) = generator
   (x_tmp, y_tmp) = generator
   init = 0
   for i in str(bin(multi)[2:]):
       if (i=='1') and (init==0):
          init = 1
       elif (i=='1') and (init==1):
          (x3,y3) = ecc_double(x_tmp, y_tmp, p, a)
          (x3,y3) = ecc_add(x1, y1, x3, y3, p, a)
          (x_tmp, y_tmp) = (x3, y3)
       else:
          (x3, y3) = ecc_double(x_tmp, y_tmp, p, a)
          (x_tmp, y_tmp) = (x3, y3)
   return (x3, y3)

if __name__== '__main__':
   rows = []
   p = 751
   a = -1
   b = 188
   (x1, y1) = (0, 376) # primitive point 
   x2 = x1
   y2 = y1
   for k in range(2, 770):
      try:
         s = 0
         if (x1==x2 and y1 == y2):
            s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
         else:
            s = ((y2-y1) * modinv(x2-x1, p))%p
         x3 = (s**2 - x1 - x2)%p
         y3 = (s*(x1 - x3) - y1)%p
         print('{0}Q: {1} {2} {3}'.format(k, s, x3, y3))
         row = [k, s, x3, y3, '({0}, {1})'.format(x3, y3)]
         rows.append(row)
         x1 = x3
         y1 = y3
      except Exception as e:
         row = [k, None, None, None, 0]
         rows.append(row)
         break

   filename = 'kG.csv'
   fieldnames = ['k', 'lambda', 'x3', 'y3', 'kG = (x3, y3)']

   with open(filename, 'w') as csvfile:
      csvwriter = csv.writer(csvfile)  
      csvwriter.writerow(fieldnames)   
      csvwriter.writerows(rows) 
