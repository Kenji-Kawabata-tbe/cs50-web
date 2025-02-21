202050213 32:56

pythonのalias
vim ~/.config/fish/config.fish
alias python='python3'

pythonの仮想環境
python3 -m venv ~/mypy
source ~/mypy/bin/activate.fish # macOS/Linux
mypy\Scripts\activate     # Windows

# パッケージをインストール
pip3 install パッケージ名

deactivate
