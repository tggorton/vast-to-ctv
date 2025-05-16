from flask_frozen import Freezer
from app import app
import os
import shutil
import sys

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_BASE_URL'] = 'https://tggorton.github.io/vast-to-ctv/'
app.config['FREEZER_STATIC_IGNORE'] = ['*.scss', '.DS_Store']
app.config['FREEZER_IGNORE_404_NOT_FOUND'] = True

def setup_directories():
    print("Setting up directories...")
    # Ensure build directory exists
    if not os.path.exists('build'):
        os.makedirs('build')
        print("Created build directory")

    # Ensure static directory exists in build
    if not os.path.exists('build/static'):
        os.makedirs('build/static')
        print("Created build/static directory")

    print("Directory setup complete")

@freezer.register_generator
def serve_static():
    print("Registering static routes...")
    # Ensure root route is frozen
    yield '/'
    
    # Handle static files
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            if not file.startswith('.') and file != '.DS_Store':
                rel_path = os.path.relpath(os.path.join(root, file), static_dir)
                static_url = '/static/' + rel_path
                print(f"Registered static route: {static_url}")
                yield static_url

@freezer.register_generator
def serve_generated():
    # Add any dynamic routes here
    pass

if __name__ == '__main__':
    try:
        print("Starting freeze process...")
        setup_directories()
        
        # Clean build directory
        print("Cleaning build directory...")
        if os.path.exists('build'):
            for item in os.listdir('build'):
                if item != 'static':  # Preserve static directory
                    item_path = os.path.join('build', item)
                    if os.path.isfile(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
        
        print("Starting freezer.freeze()...")
        freezer.freeze()
        print("Freeze process completed successfully")
        
        # Verify build contents
        print("\nBuild directory contents:")
        for root, dirs, files in os.walk('build'):
            for file in files:
                print(os.path.join(root, file))
                
    except Exception as e:
        print(f"Error during freeze process: {str(e)}", file=sys.stderr)
        sys.exit(1) 