from roboflow import Roboflow

rf = Roboflow(api_key="Rv0kV1kuqKXU356KKkIl")

project = rf.workspace().project("infrarouge-mines")
model = project.version(3).model

# infer on a local image
print(model.predict("AI\\Yolov5\\data\\input\\test_mine9m.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("AI\\Yolov5\\data\\input\\test_mine9m.jpg", confidence=40, overlap=30).save("AI\\Yolov5\\data\\output\\prediction_9m.jpg")