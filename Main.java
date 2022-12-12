import java.util.Arrays;
import java.util.List;

import org.antlr.v4.gui.TreeViewer;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

public class Main {
    public static void main(String[] args) throws Exception {
        final CharStream stream = CharStreams.fromFileName("test.py");
        final poplLexer lexer = new poplLexer(stream);
        final poplParser parser = new poplParser(new CommonTokenStream(lexer));
        final ParseTree tree = parser.start();
        System.out.println(tree.toStringTree(parser));

        // GUI visualization of the parse tree
        final List<String> ruleNames = Arrays.asList(poplParser.ruleNames);
        final TreeViewer view = new TreeViewer(ruleNames, tree);
        view.open();
    }
}