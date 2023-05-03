#Multinomial dist : it is a generalisation of binomial dist
#parameter's - n(no of outcomes),pcals(list of possibilities of outcome),size(shape of returned array)
#let's take the example of the dice

from numpy import random
a = random.multinomial(6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(a)

#multinomual samples will not produce a single value , they will produce one value for each pvals
#the 1/6 in above is indicating the six side of the dice

# it is almost like binomial ,