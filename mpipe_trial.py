import cv2
import sys
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def prep_data(in_file);
    # Use OpenCV’s VideoCapture to load the input video. 
    vid = cv2.VideoCapture(in_file)

        #Exit if video not opened.
    if not vid.isOpened():
        print('Cannot open input video file')
        sys.exit() 

    # Load the frame rate of the video using OpenCV’s CV_CAP_PROP_FPS
    # You’ll need it to calculate the timestamp for each frame.

    fps = vid.get(cv2.CAP_PROP_FPS)

    # Loop through each frame in the video using VideoCapture#read(
    while vid.isOpened():
        retval, frame = vid.read() 

        if not retval:
            print('Cannot access frame')
            sys.exit()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)



    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
    vid.release()
    cv2.destroyAllWindows()


def main():

    #personal file path for model
    model_path = '/Users/yujinkwon/Documents/AILab/Mediapipe_Models/efficientdet_lite2.tflite'
    # video file 
    in_file = '/Users/yujinkwon/Documents/AILab/Videos/IMG_6558.MOV'

    # Create the task 
    BaseOptions = mp.tasks.BaseOptions
    ObjectDetector = mp.tasks.vision.ObjectDetector
    ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # *** CHANGE THE NUMBER OF DESIRED RESULTS HERE ***
    options = ObjectDetectorOptions(
        base_options=BaseOptions(model_asset_path= model_path),
        max_results=5, 
        running_mode=VisionRunningMode.VIDEO)
    
    with ObjectDetector.create_from_options(options) as detector:
    # The detector is initialized. Use it here.
    # ...
        
if __name__ == "__main__":
    main()