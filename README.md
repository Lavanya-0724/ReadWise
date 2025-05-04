# BookWise - Book Recommendation System

A Flask-based web application that provides personalized book recommendations based on user preferences.

## Features

- Personalized book recommendations
- Popular books display
- Modern and responsive UI
- Case-insensitive book search

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open http://localhost:5000 in your browser

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy!

## Project Structure

```
.
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── runtime.txt        # Python version specification
├── Procfile           # Process file for Render
├── templates/         # HTML templates
│   ├── index.html    # Home page
│   └── recommend.html # Recommendation page
└── static/           # Static files (CSS, JS, images)
```

## Data Files

The following pickle files are required for the application to run:

- popular.pkl
- pt.pkl
- books.pkl
- similarity_scores.pkl

Make sure these files are present in the root directory before running the application.

## License

This project is licensed under the MIT License.
