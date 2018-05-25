import os

from setuptools import setup


def _get_version():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictmatching', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip().strip('\'')


def main():
    return setup(
        name='dictmatching',
        version=_get_version(),
        install_requires=[
            'decorator',
            'six',
        ],
    )


if __name__ == '__main__':
    main()
