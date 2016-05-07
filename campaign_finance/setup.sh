yum install gcc
cd /usr/src
wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
tar xzf Python-2.7.11.tgz
cd Python-2.7.11
./configure
make altinstall

python -V

sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo python ez_setup.py
sudo /usr/bin/easy_install-2.6 pip
sudo pip install virtualenv
sudo pip install --upgrade pip

cd /w205-project-aw
virtualenv -p /usr/bin/python2.7 venv
source /venv/bin/activate



sudo pip install pandas
sudo pip install --upgrade google-api-python-client
sudo pip install schedule


mv /usr/bin/python /usr/bin/python266
ln -s /usr/bin/Python-2.7.11/python /usr/bin/python