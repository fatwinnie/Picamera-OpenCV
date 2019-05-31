import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the video stream.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #roi= gray[100:300,150:350]        
        ret, jpeg = cv2.imencode('.jpg', roi)
        return jpeg.tobytes()
