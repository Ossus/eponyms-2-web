Eponyms 2 Web API Server
========================

A Python 3 Flask app serving the web API needed for the Eponyms 2 stack.


## Installation

To develop or run the web app locally, it's best to use a virtual environment containing all necessary modules:

```pip
git clone https://github.com/ossus/eponyms-2-web.git
cd eponyms-2-web
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt
python wsgi.py
```

You can also use gunicorn to run the app:

```bash
gunicorn --bind 0.0.0.0:8000 wsgi
```

The [eponyms-2-web-installer](https://github.com/Ossus/eponyms-2-web-installer) repository has an Ansible role that sets up **nginx** and **upstart** to route traffic accordingly and make sure the app is always running.
