from flask import Flask
from jinja2Template import jinja2Template

app = Flask(__name__)
app.register_blueprint(jinja2Template, url_prefix='/jinja2')

@app.route('/', methods=['GET','POST'])
def index():
	return """
	<!DOCTYPE html><html><body>

<a href="jinja2/">jinja2</a><br>

</body></html>
	""" 

if __name__=="__main__":
	  app.run("0.0.0.0",port = 6003,debug=False)