from setuptools import find_packages, setup
# Read: http://peterdowns.com/posts/first-time-with-pypi.html

setup(
    name='kv_settings',
    packages=find_packages(),
    include_package_data=True,
    version='0.1.1',
    description='Django Key Value Settings',
    author='Eshan Das',
    author_email='eshandasnit@gmail.com',
    url='https://github.com/eshandas/django_key_value_settings',  # use the URL to the github repo
    download_url='https://github.com/eshandas/django_key_value_settings/archive/0.1.1.tar.gz',  # Create a tag in github
    keywords=['django', 'key value', 'settings'],
    classifiers=[],
    install_requires=[
        'Django>=1.7'],
)
