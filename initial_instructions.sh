# commands you need to know to create a git repo
pwd
cd ~/Documents
mkdir py4ds
cd py4ds
# install git if you don't have it
git init
touch README.md
# use `nano README.md` to edit the file
git add .
git commit -m 'initial commit messsage'
# set up a remote repo on github and copy the link to $REMOTE_URL variable
REMOTE_URL=https://github.com/username/repo.git
git remote add origin $REMOTE_URL
git push origin main
git pull # if you want to pull changes (made by others) from the remote repo

# install python
python --version
python week1/1_hello.py
