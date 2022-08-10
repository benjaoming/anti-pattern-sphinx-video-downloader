# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import requests
import shutil


project = 'This is an anti-pattern'
copyright = '2022, Benjamin Bach'
author = 'Benjamin Bach'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# source, destination
video_files = [
    ("https://overtag.dk/files/enable-pull-request-builders.mp4", "enable-pull-request-builders.mp4")
]

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

rootdir = os.path.dirname(os.path.realpath(__file__))
videodir = os.path.join(rootdir, "_static", "videos")

os.makedirs(videodir)

for source, dest in video_files:
    dest_path = os.path.join(videodir, dest)
    download_file(source, dest_path)
