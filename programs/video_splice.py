# https://github.com/nkmk/python-snippets/tree/c4d70389733a34250595f1c17d737ef004f2dcbd/notebook
import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    """
    Function saves all frames within video file 
    Given: 
        video_path: pathname to input video
        dir_path: path to new directory (with resulting images)
        basename: basename of resulting images
    """
    if os.path.samefile(video_path, os.path.join(os.path.split(video_path)[0], ".DS_Store")):
        return
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print('Cannot open input video file')
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            cap.release()
            return


def save_onepersec_frames(video_path, dir_path, basename, ext='jpg'):
    """
    Function saves one frame per second within video file 
    Given: 
        video_path: pathname to input video
        dir_path: path to new directory (with resulting images)
        basename: basename of resulting images
    """
    if os.path.samefile(video_path, os.path.join(os.path.split(video_path)[0], ".DS_Store")):
        return
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print('Cannot open input video file')
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()
        if ret:
            if n % int(fps) == 0:
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
            # Move to next second
            cap.set(cv2.CAP_PROP_POS_MSEC, (n / fps) * 1000)
        else:
            cap.release()
            return


# save_all_frames('data/temp/sample_video.mp4', 'data/temp/result', 'sample_video_img')

# save_all_frames('data/temp/sample_video.mp4', 'data/temp/result_png', 'sample_video_img', 'png')s