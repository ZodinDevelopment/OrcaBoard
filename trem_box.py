import pyaudio
import numpy as np
import sounddevice as sd
import wave
import time
import scipy.io.wavfile as wf
import tkinter as tk


def record():
    record_button.config(text="Wait", state="disabled")
    record_button.update()
    
    duration = float(duration_scale.get())
    #factor = float(factor_scale.get())
    #trem_freq = float(tremolo_scale.get())

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=2,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(sample_rate / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wav = wave.open('output.wav', 'wb')
    wav.setnchannels(2)
    wav.setsampwidth(p.get_sample_size(FORMAT))
    wav.setframerate(sample_rate)
    wav.writeframes(b''.join(frames))
    wav.close()

    record_button.update()
    record_button.config(text="Record", state="normal")

def tremolo():
    play_button.config(text="Wait", state="disabled")
    play_button.update()
    
    factor = float(factor_scale.get())
    trem_freq = float(tremolo_scale.get())


    rate, data = wf.read('output.wav')
    data0 = data[:, 0]

    sound = data0[:190000]

    duration = len(sound) / rate

    x = np.linspace(0, duration * 2 * np.pi, len(sound))
    tremolo_osc = np.sin(trem_freq * x)
    tremolo_osc = (tremolo_osc * factor / 2 + (1 - factor / 2))

    result = sound * tremolo_osc * 0.5

    result = np.int16(result)

    sd.play(result, sample_rate)
    time.sleep(duration)
    sd.stop()

    play_button.update()
    play_button.config(text="Play", state="normal")

sample_rate = 44100
FORMAT = pyaudio.paInt16
CHUNK = 1024

root = tk.Tk()
root.geometry('600x400')

duration_label = tk.Label(root, text="Duration")
factor_label = tk.Label(root, text="Factor")
frequency_label = tk.Label(root, text="Trem Frequency")

duration_scale = tk.Scale(root, from_=1, to=20, resolution=1, orient=tk.HORIZONTAL)
factor_scale = tk.Scale(root, from_=0.5, to=5, resolution=0.2, orient=tk.HORIZONTAL)
tremolo_scale = tk.Scale(root, from_=5, to=20, resolution=1, orient=tk.HORIZONTAL)

record_button = tk.Button(root, text="Record", command=record)
play_button = tk.Button(root, text="Play", command=tremolo)

duration_label.grid(row=0, column=0)
factor_label.grid(row=1, column=0)
frequency_label.grid(row=2, column=0)
duration_scale.grid(row=0, column=2)
factor_scale.grid(row=1, column=2)
tremolo_scale.grid(row=2, column=2)

record_button.grid(row=0, column=3)
play_button.grid(row=2, column=3)

root.mainloop()

