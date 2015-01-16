# blog-app

-------------------------------------------------------------------------
    Dadaso Zanzane

    https://github.com/dadasoz-cuelogic/blog-app.git 
--------------------------------------------------------------------------

Install the requirements.

Setup the database connection

--Install The project

    $ git clone https://github.com/dadasoz-cuelogic/blog-app.git 

-- Install the requiremsnts from the file(requirements.txt)

    pip install -r REQUIREMENTS.txt           # Install or upgrade dependencies
    
    python manage.py migrate                  # Apply database migrations
    
    python manage.py compilemessages          # Create translation files

Sync the Database

    $ python manage.py syncdb

Run the server

    $ python manage.py runserver


