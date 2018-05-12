import os
from flask import *
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static' #folder where the uploaded files go
ALLOWED_EXTENSIONS = set(['txt']) #put your allowed file entensions here

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials'
		else:
			return redirect(url_for('admin'))
	return render_template('login.html', error=error)

@app.route("/pydoor", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
