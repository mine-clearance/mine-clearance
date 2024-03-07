from roboflow import Roboflow

rf = Roboflow(api_key="Rv0kV1kuqKXU356KKkIl")

'''
------------------------------------------------------------------
Projet sur le dataset avec les fausses mines remplies de charbon / images vision thermique : 
https://www.sciencedirect.com/science/article/pii/S2352340923005437
------------------------------------------------------------------
'''
project = rf.workspace().project("infrarouge-mines")
model = project.version(3).model

# infer on a local image
print(model.predict("AI\\Yolov5\\data\\input\\test_mine9m.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("AI\\Yolov5\\data\\input\\test_mine9m.jpg", confidence=40, overlap=30).save("AI\\Yolov5\\data\\output\\prediction_9m.jpg")

'''
------------------------------------------------------------------
Projet sur le dataset avec les PFM-1 / images vision thermique : 
https://universe.roboflow.com/mineguard/mineguard-thermal-hnhpg/dataset/1
------------------------------------------------------------------
'''
project = rf.workspace().project("mineguard-thermal-hnhpg")
model = project.version(1).model

# infer on a local image
print(model.predict("AI\\Yolov5\\data\\input\\MARK_3_158_png.rf.0a4c6989ee9888e51ae6b4d8025ead57.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("AI\\Yolov5\\data\\input\\MARK_3_158_png.rf.0a4c6989ee9888e51ae6b4d8025ead57.jpg", confidence=40, overlap=30).save("AI\\Yolov5\\data\\output\\prediction_PFM-1.jpg")

