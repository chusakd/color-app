from setuptools import setup

APP = ['app.py']
DATA_FILES = ['templates', 'data']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['flask'],
    'plist': {
        'CFBundleName': 'FlaskColorApp',
        'CFBundleIdentifier': 'com.example.flaskcolorapp',
        'CFBundleVersion': '0.1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
