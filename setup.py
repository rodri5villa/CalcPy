from setuptools import setup, find_packages

setup(
    name='CalcPy',  # Nombre del paquete
    version='0.1.0',  # Versión inicial del paquete
    author='Rodrigo Villa',  # Tu nombre como autor
    author_email='tu.email@example.com',  # Tu correo electrónico
    description='Una librería de calculadora en Python que soporta cálculos básicos, científicos y avanzados.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),  # Leer la descripción larga desde README.md
    long_description_content_type='text/markdown',  # Especifica que el README.md usa Markdown
    url='https://github.com/rodri5villa/CalcPy-Library',  # URL del repositorio en GitHub
    license='MIT',  # Especifica la licencia
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes
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
    python_requires='>=3.6',  # Especifica la versión mínima de Python
    install_requires=open('requirements.txt').read().splitlines(),  # Lee las dependencias desde requirements.txt
    extras_require={
        'dev': ['pytest>=6.0'],  # Dependencias adicionales para desarrollo
        'test': ['pytest'],  # Dependencias adicionales para pruebas
    },
    include_package_data=True,  # Incluye archivos adicionales especificados en MANIFEST.in
)
