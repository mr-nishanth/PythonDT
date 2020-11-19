# Cars = ['bmw', 'audi', 'zen', 'rolls royal']
# for Car in Cars:
#     if Car == 'bmw' or Car == 'rolls royal':
#         print(Car.upper())
#     else:
#         print(Car.title())


Dosa_Price = 20
requested_toppings = ['Ghee', 'Onion']#, 'Veg','Egg']
for requested_topping in requested_toppings:
    if requested_topping == 'Ghee': #and 'Egg':
        Dosa_Price += 10
    else:
        Dosa_Price +=20

    #print(f'Dose price : {Dosa_Price}')
    print(Dosa_Price)