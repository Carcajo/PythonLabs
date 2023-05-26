from setuptools import setup

setup(
    name='pmserializer',
    version="2.0.4",
    description="serializer of few formats",
    author="Carcajo",
    author_email='t375445391507@gmail.com',
    url='https://github.com/Carcajo/pmserializer',
    install_requires=["pytomlpp", 'pyyaml'],
    packages=['lab3'],
    test_suite='tests/',
)
