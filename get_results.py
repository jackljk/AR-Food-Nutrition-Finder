from ultralytics import YOLO
from PIL import Image
import io
import pandas as pd


YOLO_MODEL = YOLO("data/Best model.pt")

df = pd.read_csv("data/cleaned_data.csv")

def getNutritionInfo(image):
    # image is binary data hoew to open 
    image = Image.open(io.BytesIO(image))
    
    # save image to a file
    image.save("image.jpg")
    
    results = YOLO_MODEL(image)
    converter_dict = results[0].names
    
    out = []
    for r in results:
        predtop5 = r.probs.top5
        conftop5 = r.probs.top5conf.tolist() 
        print(r.probs.top5)
        for i, prob in enumerate(predtop5):
            print(f"Predict {i}" + " " + converter_dict[prob] + " " + str(conftop5[i] * 100))
            out.append((converter_dict[prob], conftop5[i] * 100))
    
    json_list = _getNutritionInfo(out)
    return json_list




def _getNutritionInfo(predicted_foods):
    out = []
    print(predicted_foods)
    for word, prob in predicted_foods:
        temp = {}
        # print(df[df['food_idx'] == word]['Food'].values[0])
        temp['Food'] = df[df['food_idx'] == word]['Food'].values[0]
        temp['Serving_Size'] = df[df['food_idx'] == word]['Serving Size (1 Portion)'].values[0]
        temp['Calories'] = df[df['food_idx'] == word]['Calories'].values[0]
        temp['Fat'] = df[df['food_idx'] == word]['Fat (g)'].values[0]
        temp['Protein'] = df[df['food_idx'] == word]['Protein (g)'].values[0]
        temp['Carbs'] = df[df['food_idx'] == word]['Carbs (g)'].values[0]
        temp['Sodium'] = df[df['food_idx'] == word]['Sodium (mg)'].values[0]
        temp['Potassium'] = df[df['food_idx'] == word]['Potassium (mg)'].values[0]
        temp['Predicted_Probability'] = prob
        temp['link'] = df[df['food_idx'] == word]['Source'].values[0]
        out.append(temp)

    return out