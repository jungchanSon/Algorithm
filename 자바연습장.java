public class 자바연습장{
    public static void main(String[] args) {
        LinkedList lk = new LinkedList();

        lk.append(1);
        lk.append(2);
        lk.append(3);
        lk.insert(2, 222);
        lk.appendLeft(0);

        System.out.println(lk);
    }
    
}

class Node{
    public int data;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    private Node head;

    public LinkedList(){
        this.head = null;
    }

    public void append(int data) { 
        Node newNode = new Node(data);

        if(this.head == null){
            this.head = newNode;
        } else {
            Node curNode = this.head;
            while(curNode.next != null) {
                curNode = curNode.next;
            }
            curNode.next = newNode;
        }
    }

    public void appendLeft(int data){ 
        Node newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }

    public void insert(int n, int data){
        Node newNode = new Node(data);
        Node prevNode = null;
        Node curNode = this.head;
        while(n > 1){
            prevNode = curNode;
            curNode = curNode.next;
            n -= 1;
        }
        prevNode.next = newNode;
        newNode.next = curNode;
    }
    public String toString(){
        String res = "";
        Node curNode = this.head;
        while (curNode.next != null){
            res += curNode.data + " -> ";
            curNode = curNode.next;
        }
        res += curNode.data;
        return res;
    }
}