#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np


class moneyAccount:
    """class for producing the numbers of how the wealth of an account is evolving"""

    def __init__(self):
        self.configuration = {
            "initialSavings": 0,
            # "monthlyEarning": 0,
            # "monthlySpending": 0,
            "monthlySaving": 0,
            "interestRate": 1,
        }

    def setInputConfiguration(self, **kwargs):
        for k, v in kwargs.items():
            self.configuration[k] = v

    # TODO: Make this with pandas instead of a dic <02-12-19, Janik von Ahnen>
    def calcEvolution(self, nYears=50):
        timeEvolution = {}
        newBalance = self.configuration["initialSavings"]
        for year in range(nYears):
            newBalance += self.configuration["monthlySaving"] * 12
            newBalance *= self.configuration["interestRate"]
            timeEvolution[year] = newBalance
        return timeEvolution

    def createInput(self, nYears=50.0, outFileName="inputData.txt"):
        with open(outFileName, "w") as outFile:
            outFileWriter = csv.writer(
                outFile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL,
            )
            outFileWriter.writerow(["year", "savings", "monthlyInterest"])
            evo = self.calcEvolution()
            for k, v in evo.items():
                outFileWriter.writerow(
                    [k, v, v * (self.configuration["interestRate"] - 1) / 12]
                )

    def __repr__(self):
        prettyString = (
            "Printing attributes for moneyAccount object:\n--------\n"
        )
        for k in self.__dict__:
            prettyString += (
                str(k) + "  :  " + str(self.__dict__[k]) + "\n--------\n"
            )
        return prettyString


bla = moneyAccount()
bla.setInputConfiguration(
    initialSavings=10000, monthlySaving=700, interestRate=1.04
)
print(bla)
bla.createInput()
