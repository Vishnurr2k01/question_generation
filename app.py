from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    return render_template('afterpost.html', data=data1)

if __name__ == "__main__":
  app.run(debug=True)