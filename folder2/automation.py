import cv2
import dropbox
import time
import random

start_time=time.time()

def snapshot()
    number = random.randint(0,100)

    capture=VideoCapture(0)
    result=True
    while(result):
    ret,frame=capture.read()
    img_name = "myimage"+str(number)+".jpg"
    cv2.imwrite(img_name,frame)
    start_time=time.time
    result=False

return img_name
   
capture.release()
cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'JTrdh1m3fxcAAAAAAAAAAf1yCLzb5Xo6XQ4HzRxXWazHMS98ioC2Bgd_pxA6NvKV'
    file=img_name
    file_from = file
    file_to = "/test/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)

    # API v2
def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = snapshot()
            upload_file(name)
main()