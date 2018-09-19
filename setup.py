from distutils.core import setup

setup(name='OvStat',
      version='1.0',
      description='OV Chipkaart API',
      author='Hylco Uding',
      author_email='chipchop@protonmail.com',
      packages=['ovstat'],
      install_requires=[
        "requests",
      ],
      url = 'https://github.com/OVChip/ovchipapi-python',
      download_url = 'https://github.com/OVChip/ovchipapi-python/tarball/0.1',
      keywords = ["OV","Public Transport","ov-chipkaart","chipkaart"]
     )
