# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
#
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
#
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.


K = int(input())
stack = []

def is_empty(s):
    if len(s) == 0:
        return True

for i in range(K):
    n = int(input())
    if n > 0:
        stack.append(n)
    else:
        if is_empty(stack):
            break
        stack.pop()

print(sum(stack))
