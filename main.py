count = 0
import time

start = time.time()

def check(a,b, placeinbetween):
    return ((a!=b) and abs(a-b)!= placeinbetween)

for i in range(1,5):
    print('#',i)
    for j in range(1,5):
        if(
            check(j,i,1)
            ):
            print('#',i,'#',j)
            for k in range(1,5):
                if(
                    check(k,i,2) and check(k,j,1)
                   ):
                    print('#',i,'#',j, '#',k)
                    for l in range(1,5):
                        if(
                            check(l,i,3) and check(l,j,2) and check(l,k,1)
                        ):
                            print('Solution -->',i, ' ', j, ' ',  k, ' ', l)
                            count = count +1

print( count)
end = time.time()
print(end - start)
