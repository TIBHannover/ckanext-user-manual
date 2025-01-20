[![CI](https://github.com/TIBHannover/ckanext-user-manual/actions/workflows/test.yml/badge.svg)](https://github.com/TIBHannover/ckanext-user-manual/actions/workflows/test.yml)


# ckanext-user-manual

 The plugin adds a "Help" option on the site main navigation menu. The Help page contains information about CKAN functionalities that aims to answer users questions and guiding them to use CKAN.  


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
|  2.9 | Yes    |
| earlier | Not Tested |           |


## Installation


To install ckanext-user-manual:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

        git clone https://github.com//ckanext-user-manual.git
        cd ckanext-user-manual
        pip install -e .
        pip install -r requirements.txt

3. Add `user_manual` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

        sudo service apache2 reload


## Customization

The page contents are in: `templates/snippets/sections`. You may also need to change `templates/snippets/ckanext_user_manual_help.html`