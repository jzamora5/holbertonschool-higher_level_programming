#!/usr/bin/python3
class Node:
    """ Defines a node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ Class Constructor """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data Getter """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ data Setter """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ next_node Getter """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ next_node Setter """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Defines a singly linked list """
    def __init__(self):
        """ Class Constructor """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position
         in the list(Increasing order)"""

        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp1 = self.__head
            tmp2 = tmp1.next_node
            while (tmp1 and tmp2 and (tmp2.data < value)):
                tmp1 = tmp1.next_node
                tmp2 = tmp1.next_node

            new_node.next_node = tmp2
            tmp1.next_node = new_node

    def __str__(self):
        """ Prints singly linked list """
        tmp = self.__head
        sllstr = ""
        while (tmp):
            sllstr += str(tmp.data)
            tmp = tmp.next_node
            if (tmp):
                sllstr += "\n"
        return (sllstr)
