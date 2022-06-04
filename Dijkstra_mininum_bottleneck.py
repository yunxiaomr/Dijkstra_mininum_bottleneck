# -*- coding: utf-8 -*-
"""
@author: yunxiao
@software: PyCharm
@file: test.py
@email:yunxiaomr@163.com
@time: 2020/12/20 20:02

Topic:Dijkstra's mininum bottleneck algorithm via heap
"""

import math

class MinHeap():
    def __init__(self):
        self.value = []
        self.node = []

    def _swap(self, i, j):
        self.value[i], self.value[j] = self.value[j], self.value[i]
        self.node[i], self.node[j] = self.node[j], self.node[i]
        return

    def _bubble_up(self, idx):
        while idx > 0 and self.value[(idx - 1) // 2] > self.value[idx]:
            self._swap(idx, (idx - 1) // 2)
            idx = (idx - 1) // 2
        return

    def _bubble_down(self, idx):
        n = len(self.value)
        while idx <= n - 1:
            l, r = idx * 2 + 1, idx * 2 + 2
            if l > n - 1: break
            child = r if r <= n - 1 and self.value[r] < self.value[l] else l
            if self.value[child] < self.value[idx]:
                self._swap(idx, child)
                idx = child
            else:
                break
        return

    def extract_min(self):
        if not self.value: return None
        return self.value[0], self.node[0]

    def insert(self, v, node):
        idx = len(self.value)
        self.value.append(v)
        self.node.append(node)
        self._bubble_up(idx)
        return

    def delete(self, pos=int(0)):
        idx = len(self.value) - 1
        self._swap(pos, idx)
        self.value.pop()
        self.node.pop()
        if pos > len(self.value) - 1: return
        # bubble up, bubble down
        if pos > 0 and self.value[pos] < self.value[(pos - 1) // 2]:
            self._bubble_up(pos)
        else:
            self._bubble_down(pos)
        return


def dijkstra(adjlist, lengths, s=0):
    n = len(adjlist)
    dist = [math.inf for i in range(n)]
    heap = MinHeap()
    explored = [False for i in range(n)]
    explored[s] = True
    for nex, w in zip(adjlist[s], lengths[s]):
        if nex not in heap.node:
            heap.insert(w, nex)
        elif w < heap.value[heap.node.index(nex)]:
            heap.delete(heap.node.index(nex))
            heap.insert(w, nex)
    for i in range(n - 1):
        if not heap.value:
            break
        score, curr = heap.extract_min()
        heap.delete(0)
        dist[curr] = score
        explored[curr] = True
        for nex, w in zip(adjlist[curr], lengths[curr]):
            if explored[nex]:
                continue
            if nex not in heap.node:
                heap.insert(dist[curr] + w, nex)
            else:
                idx = heap.node.index(nex)
                if dist[curr] + w < heap.value[idx]:
                    heap.delete(idx)
                    heap.insert(dist[curr] + w, nex)
    return dist

def dijkstra_mininum_bottleneck(adjlist, lengths, s=0):
    n = len(adjlist)
    # 初始化
    dist_mininum_bottleneck = [math.inf for i in range(n)]
    heap = MinHeap()
    explored = [False for i in range(n)]
    explored[s] = True
    for nex, w in zip(adjlist[s], lengths[s]):
        if nex not in heap.node:
            heap.insert(w, nex)
        elif w < heap.value[heap.node.index(nex)]:
            heap.delete(heap.node.index(nex))
            heap.insert(w, nex)
    # 处理
    for i in range(n - 1):
        # 取堆顶元素 即最小值
        if not heap.value:
            break
        score, curr = heap.extract_min()
        heap.delete(0)
        dist_mininum_bottleneck[curr] = score
        explored[curr] = True
        # 取bottleneck并入小顶堆
        for nex, w in zip(adjlist[curr], lengths[curr]):
            if explored[nex]:
                continue
            if nex not in heap.node:
                heap.insert(max(dist_mininum_bottleneck[curr],w),nex)
            else:
                idx = heap.node.index(nex)
                if max(dist_mininum_bottleneck[curr],w)< heap.value[idx]:
                    heap.delete(idx)
                    heap.insert(max(dist_mininum_bottleneck[curr],w), nex)

    return dist_mininum_bottleneck

if __name__ == '__main__':
    line_str = input()
    node_n,edge_m = int(line_str.split(' ')[0]),int(line_str.split(' ')[1])

    adjlist = []   # 定义邻接表
    lengths = []   # 定义权重表

    for i in range(node_n):
        adjlist.append([])
        lengths.append([])

    #初始化邻接表及权重表
    for i in range(edge_m):
        edge_str = input()
        u, v, w = int(edge_str.split(' ')[0]), int(edge_str.split(' ')[1]),int(edge_str.split(' ')[2])
        adjlist[u-1].append(v-1)
        lengths[u-1].append(w)

    print('adjlists:',adjlist)
    print('weights:',lengths)

    #返回答案
    dist_mininum_bottleneck = dijkstra_mininum_bottleneck(adjlist, lengths, s=0)
    print('dist_mininum_bottleneck:',dist_mininum_bottleneck)
    pass
