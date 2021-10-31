import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming


   
# def route():

    
    

    
#     #take no.of showrooms
#     n=sd.askstring("Input", "How Many Showrooms are available withouth DC ?",parent=root)
#     if n.isnumeric() :
       
#         N=int(n)
       
#         #find route  
#         distance_matrix=np.zeros((N+1,N+1))

#         #taking distances            
#         for i in range(N+1):
#             for j in range (i+1,N+1):
#                 x=sd.askstring("Input", "Enter distances from "+str(i)+" to "+str(j)+"\nX when route is not defined.",parent=root)
#                 if x.upper()!="X":
#                     distance_matrix[i,j]=distance_matrix[j,i]=x
#                 else:
#                     distance_matrix[i,j]=distance_matrix[j,i]=10000
#         print(distance_matrix)

#         #results
#         permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
#         messagebox.showinfo("Result","Cost-effective path : "+">".join(list(map(str,permutation)))+">0"+"\nMinimum Distance: "+str(distance))
     
        
#     else:
#         messagebox.showerror("Error", "Enter Valid Number")
    
#     browse_text1.set("Cost-effective Route")
    