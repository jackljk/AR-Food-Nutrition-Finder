from ultralytics import YOLO
from PIL import Image
import io



YOLO_MODEL = YOLO("Best model.pt")



def getNutritionInfo(image):
    # image is binary data hoew to open 
    image = Image.open(io.BytesIO(image))
    
    # save image to a file
    image.save("image.jpg")
    
    results = YOLO_MODEL(image)
    converter_dict = results[0].names
    
    out = []
    for r in results:
        probtop5 = r.probs.top5
        for i, prob in enumerate(probtop5):
            # TODO: replace with getting the nutrition info
            print(f"Predict {i}" + " " + converter_dict[prob] + " " + str(prob))
            out.append(f"Predict {i}" + " " + converter_dict[prob] + " " + str(prob))
    
    
    return out[0]