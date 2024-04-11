


FRAME_NUM = 4 #size of physical memory

#prints the memory and number of page faults every step of the refrence string
def print_step(page_faults, step, page, fault, phy_mem):
	print(f"Step {step}:")
	print(f"\tAccessing Page: {page} ", end='')
	if fault:
		print("(Fault)", end='')
	print("")
	print(f"\tFault Number: {page_faults}")
	
	print("\tMemory:\n\t| ", end='')
	for x in range(0, FRAME_NUM):
		if x < len(phy_mem): #filled memory
			print(f"{phy_mem[x]} | " , end='')
		else: #empty memory
			print("  | " , end='')
	print("")
			
#Least Recently Used
#the idea is to keep index 0 of tracking the least recenty used page by moving pages to the far right every time they're used
def LRU(ref_str):
	phy_mem = [] #representaion of the physical memory
	tracking = [] #keeps track of what page is being removed next (is used so physical memory doesn't shift in order)
	page_faults = 0
	step = 1
	print("_______Performing LRU________")
	for page in ref_str: #go through refrence string
		fault = False
		if page not in phy_mem: #page fault occurs
			page_faults += 1 #increment page fault
			fault = True #used so the print function knows to print it was a fault
			if len(phy_mem) < FRAME_NUM: #if there is space in memory
				phy_mem.append(page) #add the page to memory
				tracking.append(page) 
			else: #if memory is full, replace a page in memory
				phy_mem[phy_mem.index(tracking[0])] = page #remove the page that is index 0 in tracking
				tracking.pop(0) #remove the page from tracking
				tracking.append(page) #put the new page in the front of tracking since its the most recently used
		else: #page hit
			tracking.remove(page) 
			tracking.append(page) #move the page to the front of tracking, to indicate it is the most recently used page
		print_step(page_faults, step, page, fault, phy_mem) #print the step
		step += 1
	print(f"Total Page Faults: {page_faults}")
	print("_________Ending LRU__________")
	

#First In First Out
#By adding every new page to the far right of tracking, the oldest page (first in) will always be at index 0
def FIFO(ref_str):
	phy_mem = [] #representaion of the physical memory
	tracking = []
	page_faults = 0
	step = 1
	print("_______Performing FIFO_______")
	for page in ref_str:
		fault = False
		if page not in phy_mem: #page fault occurs
			page_faults += 1
			fault = True #used so the print function knows to print it was a fault
			if len(phy_mem) < FRAME_NUM: #if there is space in memory
				phy_mem.append(page) #add the page to memory
				tracking.append(page)
			else:
				phy_mem[phy_mem.index(tracking[0])] = page #remove the page that is index 0 in tracking
				tracking.pop(0) #remove the page from tracking since t was removed from phy_mem
				tracking.append(page) #add the new page to tracking
		print_step(page_faults, step, page, fault, phy_mem) #print the step
		step += 1
	print(f"Total Page Faults: {page_faults}")
	print("_________Ending FIFO_________")
		
#Optimal
#searches the refrence string for the next FRAME_NUM-1 pages in physical memory to be used then removes the one page in physical memory that was left out of that
def optimal(ref_str):
	phy_mem = [] #representaion of the physical memory
	page_faults = 0
	step = 1
	print("______Performing Optimal_____")
	for page in ref_str:
		fault = False
		if page not in phy_mem: #page fault occurs
			page_faults += 1
			fault = True #used so the print function knows to print it was a fault
			if len(phy_mem) < FRAME_NUM: #if there is space in memory
				phy_mem.append(page) #add the page to memory
			else:
				x = 0
				tracking = [] #holds the pages in phy_mem that are going to be called be the ref_str in the future
				while len(tracking) < FRAME_NUM-1 and step+x < len(ref_str): #loop until every page but one from physical memory has been found in the refrence string (or the end of the refrence string is reached)
					if ref_str[step+x] in phy_mem: #if the referenc string is going to call a page currently in memory
						tracking.append(ref_str[step+x]) #save that information
					x += 1 #check next page in the refrence string
				for frame in phy_mem: #go through each frame in physical memary
					if frame not in tracking: #if this frame is the one that was left out of tracking
						phy_mem[phy_mem.index(frame)] = page #replace it with the new frame
						break
		print_step(page_faults, step, page, fault, phy_mem) #print the step
		step += 1
	print(f"Total Page Faults: {page_faults}")
	print("________Ending Optimal_______")



ref_str = "1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5"
ref_str = ref_str.replace(" ", "")
ref_str = ref_str.split(",")

LRU(ref_str)
FIFO(ref_str)
optimal(ref_str)
