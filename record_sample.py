import pyaudio
import wave 
import tkinter as tk


def record():
    play_button.config(text='Wait', state='disabled')
    play_button.update()
    duration = float(duration_scale.get())

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    play_button.update()
    play_button.config(text='Record', state='normal')

RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024

root = tk.Tk()
root.geometry('200x150')

duration_label = tk.Label(root, text='Duration')
duration_scale = tk.Scale(root, from_=1, to=20, resolution=1, orient=tk.HORIZONTAL)
play_button = tk.Button(root, text='Record', command=record)

duration_label.grid(row=0, column=0)
duration_scale.grid(row=0, column=1)
play_button.grid(row=2, column=0)

root.mainloop()

