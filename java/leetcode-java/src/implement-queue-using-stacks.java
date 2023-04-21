import java.util.Stack;

class MyQueue {
  private final Stack<Integer> input = new Stack<Integer>();
  private final Stack<Integer> out = new Stack<Integer>();
  public MyQueue() {}

  public void push(int x) {
    this.input.push(x);
  }

  public int pop() {
    this.peek();
    return this.out.pop();
  }

  public int peek() {
    if (this.out.empty()) {
      while (!this.input.empty()) {
        this.out.push(this.input.pop());
      }
    }
    return this.out.peek();
  }

  public boolean empty() {
    return this.out.empty() && this.input.empty();
  }

  public static void main(String[] args) {
    MyQueue obj = new MyQueue();
    obj.push(99);
    obj.push(2);
    int param_2 = obj.pop();
    int param_3 = obj.peek();
    boolean param_4 = obj.empty();
    System.out.println(param_2);
    System.out.println(param_3);
    System.out.println(param_4);
  }

}