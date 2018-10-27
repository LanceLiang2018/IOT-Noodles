#!/usr/bin/python
from aip import AipSpeech
class Speech():
    aipSpeech = None
    def __init__(self):
        APP_ID = '9943844'
        API_KEY = 'Blv5wLPLtvG1Dzew9ZOe06px'
        API_S = '30612e0ebe5dfe79aab72f432b9a6e0d'
        self.aipSpeech = AipSpeech(APP_ID, API_KEY, API_S)
        #Init the object
        #self.main_loop()

    #get the file buffer
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    
    def get_result(self):
        FILE_NAME = '01.wav'
        dat = self.aipSpeech.asr(self.get_file_content(FILE_NAME), 'wav', 8000, {'lan':'zh',})
        if dat['err_no'] == 0:
            return dat['result'][0]
        else:
            return None

    def save_wave_file(self,filename,data):
        import wave
        framerate=8000
        NUM_SAMPLES=2000
        channels=1
        sampwidth=2
        TIME = 2

        '''save the date to the wavfile'''
        wf=wave.open(filename,'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(b"".join(data))
        wf.close()

    def record(self):
        import os
        import wave
        from pyaudio import PyAudio,paInt16
        from pyA20.gpio import gpio
        from pyA20.gpio import port
        import time

        os.system('gpio reset')

        framerate=8000
        NUM_SAMPLES=2000
        channels=1
        sampwidth=2
        TIME = 2

        gpio.init()
        uport = port.PC7
        gpio.setcfg(uport, gpio.INPUT)
        gpio.setcfg(port.PD14, gpio.OUTPUT)
        gpio.output(port.PD14, 1)

        pa=PyAudio()
        stream=pa.open(format = paInt16,channels=1,
                       rate=framerate,input=True,
                       frames_per_buffer=NUM_SAMPLES)
        my_buf=[]
        count=0
        while gpio.input(uport) == 1:
            time.sleep(0.2)
        time.sleep(0.2)
        while gpio.input(uport) == 0:
            string_audio_data = stream.read(NUM_SAMPLES, exception_on_overflow = False)
            my_buf.append(string_audio_data)
            print('.')
        self.save_wave_file('01.wav',my_buf)
        stream.close()
        pass

    def main_loop(self):
        self.record()
        print(self.get_result())
        pass


if __name__ == '__main__':
    s = Speech()
    s.record()
    print(s.get_result())
