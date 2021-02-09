from setuptools import setup, find_packages
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
    packages=find_packages(),
    entry_points={
        'intake.drivers': [
            'stripe_catalog = intake_stripe.core:StripeCatalog',
            'stripe_table = intake_stripe.core:StripeTableSource',
            ]
    },
    install_requires=[
        'stripe',
        'intake',
        'pandas'
    ],
    keywords='intake-stripe',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
