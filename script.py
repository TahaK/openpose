import glob
import os
import subprocess
from random import shuffle

video_list = [os.path.basename(x)[:-4] for x in glob.glob("/data/videos_mp4/*.mp4")]
shuffle(video_list)
processed_list = [os.path.basename(x)[:-4] for x in glob.glob("/data/output2D/*.avi")]
print(len(processed_list))
for video in video_list:
    processed_list = [os.path.basename(x)[:-4] for x in glob.glob("/data/output2D/*.avi")]
    if(video not in processed_list):
        bashCommand = "mkdir /data/output2D/{}_poses".format(video)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        bashCommand = "./build/examples/openpose/openpose.bin --video /data/videos_mp4/{}.mp4 --write_video /data/output2D/{}.avi --write_keypoint_json /data/output2D/{}_poses --no_display --num_gpu 2".format(video,video,video)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(bashCommand)
