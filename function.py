'''a vector made of twopoints A and B is defined as (x_b-x_a)*i + ((y_b-y_a)*j) + (z_b-z_a)*k'''

#p = [(1.0, 6.0, 2.0) , (3.0, 8.0, 2.0),(7.0,12.0,2.0)]
#a = [(0.0, 5.0, 0.0), (1.0, 6.0, 0.0), (2.0, 7.0, 0.0), (3.0, 8.0, 0.0), (4.0, 9.0, 0.0), (5.0, 10.0, 0.0)]
'''function to return the dot product, function to return the square distance, function to return the projection'''
#print p
#print a

'''Add function to return the distance between two points. Assumming point are distributed as tuples'''
def distance_points(tuple1,tuple2):
    distance=math.sqrt((tuple2[0]-tuple1[0])**2.0+
                       (tuple2[1]-tuple1[1])**2.0+
                       (tuple2[2]-tuple1[2])**2.0)
    return distance

'''function to return the legth of the segments'''
def squared_distance(my_list_of_points):
    squared_distance=np.zeros(len(my_list_of_points)-1)
    for i in range(0,len(squared_distance)):
        squared_distance[i]=math.sqrt((my_list_of_points[i+1][0]-my_list_of_points[i][0])**2.0 +
                                      (my_list_of_points[i+1][1]-my_list_of_points[i][1])**2.0 +
                                      (my_list_of_points[i+1][2]-my_list_of_points[i][2])**2.0)
        
    return squared_distance  

'''function to return a vector'''
def construct_vector(my_list_of_points):
    construct_vector={}
    counter=0
    for i in range(0,len(my_list_of_points)-1):
        construct_vector[i]=(my_list_of_points[i+1][0]-my_list_of_points[i][0],
                             my_list_of_points[i+1][1]-my_list_of_points[i][1],
                             my_list_of_points[i+1][2]-my_list_of_points[i][2])
    
    return construct_vector

'''function to construct a vector'''
def construct_vector_PtoS(my_list_1,my_list_2):
    '''loop over the main dictionaries: output two entries'''
    '''my_list_1 is the list of points in space and my_list_2 is the list_forming the segment'''
    construct_vector_PtoS={}
    counter = 0
    for i in range(0,len(my_list_1)):
        construct_vector_PtoS[counter]=[]
        for j in range(0,len(my_list_2)):
            #construct_vector_PtoS[counter_1]=[]
            construct_vector_PtoS[counter].append((my_list_1[i][0]-my_list_2[j][0],
                                                   my_list_1[i][1]-my_list_2[j][1],
                                                   my_list_1[i][2]-my_list_2[j][2]))
        counter+=1
    #print 'the dictionary is = ', construct_vector_PtoS
    
    return construct_vector_PtoS

'''define a function to calculate distances  from points to the segments'''
def dist_and_neighbours(my_list_1,my_list_2):
    dist_and_neighbours={}
    count=0
    for i in range(0,len(my_list_1)):
        dist_and_neighbours[count]=[]
        for j in range(0,len(my_list_2)):
           
            dist_and_neighbours[count].append(math.sqrt((my_list_1[i][0]-my_list_2[j][0])**2.0 +
                                                        (my_list_1[i][1]-my_list_2[j][1])**2.0 +
                                                        (my_list_1[i][2]-my_list_2[j][2])**2.0))
            
        count+=1
    #print dist     
    return dist_and_neighbours

'''define function to find the parameter t '''
def parameter_t(my_list_1,my_list_2):
    parameter_t={}
    count=0
    distance=squared_distance(my_list_2)
    
    
    for i in range(0,len(my_list_1)):
        parameter_t[count]=[]
        for j in range(0,len(my_list_2)-1):
            parameter_t[count].append((((my_list_1[i][0]-my_list_2[j][0])*(my_list_2[j+1][0]-my_list_2[j][0]))+
                                      ((my_list_1[i][1]-my_list_2[j][1])*(my_list_2[j+1][1]-my_list_2[j][1]))+
                                      ((my_list_1[i][2]-my_list_2[j][2])*(my_list_2[j+1][2]-my_list_2[j][2])))/
                                      (distance[j]**2.0))
        count+=1
    distances_and_neighbours=dist_and_neighbours(my_list_1,my_list_2)
    ''' some magic to store the nearest distance based on the  '''
    '''store points in a dictionary'''
    
    #print (distances_and_neighbours[0][0])
    print (distances_and_neighbours)
    #print parameter_t[0][0]
    print parameter_t
    
    print '                       '
    
    '''store the projections '''
    projections={}
    count_1=0
    count_2=0
    
    for key in parameter_t:
        projections[key]=[]
        for t in range(0,len(parameter_t[key])):
            
            if parameter_t[key][t]<0.0:
                
                '''It falls BEFORE LEFT point of the segment. return the point '''
                print 'I am less than  0.0 return parameter          ',parameter_t[key][t]
                print 'The point is BEFORE of the segment return nearest point   ',my_list_2[t]
                print ' The distance point to the nearest is     ',distances_and_neighbours[key][t]
                print '                        '
                projections[key].append([(my_list_2[t]),distances_and_neighbours[key][t]])
            elif parameter_t[key][t]>1.0:
                '''It falls AFTER RIGHT point of the segment. return the point '''
                
                print 'I am bigger than 1.0  return the parament        ',parameter_t[key][t]
                print 'The point is AFTER the segment  return nearest point',my_list_2[t+1]                
                print ' The distance point to the nearest is     ',distances_and_neighbours[key][t]
                print '                        '
                projections[key].append([(my_list_2[t]),distances_and_neighbours[key][t]])

                    
            else:
                mypoint_q = ()
                mypoint_q= mypoint_q + (my_list_2[t][0]+parameter_t[key][t]*(my_list_2[t+1][0]-my_list_2[t][0]),
                                        my_list_2[t][1]+parameter_t[key][t]*(my_list_2[t+1][1]-my_list_2[t][1]),
                                        my_list_2[t][2]+parameter_t[key][t]*(my_list_2[t+1][2]-my_list_2[t][2])) 
                print mypoint_q
                
                '''IT FALLS ON THE SEGMENT '''

                print 'I am between 0.0 and 1.0 return ---> return projection    ',parameter_t[key][t]
                               
                print 'Calculate the coordinates of the projected point. and return the distance'
                print '                      '
                projections[key].append([(mypoint_q),distance_points(mypoint_q,my_list_1[t])])
                print projections

        count_1+=1
                
    #print projections
                

            #projections[key].append((t))
    print '                                      '
        
    #print 'the projections are  ', projections
           
    return projections
print '                                      '
print '                                      '
print '                                     '


    
    
