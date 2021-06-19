# Python & Excel Course Code & Materials

This repository contains the course source code and other materials like excel files.



# Run in Docker
If you have issues with installing python3 or other dependencies on your computer, you can run scripts by using docker.


as first step, you need to create an image based on the existing Dockerfile:

`docker build . --tag fardaneshpythonexcel`


and than to run a python file:

`docker run --rm -v ${PWD}/app:/app/  fardaneshpythonexcel lecture01/file1.py`

