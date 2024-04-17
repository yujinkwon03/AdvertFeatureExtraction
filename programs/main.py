from video_splice import save_all_frames, save_onepersec_frames
from image_analysis import open_locImage, describe_image, categorize_image, detect_objects, detect_brands, detect_color, detect_faces
from csv_make import create_tuples_for_video, write_tuples_to_csv

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from dotenv import load_dotenv
from array import array
import os
from PIL import Image
import sys
import time
import cv2
import os
import re

def extract_frame_number(filename):
    """extracts frame number from filename for uid in csv"""

    pattern = r'_image_(\d+)\.jpg'

    # Find the matching pattern in the filename
    match = re.search(pattern, filename)

    # If a match is found, extract the number part
    if match:
        extracted_number = match.group(1)
        # print(extracted_number)
    else:
        print("No matching pattern found in the filename.")
    
    return extracted_number

def main():

    # splices video in dir 'video_test' into jpg frames
    # ** CHANGE dir_path TO PERSONAL DIRECTORY **

    dir_path = '/Users/yujinkwon/Documents/AILab/programs/splice_test/video_test' 
    spliced_dir = os.path.join(dir_path, 'spliced_videos')
    if os.path.exists(spliced_dir) == 0:
        os.mkdir(spliced_dir)
        for filename in os.listdir(dir_path):
            if os.path.samefile(os.path.join(dir_path, filename), spliced_dir): continue       
            video_path = os.path.join(dir_path, filename)
            save_onepersec_frames(video_path, os.path.join(spliced_dir, filename + '_frames'),  filename + '_image')

    """ 
                *** AZURE TEST IMPLEMENTATION ***
    """

    # Authenticates credentials and creates a client.
    load_dotenv()
    subscription_key = os.environ.get("VISION_KEY")
    endpoint = os.environ.get("VISION_ENDPOINT")
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

        # *** CHANGE THIS SO THAT IT IS GENERALIZABLE ***
    framesdirectory_path = '/Users/yujinkwon/Documents/AILab/programs/splice_test/video_test/spliced_videos/JackDaniel.mp4_frames'
    image_name = 'JackDaniel.mp4_image_116.jpg'
    csv_name = 'JackDaniel.csv'

    # ORGANIZE PIPELINE INTO FOLDERS!!!
    frame_tuples = create_tuples_for_video(framesdirectory_path)
    write_tuples_to_csv(frame_tuples, )

    # local_image.close()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()