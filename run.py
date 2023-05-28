from ssis import create_app
from dotenv import load_dotenv

app = create_app()
app.secret_key = 'your-secret-key'


if __name__ == '__main__':
    app.run()
    