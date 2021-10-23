import java.util.Scanner;

public class Main {

    static class Node {
        char ch;
        Node left;
        Node right;

        Node(char ch) {
            this.ch = ch;
            left = null;
            right = null;
        }
    }

    static class Tree {
        Node root;

        Tree() {
            this.root = null;
        }

        Node find(Node curN, char ch) {
            if (curN == null) {
                return null;
            }
//            System.out.println("find func current value : " + curN.ch);

            if (curN.ch == ch) {
                return curN;
            }


            Node findLeft = find(curN.left, ch);
            if (findLeft != null) {
                return findLeft;
            }

            return find(curN.right, ch);
        }

        void addNode(char pCh, char Cch) {
            Node parentNode = find(root, pCh);
//            System.out.println("pCh : " + pCh + ", Cch : " + Cch);
//            System.out.println("parentNode : " + parentNode.ch);
            if (parentNode.left == null) {
                parentNode.left = new Node(Cch);
//                System.out.println("add left : " + parentNode.left.ch);
            } else if(parentNode.right == null) {
                parentNode.right = new Node(Cch);
//                System.out.println("add right : " + parentNode.right.ch);
            }
        }

        void addNodeLeft(char pCh, char Cch) {
            Node parentNode = find(root, pCh);
            parentNode.left = new Node(Cch);
        }

        void addNodeRight(char pCh, char Cch) {
            Node parentNode = find(root, pCh);
            parentNode.right = new Node(Cch);
        }

        void preOrder(Node start) {
            if(start == null) {
                return;
            }

            System.out.print(start.ch);
            preOrder(start.left);
            preOrder(start.right);
        }

        void inOrder(Node start) {
            if (start == null) {
                return;
            }

            inOrder(start.left);
            System.out.print(start.ch);
            inOrder(start.right);
        }

        void postOrder(Node start) {
            if (start == null) {
                return;
            }

            postOrder(start.left);
            postOrder(start.right);
            System.out.print(start.ch);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        Tree tree = new Tree();

        for (int i=0; i<n; i++) {
            char first = scan.next().charAt(0);
            char second = scan.next().charAt(0);
            char third = scan.next().charAt(0);

            if (tree.root == null) {
                tree.root = new Node(first);
            }
            if (second != '.') {
                tree.addNodeLeft(first, second);
            }
            if (third != '.') {
                tree.addNodeRight(first, third);
            }
        }

        tree.preOrder(tree.root);
        System.out.println();
        tree.inOrder(tree.root);
        System.out.println();
        tree.postOrder(tree.root);
    }

}
