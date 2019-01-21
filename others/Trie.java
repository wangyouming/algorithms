public class TrieNode {
    public char data;
    public TrieNode[] children = new TrieNode[26];
    public boolean isEndintChar = false;
    public TrieNode(char data) {
        this.data = data;
    }
}

public class Trie {
    private TrieNode root = new TrieNode('/');

    public void insert(char[] text) {
        TrieNode p = root;
        for (int i = 0; i < text.length; ++i) {
            int index = text[i] - 'a';
            if (p.children[index] == null) {
                TrieNode newNode = new TrieNode(text[i]);
                p.children[index] = newNode;
            }
            p = p.children[index];
        }

        p.isEndintChar = true;
    }

    public boolean find(char[] pattern) {
        TrieNode p = root;
        for (int i = 0; i < pattern.length; ++i) {
            int index = pattern[i] - 'a';
            if (p.children[index] == null) {
                return false;
            }
            p = p.children[index];
        }
        if (p.isEndintChar == false) return false;
        else return true;
    }
}