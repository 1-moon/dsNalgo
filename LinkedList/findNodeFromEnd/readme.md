# What is this algorithm ?

`find_kth_from_end` function is designed to retrieve the kth node from the end of a LL.

## Description

let's consider a LL with the nodes:
1->2->3->4->5->6->7->8
If we wnat to find the 3rd node from the end (i.e. k = 3), 
this node will be 6.

## Key

Unlike previous examples where a fast pointer goes two steps at time using `.next`,
we are moving the fast ptr k nodes ahead.

`for _ in range(k) { fast= fast.next }`
This loop will advance the fast ptr k nodes forward, 
thereby creating a gap of k nodes between
`slow` and `fast`
