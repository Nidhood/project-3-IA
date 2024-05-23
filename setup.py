from setuptools import setup, find_packages

setup(
    name='nombre_proyecto',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'tensorflow',  # o 'keras' dependiendo de tu instalación
        # Añade aquí otras librerías que necesites
    ],
    author='Nidhood',
    author_email='ivan.oroz34@gmail.com',
    description='Descripción de tu proyecto',
    url='https://github.com/Nidhood/project-3-IA.git',
)