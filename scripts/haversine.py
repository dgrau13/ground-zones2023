import numpy

def haversine (lat2,lon2,lat1,lon1):
    radius = 6371*1000 # m
    dlat = numpy.radians(lat2-lat1)
    dlon = numpy.radians(lon2-lon1)
    a = numpy.sin(dlat/2) * numpy.sin(dlat/2) + numpy.cos(numpy.radians(lat1)) \
        * numpy.cos(numpy.radians(lat2)) * numpy.sin(dlon/2) * numpy.sin(dlon/2)
    c = 2 * numpy.arctan2(numpy.sqrt(a), numpy.sqrt(1-a))
    d = radius * c
    return d



