#!/usr/bin/env python3
"""Persistent immutable linked list."""
import sys
class Cons:
    def __init__(self,head,tail=None):self.head=head;self.tail=tail
    def __iter__(self):n=self;
    while n:yield n.head;n=n.tail
def cons(h,t=None):return Cons(h,t)
def to_list(c):return list(c) if c else[]
def prepend(x,lst):return Cons(x,lst)
def head(lst):return lst.head if lst else None
def tail(lst):return lst.tail if lst else None
def length(lst):n=0;c=lst;
while c:n+=1;c=c.tail
return n
def reverse(lst):
    r=None
    for x in lst:r=Cons(x,r)
    return r
def main():
    if len(sys.argv)>1 and sys.argv[1]=='--test':
        a=cons(1,cons(2,cons(3)));assert to_list(a)==[1,2,3]
        b=prepend(0,a);assert to_list(b)==[0,1,2,3]
        assert to_list(a)==[1,2,3]
        assert head(a)==1 and to_list(tail(a))==[2,3]
        assert length(a)==3 and to_list(reverse(a))==[3,2,1]
        print('All tests passed!')
    else:print(to_list(cons(1,cons(2,cons(3)))))
if __name__=='__main__':main()
