# Running program
1) Download python from the official website
1) Launch the command line (on Windows OS this can be done by pressing the Win+R key combination and entering “cmd” in the window that opens)
2) Move to the folder with the script and requirements file using the "cd" command

example:

```
cd Scripts
```
3) Install requirements

```
pip install -r requirements.txt
```
4) Run python file

```
python main.py
```
5) enjoy :)

# Creating an executable file for ease of use

1) Install package "pyinstaller":

```
pip install pyinstaller
```
2) Go to the folder with the python file using the method described above
3) Run the required command:

```
pyinstaller --onefile main.py
```
4) Go to the "src" folder that appears, where the resulting launch file is located
5) Run and enjoy :)
