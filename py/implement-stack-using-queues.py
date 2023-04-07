# 225. Implement Stack using Queues

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.pop())

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    obj = MyStack()
    obj.push(10)
    obj.push(11)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
