alphabets ="abcdefghijklmnopqrstuvwxyz"
p = 223
q = 271
n =0
print(alphabets[16])
phi_n = (p-1)*(q-1)
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
for x in range(40):
    if (7*x)
