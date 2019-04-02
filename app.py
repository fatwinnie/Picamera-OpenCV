from flask import Flask, render_template, Response
from VideoCV import VideoCamera
import time

app = Flask(__name__)
vc = cv2.VideoCapture(0)

@app.route("/")
def index():
	"""Main page."""	
	return render_template('index.html')

@app.route('/photo')
def photo():
	""" take a photo """
	return render_template('photo.html')

@app.route('/get-pic')
def CameraPic():  
	camera = PiCamera()
	camera.hflip=True
	camera.vflip=True
	camera.start_preview()
	time.sleep(3)
	filename='/static/image/test2.jpg'		
	camera.capture('/home/pi/camWebServer2/static/image/test2.jpg')
	camera.close()
	return 'http://1.1.1.34:5000'+ filename

	

@app.route('/camera')
def cam():
	"""Video streaming home page."""
	#timeNow = time.asctime( time.localtime(time.time()) )
	#templateData = {time: timeNow}
	return render_template('camera.html')

def gen(VideoCV):
    """Video streaming generator function."""
    while True:
		frame=VideoCV.get_frame()	
		 yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='1.1.1.34', port=5050, debug=True, threaded=True)
