import pyaudio
import wave
import tkinter as tk


def play():
    play_button.config(text='Wait', state='disabled')
    play_button.update()

    wf = wave.open('output.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

    play_button.update()
    play_button.config(text='Play', state='normal')

CHUNK = 1024

root = tk.Tk()

root.geometry('150x150')

play_button = tk.Button(root, text="Play", command=play)

play_button.grid(row=1, column=1)

root.mainloop()


