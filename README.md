# pwdgen

### A simple password generator written in Python. pwdgen allows you to create a weak or strong password and copies it to your clipboard. Shitty codebase included!
---
Disclaimer: I have no idea how secure the generated passwords are since I'm using built in functions (especially from `random` (https://docs.python.org/3/library/random.html)) to randomize strings.

---

**Strong 💪 passwords**, by my randomly made up definition, consist of:
* a length between 8 and 12 (included)
* at least one digit, letter and symbol (string.ascii_punctuation)

**Strong 💪 passwords** don't allow:
* duplicates (`d` and `D` count as duplicate)
* therefore consecutive elements (`aA`, `**`)

---
*Weak 👶 passwords*, by my randomly made up definition, consist of:
* a length between 6 and 8 (included)
* at least one digit and letter

*Weak 👶 passwords* don't allow:
* the usage of consecutive letters (`d` and `D` count as consecutive)

---
### Installation
You simply clone the repository:
```shell
mkdir pwdgen
cd pwdgen
git clone https://github.com/grndng/pwdgen .
```

---
### Usage
Since `pwdgen` is copying passwords directly into your clipboard using `pyperclip`, you might need additional modules. On the PyPi project site (https://pypi.org/project/pyperclip/) you can find following information:

On Windows, no additional modules are needed.
On Mac, pyperclip makes use of the pbcopy and pbpaste commands, which should come with the os.
On Linux, this module makes use of the xclip or xsel commands, which should come with the os. I had to install xsel (I'm using Arch, btw).
Otherwise on Linux, you will need the gtk or PyQt4 modules installed.

To generate a password, you have to run `pwdgen.py` with an argument (in case you want to create a weak password). By default `pwdgen.py` will create strong passwords:
```shell
python pwdgen.py -s strong      # for strong passwords
python pwdgen.py -s weak        # for weak passwords
```

Afterwards you can CTRL+V the password whereever you like.

---
### ToDo
* Allow to hide (=not print) the password from Terminal
* Allow to decide that the password should not be copied to clipboard
* Simplify the password generator
