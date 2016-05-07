yum install gcc
cd /usr/src
wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
tar xzf Python-2.7.11.tgz
mv /usr/src/Python-2.7.11 /usr/bin/
cd /usr/bin/Python-2.7.11
./configure
make altinstall

mv /usr/bin/python2.7 /usr/bin/python273
ln -s /usr/bin/Python-2.7.11/python /usr/bin/python2.7
python -V

sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo python ez_setup.py
sudo /usr/bin/easy_install-2.6 pip
sudo pip install virtualenv
sudo pip install --upgrade pip

git clone https://github.com/winlingit/w205-project-aw.git
cd w205-project-aw
virtualenv -p /usr/bin/python2.7 venv
source /venv/bin/activate

sudo pip install pandas
sudo pip install --upgrade google-api-python-client
sudo pip install schedule

mkdir data_raw
mkdir data_master