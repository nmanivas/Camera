from cv2.cv import *

img = LoadImage("./image/a.jpg")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
