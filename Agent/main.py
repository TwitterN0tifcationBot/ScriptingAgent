from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to the Scripting Agent</h1>
        <form action="/run" method="post">
            <textarea name="code" rows="10" cols="30"></textarea><br>
            <input type="submit" value="Run Code">
        </form>
    ''')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    try:
        # Save the code to a temporary file
        with open('temp_script.py', 'w') as f:
            f.write(code)
        
        # Run the code and capture the output
        result = subprocess.run(['python', 'temp_script.py'], capture_output=True, text=True)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    
    return render_template_string('''
        <h1>Code Output</h1>
        <pre>{{ output }}</pre>
        <a href="/">Go Back</a>
    ''', output=output)

if __name__ == '__main__':
    app.run(debug=True)