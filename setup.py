import setuptools, os

PACKAGE_NAME = 'facenet-train'
VERSION = '2.5.2'
AUTHOR = 'Aryan Rajoria'
EMAIL = 'aryanrajoria1003@gmail.com'
DESCRIPTION = 'Fork of facenet-pytorch for training'
GITHUB_URL = 'https://github.com/Aryan-Rajoria/facenet-pytorch'

parent_dir = os.path.dirname(os.path.realpath(__file__))
import_name = os.path.basename(parent_dir)

with open('{}/README.md'.format(parent_dir), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_URL,
    packages=[
        'facenet_train',
        'facenet_train.models',
        'facenet_train.models.utils',
        'facenet_train.data',
    ],
    package_data={'': ['*net.pt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'requests',
        'torchvision',
        'pillow',
    ],
)
