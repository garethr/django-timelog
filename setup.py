from setuptools import setup, find_packages

setup(
    name = "django-timelog",
    version = "0.3",
    author = "Gareth Rushgrove",
    author_email = "gareth@morethanseven.net",
    url = "http://github.com/garethr/django-timelog/",
    
    packages = find_packages('src'),
    package_dir = {'':'src'},
    license = "MIT License",
    keywords = "django",
    description = "Performance logging middlware and analysis tools for Django",
    install_requires=[
        'texttable',
        'progressbar',
    ],
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
