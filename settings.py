import os
from dotenv import load_dotenv
load_dotenv()

""" A settings file is just a Python module with module-level variables."""


MODEL_NAME=os.getenv("MODEL_NAME")
NO_OF_CLUSTERS=os.getenv("NO_OF_CLUSTERS")
WORKING_DIRECTORY=os.getcwd()
TARGET_SIZE_WIDTH=int(os.getenv("TARGET_SIZE_WIDTH"))
TARGET_SIZE_HEIGHT=int(os.getenv("TARGET_SIZE_HEIGHT"))

#------------define dimensions for cropping---------    
# Setting the points for cropped image

LEFT = os.getenv("LEFT") 
TOP = os.getenv("TOP")
RIGHT = os.getenv("RIGHT")
BOTTOM =os.getenv("BOTTOM")

#---------------------------------------------------