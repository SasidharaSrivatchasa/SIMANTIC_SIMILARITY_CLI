from setuptools import setup

setup(
    name='semantic-sim',
    version='1.0',
    py_modules=['semantic_similarity'],
    install_requires=[
        'nltk',
        'joblib',
        'numpy',
        'sentence-transformers',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'semantic-sim=semantic_similarity:main',
        ],
    },
)
