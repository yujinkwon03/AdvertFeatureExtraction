# https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py#L419
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from image_analysis import open_locImage, describe_image, categorize_image, detect_objects, detect_brands, detect_color, detect_faces

import cv2
import os
import json
import csv

"""
    *** NEED TO INCLUDE TAG!! ***
"""

def make_json(image_path, image_name, subscription_key, endpoint):
    # Create a client
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # # Open the image file
    # image_name = open_locImage(image_path, image_name)

    # describe image
    local_image_path, local_image = open_locImage(image_path, image_name)
    image_description = describe_image(computervision_client, local_image, True)

    # # categorize image
    # local_image_path, local_image = open_locImage(image_path, image_name)
    # categories_description = categorize_image(computervision_client, local_image)

    # detect objects
    local_image_path, local_image = open_locImage(image_path, image_name)
    objects_detected = detect_objects(computervision_client, local_image)

    # detect brands
    local_image_path, local_image = open_locImage(image_path, image_name)
    brands_detected = detect_brands(computervision_client, local_image)

    # detect color
    local_image_path, local_image = open_locImage(image_path, image_name)
    color_detected = detect_color(computervision_client, local_image)

    #detect faces
    local_image_path, local_image = open_locImage(image_path, image_name)
    faces_detected = detect_faces(computervision_client, local_image)


    combined_data = {}
    
    # image_description
    if len(image_description.captions) == 0:
        caption_data_json = 'No captions detected'
    else:
        # Initialize a list to store caption data
        caption_data = []
        for caption in image_description.captions:
            caption_info = {
                "Description": caption.text,
                "Confidence": caption.confidence
            }
            # Append caption data to the list
            caption_data.append(caption_info)

        # Convert caption_data to a JSON string
        caption_data_json = json.dumps(caption_data)
    
    print(caption_data_json)


    #object_detected
    object_data = []
    if len(objects_detected.objects) == 0:
        # print("No brands detected.")
        object_data_json = 'No objects detected'
    else:
        for object in objects_detected.objects:
            obj_name = object.object_property
            obj_location = "Object at location {}, {}, {}, {}".format(
                object.rectangle.x,
                object.rectangle.x + object.rectangle.w,
                object.rectangle.y,
                object.rectangle.y + object.rectangle.h)
                # Append object data to the list

            object_data.append({'Object_Name': obj_name, 'Object_Location': obj_location})

        object_data_json = json.dumps(object_data)
    
    print(object_data_json)

    #brands_detected
    if len(brands_detected.brands) == 0:
        # print("No brands detected.")
        brand_data_json = 'No brands detected'
    else:
        brand_data = []
        # Initialize a list to store brand data
        for brand in brands_detected.brands:
            brand_name = brand.name
            confidence = brand.confidence
            brand_location = "Brand location: {}, {}, {}, {}".format(
                brand.rectangle.x,
                brand.rectangle.x + brand.rectangle.w,
                brand.rectangle.y,
                brand.rectangle.y + brand.rectangle.h
            )

            # Append brand data to the list
            brand_data.append({'Brand_Name': brand_name, 'Confidence': confidence, 'Brand_Location': brand_location})

            # print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format(
            #     brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w,
            #     brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))

        # Convert brand_data to a JSON string
        brand_data_json = json.dumps(brand_data)
        
    print(brand_data_json)

    
    #color_detected
    color_data = {
        "Is_Black_and_White": color_detected.color.is_bw_img,
        "Accent_Color": color_detected.color.accent_color,
        "Dominant_Background_Color": color_detected.color.dominant_color_background,
        "Dominant_Foreground_Color": color_detected.color.dominant_color_foreground,
        "Dominant_Colors": color_detected.color.dominant_colors
    }

        # Convert color_data to a JSON string
    color_data_json = json.dumps(color_data)
    print(color_data_json)

    #faces_detected
    if len(faces_detected.faces) == 0:
        print("No faces detected.")
    else:
        # Initialize a list to store face data
        face_data = []
        for face in faces_detected.faces:
            face_info = {
                "Gender": face.gender,
                "Age": face.age,
                "Location": {
                    "Left": face.face_rectangle.left,
                    "Top": face.face_rectangle.top,
                    "Right": face.face_rectangle.left + face.face_rectangle.width,
                    "Bottom": face.face_rectangle.top + face.face_rectangle.height
                }
            }
            # Append face data to the list
            face_data.append(face_info)

        # Convert face_data to a JSON string
        face_data_json = json.dumps(face_data)
    
    print(face_data_json)

    return caption_data_json, object_data_json, brand_data_json, color_data_json, face_data_json
                    
    cv2.destroyAllWindows()

# def make_csv(json_list, csv_name, frame_number):
#     with open(csv_name, 'w', newline='') as file:
#         writer = csv.writer(file)
#         if file.tell() == 0:  # Check if the file is empty
#              writer.writerow(["Frame Number", "Image Description", "Object Detected", "Brand Detected", "Color Detected", "Face Detected"])
#         writer.writerow(["Frame Number", "Image Description", "Object Detected", "Brand Detected", "Color Detected", "Face Detected"])
#         writer.writerows(frame_number, json_list)

subscription_key = os.environ.get("VISION_KEY")
endpoint = os.environ.get("VISION_ENDPOINT")

make_json('/Users/yujinkwon/Documents/AILab/programs/splice_test/video_test/spliced_videos/JackDaniel.mp4_frames', 'JackDaniel.mp4_image_116.jpg', subscription_key, endpoint)