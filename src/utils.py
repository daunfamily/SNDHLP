# -*- coding: utf-8 -*-
"""
@Created at 2020/8/22 19:00
@Author: Kurt
@file:utils.py
@Desc:
"""
import gurobipy as gp


class MyException(Exception):
    def __init__(self, err=None):
        self.err = err
        Exception.__init__(self, err)

def parse_results(model: gp.Model) -> None:
    objVal = model.getObjective().getValue()
    print("Get optimal Obj: {}".format(objVal))
    print("Solution:")
    for name, val in zip(model.getAttr("varName"), model.getAttr("x")):
        print("Var {}: {}".format(name, val))

    for con, val in zip(model.getAttr("constrName"), model.getAttr("Pi")):
        print("Dual var of {}: {}".format(con, val))

