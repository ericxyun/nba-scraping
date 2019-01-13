import numpy as np

source = np.arange(1,31)









n = 0
for i in source:
	column[n].append(source[3 * n - 2])
	n += 1

Using:
a = []
b = []
c = []
column = [a, b, c]
# algorithm problem:
You have set of numbers from 1 to 9.
You have 3 empty lists: a, b, and c.
Find an algorithm to so that:
  	Bin A gets [1, 4, 7]
	Bin B gets [2, 5, 8]
	Bin C gets [3, 6, 9]

# harder algorithm problem:
You have a list that contains:
	[(0, 'a'), (1, 'b'), (2, 'c'), (3, ' '), (4, ' '), (5 ' '), (6, 'd') (7, 'e'), (8, 'f'), (9, ' '), (10, ' '), (11, ' '), (12, 'g'), (14, 'h'), (15, 'i')]
You have 3 empty lists: a, b, and c.
Find an algorithm so that:
	Bin A gets: [1, 7, 13]
	Bin B gets: [2, 8, 9]
	Bin C gets: [3, 9, 15]
