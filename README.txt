To Run:
    copy and paste HW4.py into https://www.onlinegdb.com/online_python_compiler
    insert reference string into the variable ref_str on line 109
   	 (needs to be a string with the numbers separated by commas)
    
    
    

I noticed this part was in the requirements:
"Assess the efficiency of the algorithms in terms of time complexity and resource usage. Consider factors such as the number of comparisons, memory accesses, and overall execution time"
so I guess I'll try to answer it here.

To be clear, I'm basing my answer off my own implementation of the algorithms.

Space complexity of the algorithms is pretty similar. The majority of the memory they use (beyond the physical memory) is the tracking list which usually contains an element for each frame of physical memory
(optimal's tracking list only ever goes up to frame - 1 in size but that's hardly a difference, especially since it uses an extra integer for iteration)


The time complexity of FIFO is probably the best of the three.
It has to rearrange the elements of the tracking array in memory whenever the first element get popped during page faults

The time complexity of LRU is the same thing except on page hits it has to iterate through tracking to remove the hit page, then rearrange the following elements in memory which makes it slower than FIFO

In hindsight, a linked list with a head and tail pointer may have been a more efficient way to implement the tracking array for these two, since I'm only really directly accessing the first or last element
Even when I access a middle element, its for a remove that's probably iterating over the list anyways.
(Although, with array's better locatilty for CPU caching, array might still end up being faster, not sure to be honest)

Optimal struggles with time complexity as it has to, at worst, iterate over the entire remaining reference string every page fault.
Then it proceeds to iterate over both the physical memory and the tracking array, so like, there's just a lot of iterating over arrays on every page fault
Also, it probably easily makes way more comparisons than the other two.

