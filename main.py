#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy
import BloodDonationPoint
import Patient

class Program:
    empCount = 0

    def __init__(self):
        # self.a = BDP*
        self.bloodDonationPoint = BloodDonationPoint.BloodDonationPoint()
        Patient.Patient(self.bloodDonationPoint).Activate(1.0)


run=Program()