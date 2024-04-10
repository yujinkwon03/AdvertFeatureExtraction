from video_splice import save_all_frames, save_onepersec_frames
from image_analysis import open_locImage, describe_image, categorize_image, detect_objects, detect_brands, detect_color, detect_faces

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
    imagelocal_path = '/Users/yujinkwon/Documents/AILab/programs/splice_test/video_test/spliced_videos/JackDaniel.mp4_frames'
    image_name = 'JackDaniel.mp4_image_116.jpg'

    # 

    extract_frame_number(image_name)

    # describe image
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    image_description = describe_image(computervision_client, local_image, True)

    # categorize image
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    categories_description = categorize_image(computervision_client, local_image)

    # detect objects
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    objects_detected = detect_objects(computervision_client, local_image)

    # detect brands
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    brands_detected = detect_brands(computervision_client, local_image)

    # detect color
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    color_detected = detect_color(computervision_client, local_image)

    #detect faces
    local_image_path, local_image = open_locImage(imagelocal_path, image_name)
    faces_detected = detect_faces(computervision_client, local_image)

    print(faces_detected)

    # local_image.close()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()