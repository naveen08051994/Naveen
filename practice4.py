#14. Write a Python program to print the numbers of a
# specified list after removing even numbers from it.
n=int(input("enter the list of values"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter the {} values".format(i)))
        lst.append(val)
    else:
        print("list of values")
        print(lst)

    removing_even_number=[]
    for val in lst:
        if(val%2==0):
            continue
        removing_even_number.append(val)
    print("removing_even_number{}".format(removing_even_number))

