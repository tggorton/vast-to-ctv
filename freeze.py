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
app.config['FREEZER_SKIP_EXISTING'] = True

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

    # Ensure generated and uploads directories exist in build
    if not os.path.exists('build/generated'):
        os.makedirs('build/generated')
        print("Created build/generated directory")
    
    if not os.path.exists('build/uploads'):
        os.makedirs('build/uploads')
        print("Created build/uploads directory")

    print("Directory setup complete")

@freezer.register_generator
def index():
    yield {}  # Just yield the root route

@freezer.register_generator
def generated_file():
    # This is just for the static site, so we don't need to yield anything
    return []

@freezer.register_generator
def serve_static():
    print("Registering static routes...")
    # Handle static files
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            if not file.startswith('.') and file != '.DS_Store':
                rel_path = os.path.relpath(os.path.join(root, file), static_dir)
                static_url = '/static/' + rel_path
                print(f"Registered static route: {static_url}")
                yield static_url

if __name__ == '__main__':
    try:
        print("Starting freeze process...")
        setup_directories()
        
        # Clean build directory
        print("Cleaning build directory...")
        if os.path.exists('build'):
            for item in os.listdir('build'):
                if item not in ['static', 'generated', 'uploads']:  # Preserve these directories
                    item_path = os.path.join('build', item)
                    if os.path.isfile(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
        
        print("Starting freezer.freeze()...")
        freezer.freeze()
        print("Freeze process completed successfully")
        
        # Copy necessary static files
        print("\nCopying static files...")
        if os.path.exists('static'):
            if not os.path.exists('build/static'):
                os.makedirs('build/static')
            for item in os.listdir('static'):
                src = os.path.join('static', item)
                dst = os.path.join('build/static', item)
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
        
        # Verify build contents
        print("\nBuild directory contents:")
        for root, dirs, files in os.walk('build'):
            level = root.replace('build', '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
                
    except Exception as e:
        print(f"Error during freeze process: {str(e)}", file=sys.stderr)
        sys.exit(1) 