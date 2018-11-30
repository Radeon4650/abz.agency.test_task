"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from . import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()