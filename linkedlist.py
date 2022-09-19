class LinkedNode:
    """
    Singular node object containing a linked object
    and this node's stored data
    """
    def __init__(self, obj):
        self.obj = obj
        self.next = None
    
    def __str__(self):
        return str(self.obj)
        
class LinkedList:
    """
    A Linked List containing a list of nodes without random access.
    Access to an internal node requires starting at the head node of
    the list.
    """
    def __init__(self):
        self.head = None
        
    def push_front(self, obj):
        """
        Add an object to the front of the linked list

        Parameters
        ----------
        obj: Object
            Object to add to the list
        """
        # Convert obj to a LinkedNode object
        n = LinkedNode(obj)
        # Make new node point to current node at head of linked list
        n.next = self.head
        # Make head of linked list point to the new node
        self.head = n
        
    def pop_front(self):
        """
        Remove the first object from the linked list and return it

        Returns
        -------
        object
        """
        ret = None
        if self.head:
            ret = self.head.obj
            self.head = self.head.next
        return ret
    
    def contains(self, obj):
        """
        Check if a given object is in the linked ist

        Parameters
        ----------
        obj: object
            Object to look for
        
        Returns
        -------
        True if object is in the list, False otherwise
        """
        node = self.head
        found = False
        while node and not found:
            if node.obj == obj:
                found = True
            else:
                node = node.next
        return found


    def remove(self, obj):
        """
        Remove and return object from the linked list if it exists

        Parameters
        ----------
        obj: object
            The object to remove
        
        Returns
        -------
        None if the object isn't there, or obj if it has been removed
        """
        # Removing a node within the head
        ret = None
        if self.head:
            if self.head.obj == obj:
                ret = self.pop_front()
            else:
                prev = self.head
                node = self.head.next
                found = False
                # Removing a node within the body, with early abandoning
                while node and not found:
                    if node.obj == obj:
                        prev.next = node.next
                        found = True
                        ret = obj
                    else:
                        prev = node
                        node = node.next
        return ret
    
    def __str__(self):
        """
        For each node, print the node's data separated by an '->' sign.
        """
        temp = self.head
        res = ""
        # for each node
        while temp:
            res += str(temp)
            if temp is not None:
                res += " ==> "
            temp = temp.next
        return res

if __name__ == '__main__':
    L = LinkedList()
    L.push_front("Theo")
    L.push_front("Elsie")
    L.push_front("Darcy")
    print(L.pop_front())
    L.push_front("Layla")
    print(L)
    L.remove("Layla")
    print(L)
    print(L.contains("Theo"))
    print(L.contains("Layla"))