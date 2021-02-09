from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='intake-stripe',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Intake driver to load Stripe data",
    license="BSD",
    author="Sophia Yang",
    url='https://github.com/sophiamyang/intake-stripe',
    packages=['intake-stripe'],
    entry_points={
        'console_scripts': [
            'intake-stripe=intake-stripe.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='intake-stripe',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
