# class MinHeap:
#     def __init__(self):
#         self.heap = [0] # 루트 노드의 인덱스를 1로 설정할 것 0번 인덱스는 공란
#         # self.heap = list(0) 은 틀린 문법 -> list()는 iterable한 객체를 list로 변환하는 것. 0은 iterable하지 않음.

#     def insert(self, x):
#         self.heap.append(x)
#         idx = len(self.heap)-1
#         self.heapify_up(idx) # 인덱스 히피파이

#     def heapify_up(self, idx): # idx값을 대소관계맞춰서 재정렬함
#         if idx>0 and self.heap[idx]<self.heap[idx//2]:
#             # 부모노드가 더 크면 스왑
#             self.heap[idx] , self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
#             self.heapify_up(idx//2)# 바뀐 부모노드에 대해서도 재귀

#     def pop(self):
#         #print('heap : ',self.heap)
#         if len(self.heap)>1:# 비어있지 않은 것
#             min_val = self.heap[1] # 미리 최소값빼두고
#             print(min_val)  # 일단 출력
#             last_val = self.heap.pop() # 맨뒷값 빼고
#             if len(self.heap) == 1: # 뺐는데 하나 남았으면 종료
#                 return
#             self.heap[1] = last_val     # 루트값이랑 바꾸고
#             self.heapify_down(1)    # 히피파이 다운
#         else:
#             print(0)
#     def heapify_down(self, idx):
#         min_val = idx   # 일단은 이게 부모
#         left = idx * 2  # 왼쪽 자식
#         right = idx * 2 + 1 # 오른쪽 자식

#         # 왼쪽 자식인 존재하며
#         if left < len(self.heap):
#             # 부모보다 작은 경우
#             if self.heap[left] < self.heap[min_val]:
#                 min_val = left  # 스왑
#         if right < len(self.heap):# 오른쪽 자식
#             if self.heap[right] < self.heap[min_val]:
#                 min_val = right # 스왑
#         # 스왑을 안하는 경우도 있음

#         # 근데 일단 스왑을 했으면, 끝까지 재귀 해야 함
#         if min_val != idx:
#             # 인덱스는 교환했으니까 값도 교환
#             self.heap[idx], self.heap[min_val] = self.heap[min_val], self.heap[idx]
#             self.heapify_down(min_val)

# N = int(input())
# heap = MinHeap()
# for _ in range(N):
#     c = int(input())
#     if c == 0:
#         heap.pop()
#     else:
#         heap.insert(c)
# ㅈㄴ 빠르네??

import heapq
import sys
input= sys.stdin.readline
orders = int(input())
heap= []
for i in range(orders):
    query = int(input())
    if query > 0:
        heapq.heappush(heap, query)
    else:
        if len(heap)!=0:
            print(heapq.heappop(heap))
        else:
            print(0)