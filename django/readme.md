20250215 19:46
20250216 24:46
20250217 37:19
20250219 lab done
20250219 project1 done

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

# プロジェクト作成
django-admin startproject lecture3

# アプリ作成
cd lecture3
python manage.py startapp hello

# lecture3/settings.pyのINSTALLED_APPSにhelloを追加する
# lecture3/urls.pyのfrom django.urls import pathに includeのimportを追加、urlpatternsにpath('hello/', include("hello.urls")),を追加する
# hello/urls.pyを作成し、必要に応じてviews.pyを編集


python manage.py runserper


