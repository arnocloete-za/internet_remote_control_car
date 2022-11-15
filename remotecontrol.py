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


@app.route('/')
def index():
    return render_template('web.html')

@app.route('/forward_begin')
def forward_begin_function():
    print("PRESS: forward_begin")
    rpi.output(forward_start,1)
    rpi.output(forward,1)
    time.sleep(0.05)
    rpi.output(forward_start,0)
    return render_template('web.html')

@app.route('/forward_end')
def forward_end_function():
    print("PRESS: forward_end")
    rpi.output(forward,0)
    rpi.output(forward_start,0)
    return render_template('web.html')

@app.route('/reverse_begin')
def reverse_begin_function():
    print("PRESS: reverse_begin")
    rpi.output(reverse,1)
    time.sleep(0.5)
    rpi.output(reverse,0)
    return render_template('web.html')

@app.route('/reverse_end')
def reverse_end_function():
    print("PRESS: reverse_end")
    # just going to tap reverse (above) for quick reverse to get out of trouble
    return render_template('web.html')

@app.route('/left_begin')
def left_begin_function():
    print("PRESS: left_begin")
    rpi.output(left,1)
    #time.sleep(1)
    #rpi.output(left,0)
    return render_template('web.html')

@app.route('/left_end')
def left_end_function():
    print("PRESS: left_end")
    rpi.output(left,0)
    return render_template('web.html')

@app.route('/right_begin')
def right_begin_function():
    print("PRESS: right_begin")
    rpi.output(right,1)
    #time.sleep(1)
    #rpi.output(right,0)
    return render_template('web.html')

@app.route('/right_end')
def right_end_function():
    print("PRESS: right_end")
    rpi.output(right,0)
    return render_template('web.html')

#@app.route("/forward", methods=['POST'])
#def forward_function():
#    print("FORWARD")
#    return render_template('web.html')


if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='127.0.0.1')

