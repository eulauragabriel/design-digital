from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def insira():
    return render_template("form.html")

@app.route('/formula', methods=['POST', 'GET'])
def formula():
    if request.method == 'POST':
        x = int(request.form['x'])
        y = int(request.form['y'])
        z = int(request.form['z'])
        w = x - y
        return str(f'Você fez/fará {z - x} anos em {z}, seu colega fez/fará {z - y} anos em {z} e vocês possuem {abs(w)} ano(s) de diferença!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)