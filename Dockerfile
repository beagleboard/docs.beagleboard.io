FROM python:3.9-alpine as sphinx-build-env
RUN apk update
RUN python -m pip install --upgrade pip
RUN pip install -U sphinx
RUN pip install -U sphinx_design
RUN pip install sphinxcontrib-svg2pdfconverter
RUN apk add librsvg
RUN pip install sphinx_rtd_theme
RUN apk add texlive-full
RUN apk add make
RUN apk add rsync
RUN apk add git
