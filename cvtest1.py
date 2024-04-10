import cv2
import sys

def main():
    out_filename = 'outfile.MOV'

    in_file = '/Users/yujinkwon/Documents/AILab/Videos/IMG_6558.MOV'
    vid = cv2.VideoCapture(in_file)

    #Exit if video not opened.
    if not vid.isOpened():
        print('Cannot open input video file')
        sys.exit()

    # test code
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT) 
    width  = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    print ("opencv: height:{} width:{}".format( height, width))

    # fps return 
    fps = vid.get(cv2.CAP_PROP_FPS)
    print(f"{fps} frames per second")

    retval, frame = vid.read() # ret returns true if frame is available, frame is an image array vector

    if not retval:
        print('Cannot access frame')
        sys.exit()

    cv2.imshow('image', frame)
    cv2.waitKey(0) # code crashed without this line bruh

    # while vid.isOpened():
    #     retval, frame = vid.read() # ret returns true if frame is available, frame is an image array vector

    #     if not retval:
    #         break

    #     cv2.imshow('frame', frame)

    
        
    vid.release()
    cv2.destroyAllWindows()






    
        

if __name__ == "__main__":
    main()