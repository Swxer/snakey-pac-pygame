"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['TheSnakeyPac.py']
DATA_FILES = ['pac1.png','bacteria.png','zipzap.png','pacbody.png','yummy.wav']
OPTIONS = {"packages":["pygame"],"iconfile":"zipzap.icns"}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
