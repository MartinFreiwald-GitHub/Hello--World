
#!/usr/bin/python

# def setup_install():
   # print('installing pip and virtualenv so we can give django its own version of python')
   # os.system('yum -y install python-pip && pip install --upgrade pip')
   # os.system('pip install virtualenv')
   # os.chdir('/opt')
   # os.mkdir('/opt/django')
   # os.chdir('opt/django')
   # os.system('virtualenv django-env')
   # os.system('chown -r martinfreiwald708 /opt/django')

# def django_install():
    # print('activating virtualenv and installing django after pre-requirements have been met')
    
    # os.system('source /opt/django/django-env/bin/activate && pip install django') 
                      #confirm install and start a django project#
    # os.chidr('opt/django')
    # os.system('source /opt/django/django-env/bin/activate ' + \
    #          '&& django-admin --version ' + \
    #          '&& django-admin startproject project1')

# def django_start():
    # print('starting django')
    # os.system("myip=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<. *$//') && sed -i \"s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = /[\ '$MYIP\' \]/G\ " /opt/django/project1/project1/settings.py")
    # os.system('sudo -u martinfreiwald708 sh -c "/opt/django/django-env/bin/activate && python manage.py runserver 0.0.0.0:8000&"')

# setup_install()
# django_install()
# django_start()
