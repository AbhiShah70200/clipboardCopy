from flask import Flask, render_template, jsonify
import pyperclip
import html

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clipboard')
def clipboard():
    clipboard_text = pyperclip.paste()
    # Escape HTML characters to prevent HTML injection
    clipboard_text = html.escape(clipboard_text)
    return jsonify({'clipboard_text': clipboard_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
