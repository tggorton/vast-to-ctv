from flask_frozen import Freezer
from app import app
import os

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_BASE_URL'] = 'https://tggorton.github.io/vast-to-ctv/'
app.config['FREEZER_STATIC_IGNORE'] = ['*.scss']

@freezer.register_generator
def serve_static():
    # Ensure root route is frozen
    yield '/'
    
    # Handle static files
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            if not file.startswith('.') and file != '.DS_Store':
                rel_path = os.path.relpath(os.path.join(root, file), static_dir)
                yield '/static/' + rel_path

@freezer.register_generator
def serve_generated():
    # Add any dynamic routes here
    pass

if __name__ == '__main__':
    freezer.freeze() 