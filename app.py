import RPi.GPIO as gpio
import getopt, sys
from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from picamera.array import PiRGBArray
import picamera
import cv2
import matplotlib.pyplot as plt
import io

cap = cv2.VideoCapture(0)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    while True:
        return(cap)

@app.route('/forward')
def forward():
    gpio.output(16, gpio.LOW)
    gpio.output(21, gpio.LOW)
    gpio.output(21, gpio.HIGH)
    gpio.output(12, gpio.HIGH)
    return redirect('/')

@app.route('/backward')
def backward():
    gpio.output(12, gpio.LOW)
    gpio.output(21, gpio.LOW)
    gpio.output(16, gpio.HIGH)
    gpio.output(20, gpio.HIGH)
    return redirect('/')

@app.route('/right')
def right():
    gpio.output(16, gpio.LOW)
    gpio.output(21, gpio.LOW)
    gpio.output(12, gpio.HIGH)
    gpio.output(20, gpio.HIGH)
    return redirect('/')

@app.route('/left')
def left():
    gpio.output(12, gpio.LOW)
    gpio.output(20, gpio.LOW)
    gpio.output(16, gpio.HIGH)
    gpio.output(21, gpio.HIGH)
    return redirect('/')

@app.route('/stop')
def stop():
    gpio.output(12, gpio.LOW)
    gpio.output(16, gpio.LOW)
    gpio.output(20, gpio.LOW)
    gpio.output(21, gpio.LOW)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host ='0.0.0.0')
    cap.release()
    cv2.destroyAllWindows()