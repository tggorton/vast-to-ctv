from flask_frozen import Freezer
from app import app

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_BASE_URL'] = 'https://tggorton.github.io/vast-to-ctv/'

@freezer.register_generator
def static_files():
    # Ensure static files are copied
    yield '/static/css/style.css'
    yield '/static/images/kerv-logo.png'
    # Add any other static files your app uses

if __name__ == '__main__':
    freezer.freeze() 