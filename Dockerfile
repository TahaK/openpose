FROM tahak/caffe 
# start with the nvidia container for cuda 8 with cudnn 6

LABEL maintainer "Mustafa Taha Kocyigit <taha.kocyigit@gmail.com>"

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget unzip lsof apt-utils lsb-core -y
RUN apt-get install libatlas-base-dev -y
RUN apt-get install libopencv-dev python-opencv python-pip -y   

COPY . /openpose

WORKDIR /openpose

RUN cp ubuntu/Makefile.example Makefile && \ 
    cp ubuntu/Makefile.config.Ubuntu16_cuda8.example Makefile.config && \
    make all -j"$(nproc)"

RUN bash models/getModels.sh

CMD [ "python" , "script.py" ]