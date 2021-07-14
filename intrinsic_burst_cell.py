#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:30:22 2021

@author: singhmy
"""

import izhikevich_cells as izh

class ibCell(izh.izhCell):
    """
    class modeling an intrensically bursting cell
    """
    def __init__(self, stimVal):
        """
        method initializing the values for the model

        """
        super().__init__(stimVal)
        
        # define the parameters
        self.celltype='Intrinsically Bursting' # Regular spiking
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
            
myCell = ibCell(4000)
myCell.simulate()
if __name__=='__main__':
    izh.plotMyData(myCell)
        