# For min heap we initialize a list . To getMin we just return the value of first index.
# For extracting min we return the value of the first index and swap the last element with the root and perform heapify operation.
# For inserting we insert it as an last element and then perform heapify operation
# Time Complexity : getMin = O(1),extractMin = O(logn) , insert = O(logn)
# Space Complexity : O(n)

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def getMin(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def extractMin(self):
        if self.heap:
            if len(self.heap)==1:
                return  self.heap.pop()
            else:
                popped_element = self.heap.pop()
                min_element = self.heap[0]
                self.heap[0] = popped_element
                self.heapify_down(0)
                self.print_heap()
                return min_element
        else:
            return None
    
    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)
        self.print_heap()
    
    def heapify_down(self,index):
        size = len(self.heap)-1
        while True:
            left = 2*index + 1
            right = left + 1
            smallest = index

            if left < size and self.heap[left]<self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right 

            if smallest == index:
                break
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            index = smallest

    def heapify_up(self,index):
        parent = (index-1) // 2
        print("Parent index is ",parent)

        while parent >= 0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            index = parent
            parent = index // 2
    






