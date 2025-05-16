from flask_frozen import Freezer
from app import app

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_BASE_URL'] = 'https://tggorton.github.io/vast-to-ctv/'

@freezer.register_generator
def serve_static():
    yield '/'  # Ensure root route is frozen
    yield '/static/css/style.css'
    yield '/static/images/kerv-logo.png'

@freezer.register_generator
def serve_generated():
    # Add any dynamic routes here
    pass

if __name__ == '__main__':
    freezer.freeze() 