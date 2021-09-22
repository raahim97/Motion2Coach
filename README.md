# Motion2Coach

3D Pose Estimation

How to run:

- Make sure python is installed in your machine
- Launch run.sh file in the main directory
- That's all

What code do:

- Take input from default webcam OR from saved video
- if you want to run on external camera, you have to disable integrated camera from device manager (Simple solution
  without chanting of code, otherwise you have to change parameters of cv2.VideoCapture function)
- It will check if there is camera available or not
- It will start capturing images in an infinite loop (FPS depending on interpreter and CPU + Camera's Maximum FPS)
- It will process and get coordinates
- After getting the coordinates, it will put filled circles on it
- And join those circles too
- After than it will show that image in loop in a windows tittled 'Coordinates'
- It will check if windows 'Coordinates' is visible or not, if not, program will exit
- It will check that to that if input, camera, video \stopped or input ended, it will print
- At the end it will release the camera and distro windows 

Contact Information:

- RFaizanN@gmail.com
- Skype: RFaizanN