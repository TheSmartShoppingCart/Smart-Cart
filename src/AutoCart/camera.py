from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import time

class Camera:
    def __init__(self):
        self.dispW = 1280
        self.dispH = 720
        self.count = 0
        self.piCam = Picamera2()
        self.encoder = H264Encoder(bitrate=10000000) 
    
    def setup(self):
        self.piCam.preview_configuration.main.size = (dispW, dispH)
        self.piCam.preview_configuration.main.format = "RGB888"
        self.piCam.preview_configuration.align()
        self.piCam.configure("preview")
        self.piCam.start()

    def wait(self):
        self.piCam.wait_recording(5) # 5 seconds

    def startRecording(self):
        # LED On
        self.count = self.count + 1
        self.piCam.start_recording(self.encoder, '/home/pi/Desktop/recording/video'+ str(self.count) + '.h264')
    

    def stopRecording(self):
        self.piCam.stop_recording() 
        # LED Off


camera = Camera()

while True:
    
    try: 
        time.sleep(0.1) 
    
        camera.startRecording()
        print('Start Recording')
        
        time.sleep(5)
        print('Recording for 5 sec')
    
        camera.stopRecording()
        print('Stop Recording')
    
    except KeyboardInterrupt:
        print("Interrupted. ABORT")
        break
    
    