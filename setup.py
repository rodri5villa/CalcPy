from setuptools import setup, find_packages

setup(
    name='CalcPy',  # Nombre del paquete
    version='0.1.0',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Una librería de calculadora en Python que soporta cálculos básicos, científicos y avanzados.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rodri5villa/CalcPy-Library',  # URL del repositorio de GitHub
    packages=find_packages(),  # Encuentra todos los paquetes automáticamente
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Aquí puedes listar dependencias si las hay
    ],
    extras_require={
        'dev': ['pytest>=6.0'],
        'test': ['pytest'],
    },
    include_package_data=True,
)