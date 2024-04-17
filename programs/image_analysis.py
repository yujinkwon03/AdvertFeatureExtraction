# https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py#L419
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

def open_locImage(images_folder, image):
    """
    Opens local image and returns path of local image
    Given: 
        iamges_ folder: pathname of folder containing image
        image: str image name 
    Returns:
        local_image_path: local image PATH 
        local_image: local iamge
    
    *** DONT FORGET TO CLOSE local_image ***
    """
    local_image_path = os.path.join (images_folder, image)
    local_image = open(local_image_path, "rb")
    return local_image_path, local_image

def describe_image(computervision_client, image, is_local):
    """
    gives brief desciption of image
    Given: 
        computervision_cliet: client intiialized from main file
        image: image file (local)
        is_local: bool describes local or not
    Returns:
        description_result: object with result
    """
    
    description_result = computervision_client.describe_image_in_stream(image)

    # print("===== Describe an Image - local =====")
    # if (len(description_result.captions) == 0):
    #     print("No description detected.")
    # else:
    #     for caption in description_result.captions:
    #         print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
    # print()

    return description_result

def categorize_image(computervision_client, image):
    """
    categorize images into 
    Given: 
        computervision_cliet: client intiialized from main file
        image: image file (local)
        is_local: bool describes local or not
    Returns:
        description_result: object with result
    """
    # print("===== Categorize an Image - local =====")
    
    # Select visual feature type(s)
    local_image_features = ["categories"]

    # Call API
    categorize_results_local = computervision_client.analyze_image_in_stream(image, local_image_features)

    # # Print category results with confidence score
    # print("Categories from local image: ")

    # if (len(categorize_results_local.categories) == 0):
    #     print("No categories detected.")
    # else:
    #     for category in categorize_results_local.categories:
    #         print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
    # print()

    return categorize_results_local

def detect_objects(computervision_client, image):
    """
    Detects objects in image
    Given: 
        computervision_cliet: client intiialized from main file
        image: image file (local)
    Returns:
        detect_objects_results_local: object with result
    """
    # Detect objects
    detect_objects_results_local = computervision_client.detect_objects_in_stream(image)

    # # Print results of detection with bounding boxes
    # print("Detecting objects in local image:")
    # if len(detect_objects_results_local.objects) == 0:
    #     print("No objects detected.")
    # else:
    #     for object in detect_objects_results_local.objects:
    #         obj_name =object.object_property
    #         print(obj_name)
    #         print( "Object at location {}, {}, {}, {}".format( \
    #         object.rectangle.x, object.rectangle.x + object.rectangle.w, \
    #         object.rectangle.y, object.rectangle.y + object.rectangle.h))
    # print()

    return detect_objects_results_local

def detect_brands(computervision_client, image):
    # Select the visual feature(s) you want
    local_image_features = ["brands"]
    # Call API with image and features
    detect_brands_results_local = computervision_client.analyze_image_in_stream(image, local_image_features)

    # # Print detection results with bounding box and confidence score
    # print("Detecting brands in local image: ")
    # if len(detect_brands_results_local.brands) == 0:
    #     print("No brands detected.")


    # else:
    #     for brand in detect_brands_results_local.brands:
    #         print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
    #         brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
    #         brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))
    # print()

    return detect_brands_results_local

def detect_color(computervision_client, image):
    print("===== Detect Color - local =====")
    # Select visual feature(s) you want
    local_image_features = ["color"]
    # Call API with local image and features
    detect_color_results_local = computervision_client.analyze_image_in_stream(image, local_image_features)

    # # Print results of the color scheme detected
    # print("Getting color scheme of the local image: ")
    # print("Is black and white: {}".format(detect_color_results_local.color.is_bw_img))
    # print("Accent color: {}".format(detect_color_results_local.color.accent_color))
    # print("Dominant background color: {}".format(detect_color_results_local.color.dominant_color_background))
    # print("Dominant foreground color: {}".format(detect_color_results_local.color.dominant_color_foreground))
    # print("Dominant colors: {}".format(detect_color_results_local.color.dominant_colors))
    # print()

    return detect_color_results_local

def detect_faces(computervision_client, image):
    print("===== Detect Faces - local =====")
    # Detect a face in an image that contains a single face
    # Call the API with a local image
    local_image_features = ["faces"]

    # Call the API with a local image
    detect_faces_results_local = computervision_client.analyze_image_in_stream(image, local_image_features)
   
    # # Print results with confidence score
    # print("Faces in the local image: ")
    # if (len(detect_faces_results_local.faces) == 0):
    #     print("No faces detected.")
    # else:
    #     for face in detect_faces_results_local.faces:
    #         print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
    #         face.face_rectangle.left, face.face_rectangle.top, \
    #         face.face_rectangle.left + face.face_rectangle.width, \
    #         face.face_rectangle.top + face.face_rectangle.height))
    # print()

    return detect_faces_results_local

