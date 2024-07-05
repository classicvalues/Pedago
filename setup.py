from setuptools import setup, find_packages

setup(
    name='pedago',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-restful',
        'flask-jwt-extended',
    ],
    entry_points={
        'console_scripts': [
            # Define any console scripts here
            # Example: 'pedago-script=pedago.module:function',
        ],
    },
    author='Epictecus School',
    author_email='seasthaalores@dr.com',
    description='Pedago: An educational management system package.',
    url='https://github.com/epictecus/pedago',  # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
