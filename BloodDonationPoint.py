#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Sche dule
from collections import deque


class BloodDonationPoint:

    def __init__(self):
        self.InitalPhase=400000
        self.SystemTime=0.0
        self.Schedule=Schedule.Schedule()
        self.PatientQueue = deque()
        self.BloodList = []
        self.EnFlag=False
        self.TbLevel=30
        self.TuTime=300
        self.N=15
        self.MinimalBlood=70
        self.Q=11
        self.UtilizedBlood=0
        self.BloodForScience=0

