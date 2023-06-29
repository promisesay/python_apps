import glob
joke = glob.glob('../todos/*.txt')
print(joke)
for i in joke:
    with open(i, 'r') as file:
        park = file.read()
    print(park.upper())
