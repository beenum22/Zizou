from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Zizou',
	version='1.0',
	description='A package dedicated to the G.O.A.T, Zizou. Zidane means to grow and help others grow.',
	long_description=readme(),
	url='http://github.com/beenum22/Zizou',
	author='Muneeb Ahmad',
	author_email='muneeb.gandapur@gmail.com',
	#entry_points = {
	#	'console_scripts': ['Zizou=Zizou.main:main']
	#},
	packages=setuptools.find_packages(),
	zip_safe=False)
