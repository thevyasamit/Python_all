class Node:
    def __init__(self, data , next):
        self.val = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while(itr.next!= None):
            itr= itr.next
        itr.next = Node(data,None)
    
    def print_linked_list(self):
        if self.head == None:
            print('XX Empty List XX')
            return
        itr = self.head
        res = ' '
        while itr:
            res += str(itr.val) + '->'
            itr = itr.next
        print(res)

    def detect_loop(self):
        s = set()
        itr = self.head
        while(itr.next != None):
            if (itr in s):
                return True
            s.add(itr)
            itr = itr.next
            


    def length(self):
        count = 0
        itr  = self.head
        if itr == None:
            count = 0
        while(itr!= None):
            count+=1
            itr = itr.next
        print('Length is ', count)
    
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr.next!= None:
            if count == index-2:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1



if __name__=='__main__':
    l = linked_list()
    # l.insert_at_begin(32)
    # l.insert_at_begin(3421)
    l.insert_at_end(38)
    l.insert_at_end(362)
    l.insert_at_end(32)
    l.insert_at_end(9120)
    l.head.next.next.next = l.head
    if l.detect_loop():
        print('LOOP')
    else:
        print('No Loop')
    # l.print_linked_list()
    # l.length()
    # l.delete_node(3)
    # l.print_linked_list()




# class bst:
#     def __init__(self, data):
#         self.data = data
#         self.l= None
#         self.r = None

#     def add(self,data):
#         if data == self.data:
#             return
#         if data < self.data:
#             if self.l!= None:
#                 self.l.add(data)
#             else:
#                 self.l =bst(data)
#         else:
#             if self.r!= None:
#                 self.r.add(data)
#             else:
#                 self.r =bst(data)
    
#     def inorder(self):
#         ele = []
#         if self.l!= None:
#             ele+= self.l.inorder()

#         ele.append(self.data)

#         return ele