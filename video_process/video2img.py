# encoding:UTF-8
# convert video to image
import cv2
import numpy as np
import os

def create_floders(urls):
    for dir in urls:
        os.mkdir(dir+'_npy')

if __name__=='__main__':
    url = '/home/aurora/hdd/video/'
    urls = [os.path.join(url, dir) for dir in os.listdir(url) if not 'npy' in dir]
    for video_url in urls:
        save_urls = video_url+'_npy/'
        print save_urls
        videos = [os.path.join(video_url, video) for video in os.listdir(video_url)]
        for video in videos:
            filename = video.split('/')[-1][0:-4]
            save_dir = save_urls + filename
            print save_dir,
            cap = cv2.VideoCapture(video)
            frames = []
            while True:
                ret, im = cap.read()
                # blur = cv2.GaussianBlur(im, (0, 0), 5)
                cv2.imshow('video test', im)
                frames.append(im)
                key = cv2.waitKey(10)
                if key == 1048603:
                    break
            frames = np.array(frames)
            np.save(save_dir, frames)
            # print im.shape
            print 'file shape is ', frames.shape
            cap.release()
        cv2.destroyAllWindows()
