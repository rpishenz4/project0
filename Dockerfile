FROM ubuntu:latest
RUN apt update && apt install -y python3 python3-pip git ffmpeg libsm6 libxext6 
RUN pip install SpeechRecognition
RUN apt-get install -y python3-pyaudio 
RUN pip install PyAudio
RUN pip install pywhatkit
RUN pip install pygobject
RUN pip install playsound
RUN pip install gTTS
RUN git clone https://github.com/rpishenz4/project0.git 
CMD cd project0; python3 main.py