package main

import (
	"errors"
	"fmt"
	"unsafe"
)

type XORDoublyLinkedList struct {
	Head *XORLinkedListNode
	Tail *XORLinkedListNode
	Size int
}

func (ll *XORDoublyLinkedList) Add(element int) {
	node := &XORLinkedListNode{element, nil}
	if ll.Head == nil {
		ll.Head = node
		ll.Tail = node
	} else {
		node.Both = XOR(ll.Tail, nil)
		ll.Tail.Both = XOR(ll.Tail.Both, node)
		ll.Tail = node
	}
	ll.Size++
}

func (ll XORDoublyLinkedList) Get(index int) (*XORLinkedListNode, error) {
	if index >= ll.Size {
		return nil, errors.New("out of bounds")
	}
	var prev *XORLinkedListNode = nil
	var next *XORLinkedListNode = nil
	var curr = ll.Head
	for i := 0; i < index; i++ {
		next = curr.GetNext(prev)
		prev = curr
		curr = next
	}
	return curr, nil
}

type XORLinkedListNode struct {
	Value int
	Both  *XORLinkedListNode
}

func (node *XORLinkedListNode) GetNext(prev *XORLinkedListNode) *XORLinkedListNode {
	return XOR(prev, node.Both)
}

func XOR(prev, next *XORLinkedListNode) *XORLinkedListNode {
	temp := uintptr(unsafe.Pointer(prev)) ^ uintptr(unsafe.Pointer(next))
	return (*XORLinkedListNode)(unsafe.Pointer(temp))
}

func main() {
	ll := &XORDoublyLinkedList{}
	ll.Add(5)
	ll.Add(4)
	ll.Add(3)
	fmt.Println(ll.Get(0))
	fmt.Println(ll.Get(1))
	fmt.Println(ll.Get(2))
}
