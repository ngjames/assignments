public class Ring {

  // DO NOT CHANGE THE FOLLOWING
  private class RingNode {
    Object obj;
    RingNode next;
 
    RingNode(Object j) {
      obj = j;
      next = null;  
    }
  }

  private RingNode head;
  private RingNode curr;

  public Ring() {
    head = curr = null;
  }
  
  // print out the content of the ring
  // starting from the head node
  public String toString() {
    String s = "";

    RingNode curr = head;
    if (curr == null) return s;

    s += curr.obj.toString();
    while (curr.next != head) {
      curr = curr.next;
      s += ", " + curr.obj.toString();
    }

    return s;
  }
  ////////////////////////////////////////

  // PUT YOUR CODES BELOW HERE
  public void addObj(Object obj) {

    if (curr != null) {
      RingNode toBeAdded = new RingNode(obj);
      toBeAdded.next = head.next;
      head.next = toBeAdded;
    } else {
      head = new RingNode(obj);
      curr = head;
      curr.next = head;
    }
  }

  public int size() {
    if (head != null) {
      RingNode save = curr;
      int Size = 0;
      while (curr.next != save) {
        Size++;
        curr = curr.next;
      }
      if (curr.next == save) {
        Size++;
      }
    curr = save;
    return Size;
    } else {
      return 0;
    }
  }

  public Object getCurrObj() {
    return curr.obj;
  }

  public void removeCurrObj() {
    RingNode save = curr;
    RingNode prev = curr;
    RingNode skippa = curr.next;

    if (this.size() == 1) {
      head = null;
      curr = null;
    } else {
      while (prev.next != save) {
        prev = prev.next;
      }
      prev.next = skippa;
      if (curr == head) {
        head = skippa;
      }
      curr = skippa;
    }
  }

  public void advance() {
    curr = curr.next;
  }
}
