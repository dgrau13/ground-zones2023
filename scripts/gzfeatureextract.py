#Function or extracing extrema and variables from subsized ICESat-2 tracks
def gzfeat_ext(longitude,latitude,elevation):
    #Import necessary libraries and packages
    import numpy as np 
    import matplotlib.pyplot as plt
    from scipy.signal import argrelextrema
    from haversine import haversine #from haversine.py within repository
    
    #Calculating Horizontal Distance of the subtrack 
    x = haversine(latitude, longitude) #Horizontal distance along track
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
                minima_position = distance[minima_indices[0]]
                minima_height = height[minima_indices[0]]
                maxima_position = distance[maxima_indices[0]]
                maxima_height = height[maxima_indices[0]]
            
                distance_between_ = distance[maxima_indices[0]]-distance[minima_indices[0]]
            
                return (minima_position, maxima_position, minima_height, maxima_height, distance_between_, order)
        
            order += 1

    # If we exit the loop without a return, it means we couldn't find suitable extrema
        return None
    
    
    ele_min =  #Trough of Feature
    ele_max =  #Peak of Feature
    
    lat_min =  #Latitude at Trough 
    lat_max =  #Latitude at Peak
    
    lon_min =  #Longitude at Trough 
    lon_max =  #Longitude at Peak
    
    
    dist_min =  #Distance along Track at Trough
    dist_max =  #Distance along Track at Peak
    
    wavelength = [] # Wavelength of Each Feature 
    midpoint = [] #Midpoint of Each Feature
    