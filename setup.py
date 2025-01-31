from setuptools import setup


setup(
    name='pylama-pre-commit',
    description='Pylama pre-commit support',
    url='https://github.com/gvanderest/pylama-pre-commit',
    version='0.3.0',
    author='Guillaume VanderEst',
    author_email='gvanderest@gmail.com',
    install_requires=[
        'pylama',
        'isort',
        'radon',
        'pylint',
        'pyflakes',
        'pycodestyle',
        'pydocstyle',
        'mypy',
        'eradicate',
        'pylama_pylint'
    ],
)
