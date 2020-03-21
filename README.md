cd
mkdir 
which python3
python3 -m venv env
sudo apt install python3-venv
whoami
source env/bin/activate
deactivate
rm -rf .env/
pip install flask
pip freeze
pip freeze > requirements.txt
cat requirements.txt
pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run -p 50001
printenv
echo $USER

nano main.py

- --- --- ---
TYPE

1. User rwx
2. Group rwx
3. Other rwx

r - 4
w - 2
x - 1

u, g, o + r, w, x

change permissions
0-7 0-7 0-7

chown user:group {filename}

# GIT
git init
git status

git add app.py
git add --all
git commit -m "massage"

git log
git push origin master

$ git config --global user.name "Dmytro Kaminskiy"
$ git config --global user.email "dmytro.kaminskyi92@gmail.com"
git rm --cached -r .idea
git rm -r .idea

git diff
git diff --cached

1 - 2 - 3

1. Changes [.idea, README.md...]red
2. Staging area [app.py]
3. Commit

git clone https://github.com/DmytroKaminskiy/test_repo.git

git status
git pull origin master 
git checkout -b branch1



--O--O--O--O--O
         \
          --O--O-----





