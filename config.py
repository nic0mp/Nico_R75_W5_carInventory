import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in any OS we find ourslves in
# Allow outside files/folders to be added to the project
# base directory

class Config():
    """
        Set Config variables for the flask app.
        Using Environment vvaiales where available
        create config variables if not done already
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False