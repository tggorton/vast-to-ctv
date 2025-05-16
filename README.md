# VAST to CTV Converter

A web application for converting VAST video ads to CTV-compatible format using FFmpeg.

## Features

- Upload VAST XML files
- Convert video ads to CTV-compatible format
- Preview converted videos
- Download processed files

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/vast-to-ctv-2a.git
cd vast-to-ctv-2a
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

The application will be available at `http://localhost:5002`

## Requirements

- Python 3.9+
- FFmpeg
- Flask

## Deployment

This project is configured for GitHub Pages deployment. The static assets and frontend components are served through GitHub Pages, while the backend processing can be handled through serverless functions or a separate backend service.

## License

MIT License 