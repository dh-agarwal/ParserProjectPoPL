# Parser Project for Principles of Programming Languages

## Ping Pong Club

By Dhruv Agarwal, Ryan Huynh, Adi Pillai, Andrew Chang, and Ashwin Prayaga

We are implementing a basic Python parser using Java

## Parser Requirements
ANTLR4 version 4.9.2
ANTLR-Denter (included in repo)

## ANTLR Installation and Setup
First, download ANTLR version 4.9.2 [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar).
Add the ANTLR4 and Denter JAR files to your CLASSPATH. (Denter jar file can be moved to a different location than in the repo folder) 

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
1. Add ANTLR4 and Antlr-Denter to CLASSPATH

2. Create antlr4.bat
```
java org.antlr.v4.Tool %*
```

3. Create grun.bat
```
java org.antlr.v4.gui.TestRig %*
```

## Parser Setup/Environment


## Testing Python Files
1. To generate the grammar using ANTLR, direct your terminal to the ParserProjectPoPL directory and run the following command:
```
antlr4 -Dlanguage=Java popl.g4
```
2. Compile the generated Java classes
```
javac *.java
```

3. Then, to test the parser on an example file called ```test.txt```, run the following command (-tree for terminal output and -gui for visualization):
```
grun popl start test.txt -tree
grun popl start test.txt -gui
```
