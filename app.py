from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

@app.route('/questions-generated', methods=['POST'])
def home():
    if request.method == 'POST':
      if request.form['generate']:
        data = request.form['a']
        list=[{'answer': 'Robert Zemeckis', 'question': 'Who directed Forrest Gump?'},
 {'answer': 'Eric Roth', 'question': 'Who wrote Forrest Gump?'},
 {'answer': '1986',
  'question': "In what year was Winston Groom's novel published?"},
 {'answer': 'Alabama', 'question': 'Where is Forrest Gump from?'},
 {'answer': 'differs substantially from the novel',
  'question': 'How does Forrest Gump compare to the novel?'}]
        return render_template('answer.html', data=list)
    else:
      return    

if __name__ == "__main__":
  app.run(debug=True)