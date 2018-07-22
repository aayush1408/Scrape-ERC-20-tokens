# ERC-20 Tokens
>Scrapes all the ERC-20 from etherscan.io, supports python 3.7

# Installation
1- Install python 3.7 from [Python.org](https://www.python.org)

2- `python setup.py` or `python3 setup.py`

  This will install all these packages

  * `pip install bs4`

  * `pip install requests`

After the installation, open terminal at the root folder--

Run `python script.py` or `python3 script.py` to get a spreadsheet file with all the details.

## Some Useful Installation Tips

If you have already installed python 2.7 install python 3 as well but it may be the problem that the packages installed with respect to python 2.7 and shows error for the python 3 packages,

So you need to install virtual Environment for the python 3 to install python3 packages.

```
    virtualenv -p /usr/bin/python3 py3env
    source py3env/bin/activate
    pip install package-name
```

After setting virtual environment install packages listed above and Enjoy.
