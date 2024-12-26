from flask import Flask, render_template, request

app = Flask(__name__)


def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celcius":
        if to_unit == "fahrenheit":
            return(value*9/5)+32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celcius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celcius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32

@app.route('/', methods=['GET', 'POST'])

    
def index():
        result = None
        print("fungsi index")
        if request.method == "POST":
            try:
                value = float(request.form["value"])
                from_unit = request.form["from_unit"]
                to_unit = request.form["to_unit"]
                result = convert(value, from_unit, to_unit)
            except ValueError:
                result = "Invalle helaid input. coba lagi kawan!" 
        return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)