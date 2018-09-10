#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Process
import time
import Distributions

class Patient(Process.Process):

    

    def __init__(self, system):
        # Process.__init__(self)
        BrithTime = system.SystemTime
        BloodNeeded = Distributions.Distributions().GetGeometric()

# Pat=Patient()