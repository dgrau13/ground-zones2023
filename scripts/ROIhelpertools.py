#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:51:25 2023

@author: annpu
"""

import numpy as np
from scipy.spatial.distance import cdist
from shapely.geometry import LineString


def triangle_maximum_angle(Ax, Ay, Bx, By, Cx, Cy):
    """
    Calculates the maximum angle within a triangle with
    vertices A, B and C

    Parameters
    ----------
    Ax: float
        x-coordinate of A vertice
    Ay: float
        y-coordinate of A vertice
    Bx: float
        x-coordinate of B vertice
    By: float
        y-coordinate of B vertice
    Cx: float
        x-coordinate of C vertice
    Cy: float
        y-coordinate of C vertice
    """
    # calculate sides of triangle (opposite interior angle at vertex)
    a = np.sqrt((Cx - Bx)**2 + (Cy - By)**2)
    b = np.sqrt((Cx - Ax)**2 + (Cy - Ay)**2)
    c = np.sqrt((Ax - Bx)**2 + (Ay - By)**2)
    # calculate interior angles and convert to degrees
    alpha = np.arccos((b**2 + c**2 - a**2)/(2.0*b*c))*180.0/np.pi
    beta = np.arccos((a**2 + c**2 - b**2)/(2.0*a*c))*180.0/np.pi
    gamma = np.arccos((a**2 + b**2 - c**2)/(2.0*a*b))*180.0/np.pi
    # return the largest angle within the triangle
    return np.max([alpha, beta, gamma])

def find_closest_point(x0, y0, points): 
    '''
    Computes the distance from x0,y0 to a list of points
    
    x0: float 
    x-coordinate of the x0,y0 point 
    
    y0: float 
    y-coordinate of the x0,y0 point
    
    points: list 
    A list of x,y coordinates. 
    
    '''
    
    # Compute the eucledian distance between points: 
    idx = np.argmin(cdist([(x0, y0)], points,  metric = 'euclidean')) 
    return points[idx]

def find_angle(is2_geom, GL):
    '''
    Inputs:
    - LineString of IS2 track geometry
    - GL.geometry
    '''
    ##1. Convert is2 geometry to linestring
    is2_line = LineString(is2_geom)
    ##2. Find coordinates of intersection between track and GL
    # Locate point of intersection between is2 track line and GL
    intersection = is2_line.intersection(GL.geometry)
    intersection= intersection.geometry.explode(index_parts=True)
    #print(intersection)
    ##3a. Find closest GL point to the intersect point
    #Convert GL geometry from multilinestring to linestring
    GL_exploded = GL.explode(index_parts=True)
    #Extract coordinates of points along GL line
    GL_nodes = np.column_stack((GL_exploded.geometry.iloc[0].coords.xy))
    #Get coordinates of IS2 track points
    is2_nodes = np.column_stack([np.array(is2_geom.x), np.array(is2_geom.y)])
    #Loop over all intersections on a single track
    for i in range(0,len(intersection)):
        x0, y0 = intersection[i].geometry.iloc[0].coords.xy
        x0=x0[0]
        y0=y0[0]
        #3b. Find coordinates of point on the GL closest to the intersect point
        closest_GL_node = find_closest_point(x0, y0, GL_nodes)
        ##4. Find closest point on IS2 track to the intersect point
        #Find coordinates of point on the IS2 track closest to the intersect point
        closest_is2_node = find_closest_point(x0, y0, is2_nodes)
        ##5. Find max angle between intersect point, closest GL point and closest IS2 point
        angle = triangle_maximum_angle(closest_GL_node[0], closest_GL_node[1],
                           closest_is2_node[0], closest_is2_node[1],
                           x0,y0)
        return x0,y0,angle