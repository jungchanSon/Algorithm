package 자료구조;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

public class Tree{
    public static void main(String[] args) {
        Tree_ t = new Tree_("A");
        t.add_node("A", "B");
        t.add_node("A", "C");
        t.add_node("B", "D");
        t.add_node("C", "F");

        System.out.print(t.root.data + " -> ");
        for(Node i : t.root.children){
            System.out.print(i.data+ " ");
        }
        System.out.println();

        Node b = t.root.children.get(0);
        Node c = t.root.children.get(1);
        
        System.out.print(b.data+ " -> ");
        for(Node i : b.children){
            System.out.print(i.data + " ");
        }
        System.out.println();

        System.out.print(c.data+ " -> ");

        for(Node i : c.children){
            System.out.print(i.data + " ");
        }
    }
}
class Tree_ {
    Node root;
    
    Tree_(String data) {
        this.root = new Node(data);
    }

    public void add_node(String targetNode, String data){
        Deque<Node> q = new LinkedList<>();
        q.addLast(this.root);
        while(!q.isEmpty()){
            Node currentNode = q.pollFirst();
            if (currentNode.data == targetNode) {
                currentNode.children.add(new Node(data));
                break;
            }
            
            for(Node i : currentNode.children){
                q.addLast(i);
            }

        }
    }
}

class Node{
    public String data;
    public ArrayList<Node> children;

    Node(String data){
        this.data = data;
        this.children = new ArrayList<>();
    }
}