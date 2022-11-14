from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time

app= Flask(__name__)

forward_start,forward,reverse= 3,5,7
left, right= 16,18


rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(forward_start, rpi.OUT)
rpi.setup(forward, rpi.OUT)
rpi.setup(reverse, rpi.OUT)
rpi.setup(left, rpi.OUT)
rpi.setup(right, rpi.OUT)


rpi.output(forward_start, 0)
rpi.output(forward, 0)
rpi.output(reverse, 0)
rpi.output(left, 0)
rpi.output(right, 0)
print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/FORWARD')
def forward_funciton():
    rpi.output(forward_start,1)
    rpi.output(forward,1)
    time.sleep(0.05)
    rpi.output(forward_start,0)
    return render_template('webpage.html')

@app.route('/NOT_FORWARD')
def not_forward_function():
    rpi.output(forward,0)
    rpi.output(forward_start,0)
    return render_template('webpage.html')
    
@app.route('/REVERSE')
def reverse_funciton():
    rpi.output(reverse,1)    
    time.sleep(0.5)
    rpi.output(reverse,0)
    return render_template('webpage.html')


@app.route('/LEFT')
def left_function():
    rpi.output(left,1)
    time.sleep(1)
    rpi.output(left,0)
    return render_template('webpage.html')

@app.route('/RIGHT')
def right_function():
    rpi.output(right,1)
    time.sleep(1)
    rpi.output(right,0)
    return render_template('webpage.html')



if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='127.0.0.1')
