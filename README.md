# Parser Project for Principles of Programming Languages

## Ping Pong Club

By Dhruv Agarwal, Ryan Huynh, Adi Pillai, Andrew Chang, and Ashwin Prayaga

We are implementing a basic Python parser using Python 3.9

## Parser Requirements
ANTLR4 version 4.9.2

Python 3.9

## Python Package Requirements
antlr4-python3-runtime version 4.9.2

antlr-denter

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


