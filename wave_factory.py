import numpy as np
import sounddevice as sd
import time
import tkinter as tk


def sine():
    sine_button.config(text="Wait", state="disabled")
    sine_button.update()

    duration = float(duration_scale.get())
    frequency = float(frequency_scale.get())

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    wave_data = np.sin(frequency * x)
    wave_data = wave_data * 0.3

    sd.play(wave_data, sample_rate)

    sine_button.update()
    sine_button.config(text="Sine", state="normal")


def triangle():
    triangle_button.config(text="Wait", state="disabled")
    triangle_button.update()

    duration = float(duration_scale.get())
    frequency = float(frequency_scale.get())
    
    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    wave_data = 2 / np.pi * np.arcsin(np.sin(frequency * x)) * 0.3

    sd.play(wave_data, sample_rate)

    triangle_button.update()
    triangle_button.config(text="Triangle", state="normal")
    

def sawtooth():
    saw_button.config(text="Wait", state="disabled")
    saw_button.update()

    duration = float(duration_scale.get())
    frequency = float(frequency_scale.get())

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    wave_data = -2 / np.pi * np.arctan(
            np.tan(np.pi / 2 - (x * np.pi / (1 / frequency * 2 * np.pi))))

    sd.play(wave_data*0.3, sample_rate)

    saw_button.update()
    saw_button.config(text="Sawtooth", state="normal")

def square():
    square_button.config(text="Wait", state="disabled")
    square_button.update()

    duration = float(duration_scale.get())
    frequency = float(frequency_scale.get())

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    a = np.sin(frequency * x) / 2 + 0.5
    wave_data = np.round(a) - 0.5

    sd.play(wave_data*0.3)

    square_button.update()
    square_button.config(text="Square", state="normal")

    
sample_rate = 44100

root = tk.Tk()
root.geometry('600x400')

duration_label = tk.Label(root, text="Duration")
frequency_label = tk.Label(root, text="Frequency")

duration_scale = tk.Scale(root, from_=1, to=20, resolution=1, orient=tk.HORIZONTAL)
frequency_scale = tk.Scale(root, from_=220, to=880, resolution=10, orient=tk.HORIZONTAL)

sine_button = tk.Button(root, text="Sine", command=sine)
triangle_button = tk.Button(root, text="Triangle", command=triangle)
saw_button = tk.Button(root, text="Sawtooth", command=sawtooth)
square_button = tk.Button(root, text="Square", command=square)

duration_label.grid(row=0, column=0)
frequency_label.grid(row=1, column=0)
duration_scale.grid(row=0, column=1)
frequency_scale.grid(row=1, column=1)
sine_button.grid(row=0, column=2)
triangle_button.grid(row=1, column=2)
saw_button.grid(row=2, column=2)
square_button.grid(row=3, column=2)

root.mainloop()

