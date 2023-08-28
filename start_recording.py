import time
import picamera
import os

def get_next_filename(base_path):
    sequence_number = 1
    while True:
        filename = f'{base_path}_test{sequence_number}.h264'
        if not os.path.exists(filename):
            return filename
        sequence_number += 1

def main():
    base_filename = '/path/to/save/Videos'
    
    # Initialize the camera
    with picamera.PiCamera() as camera:
        # Set desired resolution 
        camera.resolution = (640, 480)
        
        # Start recording
        output_filename = get_next_filename(base_filename)
        camera.start_recording(output_filename)
        # Record for 18 seconds
        camera.wait_recording(18)
        # Stop recording
        camera.stop_recording()

if __name__ == '__main__':
    main()	
