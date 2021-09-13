from distutils.core import setup

setup(
    name='find_indian_state',
    packages=['find_indian_state'],
    version='1.0.0',
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='get indian state by city name or by coordinates',
    author='Stuti Pathak',
    author_email='stuti.pathak@bridgelabz.com',
    url='https://github.com/BridgeLabzSource/CityStateMapping/tree/indian_state_mapping',
    download_url='',
    keywords=['STATE', 'CITY_NAME', 'COORDINATES'],
    install_requires=[
        'geopy',
        'find_indian_state',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
