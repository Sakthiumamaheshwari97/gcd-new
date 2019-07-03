lcm1,lcm2=map(int,input().split())
maxima=max(lcm1,lcm2)
while(1):
   if(maxima%lcm1==0 and maxima%lcm2==0):
          print(maxima)
          break
   maxima+=1
