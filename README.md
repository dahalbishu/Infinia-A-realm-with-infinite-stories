# Infinia: A Realm with Infinite Stories
Welcome to Infinia, an innovative game where players can shape their own stories by making choices that dynamically influence the narrative. What sets Infinia apart is its use of AI-generated content, including storylines, images, and music, ensuring a truly infinite and unique experience with each playthrough.

# Getting Started

## Prerequisites
Download Ren'Py from the official website.
Ensure you have Python 3.9 installed.

# Setup for Linux and MAC
Navigate to the Ren'Py SDK folder (version number may vary, e.g., renpy-8.1.3-sdk).

Copy video_gen.py and music_gen.py into the Ren'Py SDK folder.

Edit video_gen.py and music_gen.py to set file paths according to your system.

Download the Python 3.9 folder from the provided Google Drive link ( https://drive.google.com/drive/folders/1S0POsKfCEo7ZZeEcYvnom6fUdtMGI9tI?usp=drive_link ).

Replace the existing lib/python3.9 folder in the Ren'Py SDK directory with the downloaded one. Note: This folder contains necessary Python packages; adjust them as needed.

## Alternative Setup
If encountering package errors, follow these steps:

Create a new conda environment.
Install the required Python packages: google-generativeai, pillow, and other necessary libraries.
Copy the lib/python3.9 folder from the conda environment to the Ren'Py SDK.

## Hugging Face API Key Replacement
Open video_gen.py and music_gen.py in the Ren'Py SDK folder.
Replace "HUGGING_FACE_API_KEY" with your actual Hugging Face API key.

## Google GenerativeAI API Key Replacement
Open game/script.rpy in your project folder.
Replace "GOOGLE_GENERATIVEAI_API_KEY" with your actual Google GenerativeAI API key.

Save changes to ensure correct API key configuration.

# Running the Game
Create a new project named 'Infinia' and place all files and folders inside it.
navigate to Ren'Py SDK folder
Run ./renpy.sh.
Select 'Infinia'.
Launch the project.
Start the game and enjoy the infinite possibilities of storytelling.

# Demo Video
Explore a demo video showcasing Infinia on our Google Drive ( https://drive.google.com/drive/folders/1S0POsKfCEo7ZZeEcYvnom6fUdtMGI9tI?usp=drive_link ).

Feel free to contribute, report issues, or share your experience with us!

Disclaimer: Please note that this project might be subject to updates and changes. Always refer to the latest documentation for accurate information.
