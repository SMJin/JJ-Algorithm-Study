package stack;

import java.util.Scanner;

public class stack_2493 {

    public static class Tower {
        private int order;
        private int floor;

        Tower(int o, int f) {
            this.order = o;
            this.floor = f;
        }

        public int getOrder() {
            return this.order;
        }

        public int getFloor() {
            return this.floor;
        }
    }

    public static class Stack {
        private Tower[] array;
        private int size;

        Stack() {
            this.array = new Tower[10000];
            this.size = 0;
        }

        public void push(Tower tower) {
            array[size++] = tower;
        }

        public Tower top() {
            if (isEmpty()) return null;
            return array[size-1];
        }

        public Tower pop() {
            if (isEmpty()) return null;
            return array[--size];
        }

        public boolean isEmpty() {
            if(size == 0) return true;
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Stack stack = new Stack();
        int n = scan.nextInt();

        stack.push(new Tower(1, scan.nextInt()));
        System.out.print("0 ");

        for (int i=2; i<=n; i++) {
            int currentNum = scan.nextInt();
            Tower currentTower = new Tower(i, currentNum);

            while(!stack.isEmpty()) {
                if (currentNum < stack.top().getFloor()) {
                    System.out.print(stack.top().getOrder() + " ");
                    break;
                }
                stack.pop();
            }

            if (stack.isEmpty()) System.out.print("0 ");
            stack.push(currentTower);

        }
    }
}