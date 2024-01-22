import requests
import io
from PIL import Image
import random
import os

def rajat(place,ii):
    file_path = f"/home/bishu/Desktop/Infinia/Infinia/game/images/bishe{ii}.png"

    try:
        os.remove(file_path)
    except:
        pass



    #API_URL = "https://api-inference.huggingface.co/models/Nazaninmnd/DreamBooth_DC"
    #API_URL = "https://api-inference.huggingface.co/models/SimianLuo/LCM_Dreamshaper_v7"
    API_URL = "https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration"
    #API_URL = "https://api-inference.huggingface.co/models/dalle2/dreamweddingbooth"
    #API_URL = "https://api-inference.huggingface.co/models/Lykon/dreamshaper-8"
    #API_URL = "https://api-inference.huggingface.co/models/digiplay/AbsoluteReality_v1.8.1"
    #API_URL = "https://api-inference.huggingface.co/models/Lykon/absolute-reality-1.81"


    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response
    #print(place)
    image_response = query({
        "inputs": f"{place}"
    })

    # Check if the response is successful (status code 200) and contains image data
    if image_response.status_code == 200 and image_response.headers.get('Content-Type', '').startswith('image'):
        # Access the image with PIL.Image
        image = Image.open(io.BytesIO(image_response.content))

        # Resize the image to 1920 by 1080 pixels
        new_size = (1920, 1080)
        resized_image = image.resize(new_size)

        # Save the resized image
        loc = "/home/bishu/Desktop/Infinia/Infinia/game/images"
        resized_image.save(f"/home/bishu/Desktop/Infinia/Infinia/game/images/bishe{ii+1}.png")
    # else:
    #     print(f"Error: {image_response.status_code}, {image_response.text}")
    ii=ii+1
    return ii
