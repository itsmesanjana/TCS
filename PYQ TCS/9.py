# Q6. There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer
# Bananas and Peanuts, the
# Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total m number of
# Bananas and p number
# of Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after some of
# them jumped down to eat.
# At a time one Monkeys gets down and finishes eating and go to the other side of the road. The
# Monkey who climbed down
# does not climb up again after eating until the other Monkeys finish eating.
# Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on
# the ground or less than j
# Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
# Write code to take inputs as n, m, p, k, j and return the number of Monkeys left on the Tree.
# Where, n= Total no of Monkeys
# k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k
# Bananas)
# j = Number of eatable Peanuts by single Monkey (Monkey that jumped down last may get less than j
# Peanuts)
# m = Total number of Bananas
# p = Total number of Peanuts
# Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j
# having a value zero.


def monkeys_left_on_tree(n,m,p,k,j):
    monkeys_eating=(m//k)+(p//j)
    
    if m%k or p%j:
        mokeys_eating+=1
    return max(0,n-mokeys_eating)
# Input values from user
n = int(input("Enter total number of monkeys: "))
m = int(input("Enter total number of bananas: "))
p = int(input("Enter total number of peanuts: "))
k = int(input("Enter number of bananas a monkey can eat: "))
j = int(input("Enter number of peanuts a monkey can eat: "))

print("Monkeys left on the tree:", monkeys_left_on_tree(n, m, p, k, j))