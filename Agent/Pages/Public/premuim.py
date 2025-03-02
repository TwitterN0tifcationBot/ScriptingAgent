from flask import Flask, render_template

app = Flask(__name__)

@app.route('/premium')
def premium():
    features = [
        "More scripting languages like JavaScript, Perl, Groovy",
        "100% working code",
        "Faster responses"
    ]
    return render_template('premium.html', features=features)

if __name__ == '__main__':
    app.run(debug=True)