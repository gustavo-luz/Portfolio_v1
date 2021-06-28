# Portfolio

# Clone

fork and clone https://github.com/gustavo-luz/Portfolio.git or https://github.com/CreatorGhost/Portfolio.git

# Setup

cd Portfolio
source venv/bin/activate 

if it doesn't work,try:
python3 -m venv venv

## inside venv
pip install flask

### try running
run app.py (or flask run), you should see: 

* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


### leave venv
to exit venv, type "deactivate

# Notes about
static = flask js


## background at 
/static/assets/images/image_1.jpg


# TODO


## bug
This page uses the non standard property “zoom”. Consider using calc() in the relevant property values, or using “transform” along with “transform-origin: 0 0”.

DevTools failed to load SourceMap: Could not parse content for https://gustavo-luz.herokuapp.com/static/vendor/bootstrap.min.js.map: Unexpected token < in JSON at position 0

DevTools failed to load SourceMap: Could not parse content for https://gustavo-luz.herokuapp.com/static/vendor/popper.min.js.map: Unexpected token < in JSON at position 0