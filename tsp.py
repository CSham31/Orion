import numpy as np
import itertools 
from mip import Model, xsum, minimize, BINARY
import time
import csv

from numpy.core.fromnumeric import prod
    
def TSP_ILP(G):
	start = time.time()
	V1 =  range(len(G))
	n, V = len(G), set(V1)
	model = Model()   # binary variables indicating if arc (i,j) is used 
	# on the route or not
	x = [[model.add_var(var_type=BINARY) for j in V] for i in V]   # continuous variable to prevent subtours: each city will have a
	# different sequential id in the planned route except the 1st one
	y = [model.add_var() for i in V]   # objective function: minimize the distance
	model.objective = minimize(xsum(G[i][j]*x[i][j] for i in V for j in V))
    
   # constraint : leave each city only once
	for i in V:
		model += xsum(x[i][j] for j in V - {i}) == 1   # constraint : enter each city only once
	for i in V:
		model += xsum(x[j][i] for j in V - {i}) == 1   # subtour elimination
	for (i, j) in itertools.product(V - {0}, V - {0}):
		if i != j:
			model += y[i] - (n+1)*x[i][j] >= y[j]-n   # optimizing
	model.optimize()   # checking if a solution was found
	if model.num_solutions:
		print('Total distance {}'.format(model.objective_value))
		nc = 0 # cycle starts from vertex 0
		cycle = [nc]
		while True:
			nc = [i for i in V if x[nc][i].x >= 0.99][0]
			cycle.append(nc)
			if nc == 0:
				break
		
	return (model.objective_value, cycle)
def main():
	with open('data1.csv', newline='') as csvfile:
		values_in_string =[]
		task_arr = []
		data =  list(csv.reader(csvfile,delimiter=','))
		arr=data[1:-2:]
		for row in arr:
			row.pop(0)
		
		matrix=[]
		for row in arr:
			#print (row)
			rown=[]
			for k in range(len(row)):
				
				rown.append(float(row[k]))
			matrix.append(rown)
		print(matrix)
	
	
	# adj=[[0.0, 5.0, 12.0, 1000.0, 2.0],
	# 	[5.0, 0.0, 10.0, 3.0, 1000.0], 
	# 	[12.0, 10.0, 0.0, 3.0, 8.0], 
	# 	[1000.0, 3.0, 3.0, 0.0, 4.0], 
	# 	[2.0, 1000.0, 8.0, 4.0, 0.0]]
	distance,route=(TSP_ILP(matrix))
	
	with open("output.csv", "w", newline="") as f:
	 	writer = csv.writer(f)
	 	writer.writerow(route)
		
if __name__ == '__main__':
    main()