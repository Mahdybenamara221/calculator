from flask import Flask, request,  render_template

app = Flask(__name__)

def calculator(x,y,operation):

  if (x.isnumeric() & y.isnumeric()):
    x=float(x)
    y=float(y)
    if operation == "+":
      result = x + y
    elif operation == "-":
      result = x - y
    elif operation == "/":
      result = x / y
    elif operation == "*":
      result = x * y
    else:
      result = "Operational Error"
    
  else:
    result = "Please enter valid numbers"
    

  return result


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])



def calculate():

    x = request.form['x']
    y = request.form['y']
    operation = str(request.form['operation'])

    result = calculator(x,y,operation)

    return render_template('index.html', results=str(result))


if __name__ == "__main__":
    app.run(debug=True)



