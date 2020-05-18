from list_node import *
class Person:
    '''this class is to set name as host
    and get host's friends
    '''
    def __init__(self, name):
        self._name=name
        self._friends = None
    def get_name(self):
        return self._name
    def get_friends(self):
        return self._friends
    def set_name(self,val):
        self._name=val
    def set_friends(self,val):

        self._friends = ListNode(val)
    def add_friend(self,name):
        '''make add_friend as a linklIst ( as the structure shows on the
        d2l) hold head as first firend, then add new friends as next.val
        add all friends as a linklist
        '''
        head = self._friends
        head.next = ListNode(name)
        self._friends = head



def construct_relationships(filename):
    '''this function is built link list and each value of
    linklist is name and thier friends.People start def as None
    linklist,it val equal to key of dictionary,if get_name is NOne
    it will set that name first then,add another name one by one as linklist
    for thier friends,if get_friends is None, set first firends,then add other friends
    as linklist. Finally, return the structure people.
    '''
    dict1=read_files(filename)
    people =ListNode(Person(None))
    temp=people
    for key in dict1:
        if temp.val.get_name() is None:
            temp.val.set_name(key)
        temp.next = ListNode(Person(key))
        temp=temp.next
        for string in dict1[key]:
            if temp.val.get_friends() is None:
                    temp.val.set_friends(string)
            else:
                temp.val.add_friend(string)

        #temp.next = ListNode(Person(key))



    return people
def find_mutual_friends(rel_list,name1,name2):
    '''for this function, first is find name1 and name2 in
    people, and return thier friends out. if friend1 also exsit in
    name2's friend, it will return as first mutual firends.comapre with
    each node of linklist and add mutual firends one by one and finally return
    out the mutual_friend
    '''

    head =rel_list
    friend1=None
    friend2=None
    while head is not None:
        #this while loop is to match the name in people
        if head.val.get_name()==name1:
            friend1=head.val.get_friends()
        if head.val.get_name()==name2:
            friend2=head.val.get_friends()
        head=head.next

    mutual_friend=None
    while friend1 is not None:
        #this function is to find mutual name by compare with firend1 each node
        # to firend2 each node
        temp=friend2
        while friend2 is not None:
            if friend1.val == friend2.val and mutual_friend==None:
                mutual_friend=ListNode(friend1.val)
            elif friend1.val == friend2.val:
                node=ListNode(friend2.val)
                node.next=mutual_friend
                mutual_friend.next=node
            friend2=friend2.next
        friend2 = temp
        friend1=friend1.next
    return mutual_friend

def read_files(filename):
    '''For this function, first readfile and
    split as list. and aslo create another list
    with swithch the position.and add all in total_name
    (2_list with all name) if string[0] not in dict dict[string[0]]
    equal to epmpty list and add string[1]in list. Finally return a
    dictionary with name and friends
    '''
    dict1={}
    total_name=[]
    name=[]
    reversed_name=[]
    #file_name='word_list_text.txt'
    file=open(filename,'r')
    for i in file:
        temp=[]
        y=i.strip().split()

        reversed_name.append([y[1],y[0]])
        for string in y:
            if string not in name:
                name.append(string)
        total_name.append(y)

    for i in reversed_name:
            total_name.append(i)


    for i in total_name:
            if i[0] not in dict1 :
                dict1[i[0]]=[]
                dict1[i[0]].append(i[1])
            else:
                dict1[i[0]].append(i[1])
    return dict1
def main():

    rel_list=construct_relationships(filename)
    find_mutual_friends(rel_list,name1,name2)
if __name__ == "__main__":
    main()