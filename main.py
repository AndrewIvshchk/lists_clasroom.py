def p_a():
    arr=[1,2,3,4,5]
    print(arr[0:len(arr):2])

def p2_b():
    new_arr=[]
    arr=[1,2,2,3,3,3,4]
    for i in arr:
        if i%2==0:
            new_arr.append(i)
    print(new_arr)

def p3_c():
    arr=[1,5,2,4,3]
    a = [int(i) for i in arr]
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            print(a[i])

def p4_f():
    arr=[1,2,3,2,1]
    print(max(arr),arr.index(max(arr)))

def p_g():
    i=1
    arr=[1,0,1,0,1]
    l=len(arr)
    while i < l-1:
        if arr[i]>arr[i-1] and arr[i]> arr[i+1]:
            t=+1
            print(t)
        i=+1
def p_h():
    arr=[5,-4,3,-2,1]
    new_arr=[]
    for i in arr:
        if i>0:
            new_arr.append(i)
    print(min(new_arr))
def p_i():
    arr=[1,2,4,5,6]
    n=3
    for i in arr:
        if i-n==1 or i-n==-1:
            print(i)
            break
def p_j():
    arr=[165,163,160,160,157,157,155,154]
    n=162
    i=0
    while i < len(arr):
        y=+1
        if arr[i] >n:
            print(y)
            break
        i=+1
def p_k():
    a=[1,2,3,3,3]
    count = 0
    unique_array = []
    for x in a:
        if x not in unique_array:
            count += 1
            unique_array.append(x)
    print(len(unique_array))
def p_l():
    arr=[0,1,2,3,4]
    new_arr=[]
    for i in arr:
        if i%2==1:
            new_arr.append(i)
            y=+1
    print(min(new_arr))
    if y==len(arr):
        print(0)
def p_m():
    arr=[1,2,3,4,5]
    arr.reverse()
    print(arr)
def p_o():
    y=[3,4,5,2,1]
    maximum=max(y)
    minimum=min(y)
    i=0
    while i>len(y):
        if y[i]==maximum:
            y[i]=minimum
        elif y[i]==minimum:
            y[i]=maximum
        i=+1
    print(y)
def p_r():
    a=[1,2,1,2,3,3]
    counter = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                counter += 1
    print(counter)

def p_t():
    array = [3,2,1,2,3,4]
    count = 0
    unique_array = []
    for x in array:
        if x not in unique_array:
            count += 1
            unique_array.append(x)
    print(len(unique_array))



if __name__ == '__main__':
    pass


