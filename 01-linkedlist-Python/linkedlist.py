"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        if(self.head!=None):
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_element
        else:
            head=new_element       
    def get_position(self, position):
        temp=self.head
        count=1
        if(self.head!=None):
            while(temp!=None and count<position):

                print(temp.value,count)
                temp=temp.next
                count=count+1
            if(count==position):
                return temp
            return None
        else:
            return None
    def insert(self, new_element, position):
        temp=self.head
        count=1
        if(position==1):
            new_element.next=head
            head=new_element
        else:
            while(temp.next!=None and count<position-1):
                temp=temp.next
                count=count+1
            new_element.next=temp.next
            temp.next=new_element
    def delete(self, value):
        temp=self.head
        count=1
        if(self.head!=None):
            if(temp.value==value):
                self.head=self.head.next
            else:
                while(temp.next.next!=None and temp.next.value!=value):
                    temp=temp.next
                    count=count+1
                
                temp.next=temp.next.next