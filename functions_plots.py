''' FUNCTIONS FOR PLOTTING'''

import numpy as np

def plot_function1(my_list_of_points):
    for point in range(0,len(my_list_of_points)):
        #print list_points[point]
        xs = np.array([my_list_of_points[point][0]])
        ys = np.array([my_list_of_points[point][1]])
        zs = np.array([my_list_of_points[point][2]])
        plt.plot(xs,ys,marker='o', markersize=10,color='b',label='surface points')




def plot_function2(my_list_of_points):
    for point in range(0,len(my_list_of_points)):
        #print list_points[point]
        xs = np.array([my_list_of_points[point][0]])
        ys = np.array([my_list_of_points[point][1]])
        zs = np.array([my_list_of_points[point][2]])
        plt.plot(xs,ys,marker='o', markersize=10,color='r',label='line points')