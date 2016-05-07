sudo yum install python27-devel -y
sudo mv /usr/bin/python /usr/bin/python266
sudo ln -s /usr/bin/python2.7 /usr/bin/python

sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo python ez_setup.py
sudo /usr/bin/easy_install-2.7 pip
sudo pip install virtualenv

mkdir data_raw
mkdir data_master

pip install pandas
