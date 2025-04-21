## How to execute the grammar?

```
> cd src
> python -m venv venv
> source venv/Scripts/activate
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt
```

Download complete binaries from [link](https://www.antlr.org/download/antlr-4.13.2-complete.jar) and save in for example in C:/Users/User/ProgramFiles/antlr/

```
> curl -O C/Users/User/ProgramFiles/antlr/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
> echo 'alias antlr4="java -jar C/Users/User/ProgramFiles/antlr/antlr-4.13.2-complete.jar"' >> ~/.bashrc
> source ~/.bashrc
> cd ../Grammar
> antlr4 -Dlanguage=Python3 -visitor Esperados.g4 -o ../src/generated
> cd ../src
> python main.py
```

! Make sure you have Java version at least 11.
```
java -version
```

If not install Java from [link](https://www.oracle.com/pl/java/technologies/javase/jdk11-archive-downloads.html)

### To run tests:
```
cd src
python -m unittest discover -s tests
```
no runnable tests yet

### Notes
```
cd src
antlr4 -Dlanguage=Python3 -visitor ../Grammar/Esperados.g4 -o ../src/generated
py main.py ../Examples/code.es
```