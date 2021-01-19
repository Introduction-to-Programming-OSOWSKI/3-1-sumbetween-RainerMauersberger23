def sumBetween(x, y):
   
    cat = 0
   
    for i in range (x + 1, y):
        cat = cat + i
        
    return cat

print (sumBetween(5,7))
