import cv2
import imutils

#initalizing HOG person Detector 

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 


cap = cv2.VideoCapture('ped.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)


width = int(cap.get(3))
height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
size = (width,height)
    
out = cv2.VideoWriter("result.avi",fourcc,fps,size)
count = 0

while True:
    
    ret,image = cap.read()
    
    if ret:
        count += 1
        print(count)
        image= imutils.resize(image,width = min(400,image.shape[1]))
        
        (regions, _) = hog.detectMultiScale(image,   winStride=(4, 4), padding=(4, 4), scale=1.05) 
        
        for (x, y, w, h) in regions: 
            cv2.rectangle(image, (x, y), (x + w, y + h),   (0, 0, 255), 2) 
            
        
        out.write(image)
        cv2.imwrite('frames/{}.jpg'.format(count),image)
        
        # if cv2.waitKey(1) & 0xFF == ord('q'): 
        #     break
        
    else:
        break
    
cap.release() 
out.release()
cv2.destroyAllWindows()
            
        
   
   
        