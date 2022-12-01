# Parser Project for Principles of Programming Languages

## Ping Pong Club

By Dhruv Agarwal, Ryan Huynh, Adi Pillai, Andrew Chang, and Ashwin Prayaga

We are implementing a basic Python parser using Python 3.9.

## Parser Requirements
ANTLR4 version 4.9.2

Python 3.9

## Python Package Requirements
antlr4-python3-runtime version 4.9.2

antlr-denter

## ANTLR Installation and Setup
First, download ANTLR version 4.9.2 [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar).

### Instructions for Unix systems (Linux and MacOS)
1. Put the antlr4 file where it belongs
```
sudo cp antlr-4.9.2-complete.jar /usr/local/lib
```

2. Add the file to your bash profile
```
export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
```

3. Add alias for antlr4
```
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
```

4. Add alias for grun
```
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" org.antlr4.v4.gui.TestRig'
```

### Instructions for Windows systems

## Parser Setup/Environment
Before you begin, make sure you have Python 3.9 installed.

To install antlr4 and antlr-denter for Python, run 

```
pip install antlr4-python3-runtime==4.9.2
pip install antlr-denter
```

## Testing Python Files
To generate the grammar using ANTLR, direct your terminal to the ParserProjectPoPL directory and run the following command:

```
antlr4 -Dlanguage=Python3 popl.g4
```

Then, to test the parser on an example file called ```test.txt```, run the following command:
```
python3 main.py test.txt
```
