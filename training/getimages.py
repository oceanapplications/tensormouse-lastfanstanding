import cv2

vidcap = cv2.VideoCapture('livevideo.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  if count % 50 == 0:
  	cv2.imwrite("imgs/frame%d.jpg" % count, image)
  	pass
       # save frame as JPEG file
  count += 1