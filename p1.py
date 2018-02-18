class Anode:
	def __init__(self,key):
		self.key=key
		self.next=None
class Graph:
	def __init__(self,n):
		self.n=n;
		self.alist=[[] for i in range(n)]			#adjacency list
		self.noie=[0 for i in range(n)]				#no of incoming edges
		self.sourceset=[]
		self.active=[True for i in range(n)]		#active flag set
		self.nosem=1								#number of sems
	def insert(self):
		e=int(input("enter the number of edges:"))
		print("enter the edges:")
		for i in range(e):
			str=input()
			str=str.split()
			left=int(str[0])
			right=int(str[1])
			self.alist[left].append(right)
			self.noie[right]=self.noie[right]+1
		for i in range(self.n):
			if self.noie[i]==0:
				self.sourceset.append(i)
		y=len(self.sourceset)			#number of courses in the present sem
		z=0								#z number of courses for the next sem				
		while(len(self.sourceset)!=0):
			if(y==0):
				self.nosem=self.nosem+1
				y=z
				z=0
			y=y-1
			x=self.sourceset.pop(0)
			self.active[x]=False
			for i in range(len(self.alist[x])):						
			
				if self.active[self.alist[x][i]]==True:						#self.alist[x][i] adjacent verteices
					self.noie[self.alist[x][i]]=self.noie[self.alist[x][i]]-1
					if(self.noie[self.alist[x][i]]==0):
						z=z+1
						self.sourceset.append(self.alist[x][i])
				print(self.noie)
		return self.nosem


		





def main():
	n=int(input("enter the number of vertices:"))
	t=Graph(n)
	print(t.insert())
	
main()
