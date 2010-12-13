from distutils.core import setup


setup(
    name = "django-visitors",
    author = "Guillaume Libersat",
    author_email = "guillaume@spreadband.com",
    description = "Record and display latest visitors for an object.",
    long_description = open("README.rst").read(),
    license = "GPL v3",
    url = "http://github.com/SpreadBand/django-visitors",
    packages = [
        "visitors",
    ],
    include_package_data = True,
    package_data = {
        'visitors': [
            'locale/*/*/*',
        ]
    },
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
