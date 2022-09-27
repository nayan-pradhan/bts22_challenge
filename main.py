
from multiprocessing.dummy import Process
from typing import Reversible
import itertools

class TriangulationClass():
    '''
    Vizualization 
    Calculation of intersection
    Conversion of intersection point from xyz to lat long depth
    '''
    def __init__(self, A, B, C):
        index_ids = [A.id, B.id, C.id] # index of receiver 
        print(index_ids)
        
        transmitter_lat_long = [] # output

        # A.print_hello_world()
        


class ReceiverClass():
    '''
        Stores raw 
        Calculated data of each receiver
    '''

    id_iter = itertools.count()

    def __init__(self):

        self.id = next(ReceiverClass.id_iter) # id of receiver instance

        time_ = [] # get from receiver
        depth_ = [] # get from receiver
        
        lat_long_coord = [] #
        xy_coord = [] #
        
        radius_ = [] # calculate

    def print_hello_world(self):
        print('hello world')


if __name__ == '__main__' :
    A = ReceiverClass() 
    B = ReceiverClass() 
    C = ReceiverClass() 

    TriangulationClass(A, B, C)
    