# Python & Excel Course Code and Materials

This repository contains the course source code and other materials like excel files.

[Course on Youtube](https://www.youtube.com/playlist?list=PL0fWTDFODMLo4DM7j9Tqot7K0ga2Hxyee)


# Run in Docker
If you have issues with installing python3 or other dependencies on your computer, you can run scripts by using docker.


as first step, you need to create an image based on the existing Dockerfile:

`docker build . --tag fardaneshpythonexcel`


and than to run a python file:

`docker run --rm -v ${PWD}/app:/app/  fardaneshpythonexcel lecture01/file1.py`

