#Function or extracing extrema and variables from subsized ICESat-2 tracks
def gzfeat_ext(longitude,latitude,elevation):
    #Import necessary libraries and packages
    import numpy as np 
    import matplotlib.pyplot as plt
    from scipy.signal import argrelextrema
    from haversine import haversine #from haversine.py within repository
    
    #Calculating Horizontal Distance of the subtrack 
    x = haversine(latitude[:], longitude[:],latitude[0],latitude[0]) #Horizontal distance along track
    y = elevation #Land ice elevation along track
    
    def find_primary_extrema(x, y):
        min_distance_from_edge = len(x) // 10  # Ensuring extrema aren't near the edges.
    
        order = 1
        max_order = len(x) // 5  # Set an upper limit to avoid indefinite loops
    
        while order < max_order:
            minima_indices = argrelextrema(y, np.less, order=order)[0]
            maxima_indices = argrelextrema(y, np.greater, order=order)[0]

            # Filter out minima and maxima that are too close to the edges
            minima_indices = minima_indices[np.logical_and(minima_indices > min_distance_from_edge, minima_indices < len(distance) - min_distance_from_edge)]
            maxima_indices = maxima_indices[np.logical_and(maxima_indices > min_distance_from_edge, maxima_indices < len(distance) - min_distance_from_edge)]
        
            # Check if we have a single minima and maxima
            if len(minima_indices) == 1 and len(maxima_indices) == 1 and minima_indices[0] < maxima_indices[0]:
                min_ind = minima_indices
                max_ind = maxima_indices
            
                return (min_ind,max_ind, order)
        
            order += 1

    # If we exit the loop without a return, it means we couldn't find suitable extrema
        return 0
    
    indices = find_primary_extrema(x,y) #min:0, max:1, order: 2

    ele_min = y[indices[0]] #Trough of Feature
    ele_max = y[indices[1]] #Peak of Feature
    
    lat_min =  latitude[indices[0]]#Latitude at Trough 
    lat_max =  latitude[indices[1]]#Latitude at Peak
    
    lon_min =  longitude[indices[0]]#Longitude at Trough 
    lon_max =  longitude[indices[1]]#Longitude at Peak
    
    
    dist_min =  x[indices[0]]#Distance along Track at Trough
    dist_max = x[indices[1]] #Distance along Track at Peak
    
    wavelength = 2*(dist_max-dist_min)# Wavelength of Each Feature 
    midpoint = (ele_min+ele_max)/2 #Midpoint of Each Feature

    return(ele_min, ele_max, lat_min, lat_max, lon_min, lon_max, dist_min, dist_max, wavelength, midpoint)
    
