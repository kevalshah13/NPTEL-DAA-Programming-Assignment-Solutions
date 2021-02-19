n,a,b=map(int,input().split())
#print(n)
pair = []
weights = []
adjlist ={}
visited = []
distance = []
check=[]
large=-1
if n>0:
    for i in range(1,n+1):
        l,w,m=map(int,input().split())
        if large<l:
            large=l
        if large<m:
            large=m
            
        pair.append([l,w,m])
        weights.append(w)
        
    #print(pair)
    infinite = sum(weights)+1
    for i in range(1,large+1):
        adjlist[i]={}
        visited.append(0)
        distance.append(infinite)
    #print(adjlist)
    for i in pair:
        adjlist[i[0]][i[2]]=i[1]
        adjlist[i[2]][i[0]]=i[1]
    #print(adjlist)
    #print(distance)
    if(len(adjlist[a])!=0 or len(adjlist[b])!=0):
        distance[a-1]=0
        #lowest=0
        for i in range(1,large+1):
            min_dist=infinite
            for u in range(1,large+1):
                if(visited[u-1]==0 and distance[u-1]<min_dist):
                    min_dist=distance[u-1]
                    curr_vertex=u
            visited[curr_vertex-1]=1
            for edge in adjlist[curr_vertex]:
                if(visited[edge-1]==0):
                    if(distance[edge-1]>distance[curr_vertex-1]+adjlist[curr_vertex][edge]):
                        distance[edge-1]=distance[curr_vertex-1]+adjlist[curr_vertex][edge]
        if(distance[b-1]!=infinite):
            print("YES")
            print(distance[b-1])
        else:
            print("NO")

    else:
        print("NO")

#print(distance)
#print(visited)
