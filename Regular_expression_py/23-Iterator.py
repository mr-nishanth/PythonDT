"""
1. Iterators are object that iterator upon
2. Base is __iter__  and __next__
3. Iterators are is everywhere in python
4. It's base for ( for loop )
5. List ,Tuples strings are  iterable means , can use in loop
6. For loop only Accept Iterator type
7. If yu want to create your own iterators you can do so

                For a in name ---> name is iterable object
                    print(a)

        Now we see, For loop working function

            Ex for loop iterator

            a = [1,2,3]
        -------------------------
        |   noraml for loop     |
        |                       |
        |      for i in a:      |
        |       print(i)        |
        -------------------------

        confusion statement--|
                             |
         obj = __iter__(a)

         while True:

                a = __next__(obj)

        yield a                
        
        # Yield is kind of return

"""


Name = (1,5,9,0,10)

for i in Name:
    print(i)
    print(type(i))