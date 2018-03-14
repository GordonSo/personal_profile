pip install virtualenv
virtualenv env
env\scripts\activate.bat
pip install -r requirements
:: create the sqlit tables
python manage.py migrate

cd C:\pyprojects\textract-master
python setup.py install
deactivate