echo " BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear

echo " Making migrations "

python3 manage.py makemigrations
python3 manage.py migrate

echo " BUILD END" 
