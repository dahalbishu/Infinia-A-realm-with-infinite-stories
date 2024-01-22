import requests
import io
#from pydub import AudioSegment
#from IPython.display import Audio

def music(rthym):

    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    audio_bytes = query({
        "inputs": f"{rthym}",
    })

    # Save the audio bytes to a file
    input_filename = f"/home/bishu/Desktop/Infinia/Infinia/game/audio/audio.wav"
    with open(input_filename, "wb") as audio_file:
        audio_file.write(audio_bytes)
