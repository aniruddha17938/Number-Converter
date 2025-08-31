from flask import Flask, render_template, request

app = Flask(__name__)

def convert_number(value, base):
    try:
        number = int(value, base)
        return {
            "decimal": str(number),
            "binary": bin(number)[2:],
            "octal": oct(number)[2:],
            "hexadecimal": hex(number)[2:].upper()
        }
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_value = ''
    input_base = '10'

    if request.method == 'POST':
        input_value = request.form['number']
        input_base = request.form['base']
        result = convert_number(input_value, int(input_base))

    return render_template('index.html', result=result, input_value=input_value, input_base=input_base)

if __name__ == '__main__':
    app.run(debug=True)
