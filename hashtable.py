from linkedlist import *

class HashTable:
    """
    A hash table that stores an array of linked lists

    Parameters
    ----------
    n_buckets: int
        Number of buckets in the hash table
    """
    def __init__(self, n_buckets):
        # for each bucket, make a linked list
        self.buckets = list()
        self._n_buckets = n_buckets
        for _ in range(n_buckets):
            self.buckets.append(LinkedList())
    
    def contains(self, obj):
        """
        Identifies if a piece of data is in the hashmap
        by accessing the objects hashcode and checking that
        code's respective bucket.
        
        Params
        ------
        obj: a piece of hashable data
        
        Return
        ------
        res: boolean
            True if the object exists, or False otherwise
        
        """
        ## TODO: Fill this in
        return False
    
    def add(self, obj):
        """
        Add a piece of data to the hashmap
        by accessing the objects hashcode and making it the head
        of the existing linked list of that bucket.
        
        Params
        ------
        obj: a piece of hashable data        
        """
        ## TODO: Fill this in
        pass
    
    def remove(self, obj):
        """
        Remove and return object from the hash table if it exists

        Parameters
        ----------
        obj: object
            The object to remove
        
        Returns
        -------
        None if the object isn't there, or obj if it has been removed
        """
        ## TODO: Fill this in
        return None
    
    def __str__(self):
        """
        Return a string with all of the linked lists in the hash map
        """
        s = ""
        for i, l in enumerate(self.buckets):
            s += "{}: {}\n".format(i, l)
        return s