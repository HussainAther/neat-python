from setuptools import setup

setup(
    name='neat-python',
    version='0.7',
    author='syed.hussain.ather',
    author_email='shussainather@gmail.com',
    maintainer='Syed Hussain Ather',
    maintainer_email='shussainather@gmail.com',
    url='https://github.com/hussainather/neat-python',
    license="BSD",
    description='A NEAT (NeuroEvolution of Augmenting Topologies) implementation',
    long_description='Python implementation of NEAT (NeuroEvolution of Augmenting Topologies), a method ' +
                     'developed by Kenneth O. Stanley for evolving arbitrary neural networks.',
    packages=['neat', 'neat/iznn', 'neat/nn', 'neat/ctrnn'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering'
    ]
)
