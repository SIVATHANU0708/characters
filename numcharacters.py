s=raw_input()
p=len(s)
count=0
for i in range(0,p):
 if(s[i]>='1' and s[i]<='9'):
  count=count+1
print(count)  
