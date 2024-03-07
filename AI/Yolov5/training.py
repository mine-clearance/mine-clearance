#!/usr/bin/env python
# coding: utf-8
from roboflow import Roboflow

rf = Roboflow(api_key="Rv0kV1kuqKXU356KKkIl")
project = rf.workspace("deminage").project("infrarouge-mines")
dataset = project.version(3).download("yolov5")

print(dataset)

