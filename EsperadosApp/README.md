## How to execute the grammar?

```
> cd EsperadosApp
> python -m venv venv
> source venv/Scripts/activate
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt
```

Download complete binaries from [link](https://www.antlr.org/download/antlr-4.13.2-complete.jar) and save in for example in ~/ProgramFiles/antlr/

```
> curl -O ~/ProgramFiles/antlr/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
> echo 'alias antlr4="java -jar ~/ProgramFiles/antlr/antlr-4.13.2-complete.jar"' >> ~/.bashrc
> source ~/.bashrc
> cd ../Grammar
> antlr4 -Dlanguage=Python3 -visitor Esperados.g4 -o ../EsperadosApp/src/generated
> cd ../EsperadosApp
> python src/main.py ../Examples/code.es
```

> [!TIP]
> Make sure you have at least 11 Java version.

```
java -version
```

If not -> install Java from [link](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)

> [!TIP]
> Make sure you have graphviz programme.

```
dot -V
```

If not:
* install graphviz programme from [link](https://graphviz.org/download/)
* Choose "EXE installer" one
* Mark option "Add Graphviz to the system PATH"
* if necessary restart your device

### To run tests:

```
cd EsperadosApp
pytest
```

### Notes
```
cd EsperadosApp
antlr4 -Dlanguage=Python3 -visitor ../Grammar/Esperados.g4 -o ../EsperadosApp/src/generated
py src/main.py ../Examples/code.es
```