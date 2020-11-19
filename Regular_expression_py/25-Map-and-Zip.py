'''
    <--------ZIP------->
    
    1. Zip function takes iterables
    2. Returns iterator of tuples
    3. Zip accepts parameters of iterable
    4. If empty argument, return empty iterator
    5. If paases different count arguments then its stops at the minimum value


    <----------MAP--------->

    1. Map function accepts a function as first arguments
    2. Second argument would be a set values 
    3. Map also supports lambda expression
    4. Second  parameter must be a iterable


'''


                        # ZIP

    # firs Iter       Second Iter

'''
a=zip([1, 2, 3, 4, 4, 2, 3], [2, 3, 4, 5, 1, 2, 5])  # Now we check same element

result = tuple(a)

print(a)
print(type(a))
print("\n")

print(result)

'''

                    # MAP

            # Map take two arguments .. 1st's is function 2nd's is Iterators

'''
def add_number(a, b):
    return a + b
    


 
a = map(add_number, [1, 2, 3, 4], [4, 5, 6, 3])
result = tuple(a)

print(a)
print(type(a))

print("\n")

print(result)
print(type(result))
'''
# This function is store in call stack memory define yakerukuim
def add_number(a, b):
    return a + b
    
# Lambda is inline function and , 
a = map(lambda x: x * x, [2, 3, 4])
b= map(lambda x,y: x -y, [20,10,50],[5,7,20])

result = tuple(a)

res = tuple(b)

print(a)

print("\n", result)

print(b)

print("\n",res)