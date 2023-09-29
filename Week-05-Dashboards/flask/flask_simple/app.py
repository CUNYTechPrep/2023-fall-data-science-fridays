from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
   my_text = 'Cool dude!'
   return render_template('index.html', pass_int_html=my_text)


@app.route('/rainbows')
def rainbows():
   return render_template('rainbows.html')


def make_dist():
  growing = sorted(np.random.normal(loc=100.0, scale=20.0, size=100))
  shrinking = sorted(np.random.normal(loc=100.0, scale=20.0, size=100), reverse=True)
  growing.extend(shrinking)
  growing = [int(x) for x in growing]
  return growing


@app.route('/distribution')
def distribution():
   dist = make_dist()
   return render_template('distribution.html', 
                          list_of_numbs=dist)

if __name__ == '__main__':
   app.run(debug=True, port=6969)