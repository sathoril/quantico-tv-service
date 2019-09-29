QuanticoTv - API
================

1. 'Quantico' name is ilustrative, this project isn't about quantum physics neither about quantum coaching.

2. This software require the following projetc:

    > [quantico-tv-pwa](https://github.com/joaop221/)

3. And if you prefer this projects too:

    > [quantico-tv-pwa](https://github.com/joaop221/)

QuanticoTv - API is a simple Django app to cconnect you to your midia center. For each
question, visitors can choose between a fixed number of answers.

Setup
-----

1. Verify if [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) are installed,

2. Run `pip install -r requirements.txt`.

3. Go to [setting.py](./quanticoTv/setting.py) and change the values between '{}' to configura de applciation database:

    example: ~~{change this}~~ -> to this

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '{quanticoTv}',
            'USER': '{postgres}',
            'PASSWORD': '{123456}',
            'HOST': '{127.0.0.1}',
            'PORT': '5432',
        }
    }

    ...
    
    ALLOWED_HOSTS = [
        ...
        '{list of allowed hosts}'
    ]
    ```

4. If you are a new developer go to [Contribute and Quick start Development](#developer) section unless continue this steps.

5. Go to root directory of the project and to install run `pip install` or `python setup.py`.

6. If you prefer this project can run on [virtualenv]()

Contribute and Quick start Development
--------------------------------------

1. Add "QuanticoTv - API" features to your INSTALLED_APPS [setting.py](./quanticoTv/setting.py) like this:

    ```python
    INSTALLED_APPS = [
        ...
        'searchSources',
    ]
    ```

2. Include the urls URLconf in your project [urls.py](./quanticoTv/urls.py) like this:

    ```python
    path('searchSources/', include('searchSources.urls')),
    ```

3. Run `python manage.py migrate` to create the quanticoTv models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled, to add users run `python manage.py createsuperuser` and add the users).

5. Visit http://127.0.0.1:8000/searchSources/ to manage Search Sources.