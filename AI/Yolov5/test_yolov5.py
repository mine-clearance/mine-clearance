# import a utility function for loading Roboflow models
from inference import get_roboflow_model

# define the image url to use for inference
image = "AI\\Yolov5\\data\\input\\test_mine9m.jpg"

# load a pre-trained yolov8n model
model = get_roboflow_model(model_id="taylor-swift-records/3",api_key="Rv0kV1kuqKXU356KKkIl")

# run inference on our chosen image, image can be a url, a numpy array, a PIL image, etc.
results = model.infer(image)