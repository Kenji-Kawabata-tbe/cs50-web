20250215 19:46
20250216 24:46
20250217 37:19

pythonのalias
vim ~/.config/fish/config.fish
alias python='python3'

pythonの仮想環境
python3 -m venv ~/mypy
source ~/mypy/bin/activate.fish # macOS/Linux
mypy\Scripts\activate     # Windows

# パッケージをインストール
pip3 install Django

deactivate


django-admin startproject lecture3
python manage.py runserper
python manage.py startapp hello



