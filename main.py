jaffa_cakes = 1.00
toilet_roll = 0.50

askProduct = input("What product would you like to buy? ")

if askProduct == 'jaffa cakes':
    print("You will get ", jaffa_cakes / 0.2, "clubcard points for your", askProduct)
elif askProduct == 'toilet roll':
    print("You will get", toilet_roll / 0.2, "clubcard points for your", askProduct)
elif (askProduct != 'toilet roll' or 'jaffa cakes'):
    print("That is not a valid product.")
