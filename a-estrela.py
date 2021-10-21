#destination: MAR
#TO-DO: Run 'pip install opencv-python' on CMD
import cv2
import math
import numpy as np
image = cv2.imread('.\grafo_franca_full(pins).png',1)

#coordinates ----------------------
coord = [[1122 , 159] #LIL coord[0]
,[1029 , 298] #AMI coord[1]
,[874 , 379] #ROU coord[2]
,[692 , 428] #CAE coord[3]
,[1029 , 489] #PAR coord[4]
,[1281 , 473] #CHA coord[5]
,[1508 , 441] #MET coord[6]
,[1714 , 548] #STR coord[7]
,[520 , 619] #REN coord[8]
,[974 , 651] #ORL coord[9]
,[1380 , 765] #DIJ coord[10]
,[1497 , 784] #BES coord[11]
,[530 , 784] #NAN coord[12]
,[778 , 904] #POI coord[13]
,[892 , 1034] #LIM coord[14]
,[1343 , 1044] #LYO coord[15]
,[661 , 1222] #BOR coord[16]
,[916 , 1446] #TOU coord[17]
,[1212 , 1446] #MON coord[18]
,[1415 , 1501] #MAR coord[19]
]

#dictionary of lists with the heuristics and the coordinates for each node--------------------------------------------

heuristic = {"LIL":[0,coord[0]] #[distance from each node to the destination in straight line (heuristic), coordinate of the node]
,"AMI":[0,coord[1]]
,"ROU":[0,coord[2]]
,"CAE":[0,coord[3]]
,"PAR":[0,coord[4]]
,"CHA":[0,coord[5]]
,"MET":[0,coord[6]]
,"STR":[0,coord[7]]
,"REN":[0,coord[8]]
,"ORL":[0,coord[9]]
,"DIJ":[0,coord[10]]
,"BES":[0,coord[11]]
,"NAN":[0,coord[12]]
,"POI":[0,coord[13]]
,"LIM":[0,coord[14]]
,"LYO":[0,coord[15]]
,"BOR":[0,coord[16]]
,"TOU":[0,coord[17]]
,"MON":[0,coord[18]]
,"MAR":[0,coord[19]]} 

#list of adjacences (COORDINATES) ------------------------------------------------------------------------------
list_adj = [[["LIL", "AMI"] , [coord[0][0],coord[0][1],coord[1][0],coord[1][1]]] # [["A","B"], [Xa, Ya, Xb, Yb]]
,[["ROU", "AMI"] , [coord[2][0],coord[2][1],coord[1][0],coord[1][1]]]
,[["PAR", "AMI"] , [coord[4][0],coord[4][1],coord[1][0],coord[1][1]]]
,[["CHA", "AMI"] , [coord[5][0],coord[5][1],coord[1][0],coord[1][1]]]
,[["PAR", "ROU"] , [coord[4][0],coord[4][1],coord[2][0],coord[2][1]]]
,[["CAE", "ROU"] , [coord[3][0],coord[3][1],coord[2][0],coord[2][1]]]
,[["PAR", "CAE"] , [coord[4][0],coord[4][1],coord[3][0],coord[3][1]]]
,[["PAR", "CHA"] , [coord[4][0],coord[4][1],coord[5][0],coord[5][1]]]
,[["PAR", "DIJ"] , [coord[4][0],coord[4][1],coord[10][0],coord[10][1]]]
,[["PAR", "LYO"] , [coord[4][0],coord[4][1],coord[15][0],coord[15][1]]]
,[["PAR", "ORL"] , [coord[4][0],coord[4][1],coord[9][0],coord[9][1]]]
,[["ORL", "REN"] , [coord[9][0],coord[9][1],coord[8][0],coord[8][1]]]
,[["ORL", "POI"] , [coord[9][0],coord[9][1],coord[13][0],coord[13][1]]]
,[["ORL", "LIM"] , [coord[9][0],coord[9][1],coord[14][0],coord[14][1]]]
,[["CHA", "MET"] , [coord[5][0],coord[5][1],coord[6][0],coord[6][1]]]
,[["CHA", "DIJ"] , [coord[5][0],coord[5][1],coord[10][0],coord[10][1]]]
,[["DIJ", "MET"] , [coord[10][0],coord[10][1],coord[6][0],coord[6][1]]]
,[["DIJ", "BES"] , [coord[10][0],coord[10][1],coord[11][0],coord[11][1]]]
,[["MET", "STR"] , [coord[6][0],coord[6][1],coord[7][0],coord[7][1]]]
,[["STR", "BES"] , [coord[7][0],coord[7][1],coord[11][0],coord[11][1]]]
,[["LYO", "BES"] , [coord[15][0],coord[15][1],coord[11][0],coord[11][1]]]
,[["LYO", "LIM"] , [coord[15][0],coord[15][1],coord[14][0],coord[14][1]]]
,[["LYO", "MON"] , [coord[15][0],coord[15][1],coord[18][0],coord[18][1]]]
,[["LYO", "MAR"] , [coord[15][0],coord[15][1],coord[19][0],coord[19][1]]]
,[["LIM", "TOU"] , [coord[14][0],coord[14][1],coord[17][0],coord[17][1]]]
,[["LIM", "BOR"] , [coord[14][0],coord[14][1],coord[16][0],coord[16][1]]]
,[["LIM", "POI"] , [coord[14][0],coord[14][1],coord[13][0],coord[13][1]]]
,[["TOU", "BOR"] , [coord[17][0],coord[17][1],coord[16][0],coord[16][1]]]
,[["TOU", "MON"] , [coord[17][0],coord[17][1],coord[18][0],coord[18][1]]]
,[["MON", "MAR"] , [coord[18][0],coord[18][1],coord[19][0],coord[19][1]]]
,[["POI", "NAN"] , [coord[13][0],coord[13][1],coord[12][0],coord[12][1]]]
,[["NAN", "REN"] , [coord[12][0],coord[12][1],coord[8][0],coord[8][1]]]
,[["CAE", "REN"] , [coord[3][0],coord[3][1],coord[8][0],coord[8][1]]]
]

#Dictionaries with the real distances from each city to its adjacents -----------------------------------------------------------

LIL =  {"name":"LIL", "adj":["AMI"], "dist":[140.5]}#LIL
AMI =  {"name":"AMI", "adj":["ROU", "CHA", "LIL", "PAR"], "dist":[119.9,218.5,140.5,163.2]}#AMI
CAE =  {"name":"CAE", "adj":["PAR", "ROU", "REN"], "dist":[239.5,132.2,184.6]}#CAE
MET =  {"name":"MET", "adj":["CHA","STR","DIJ"], "dist":[157.1,166.4,269.9]}#MET
PAR = {"name":"PAR", "adj":["ROU", "CHA", "CAE", "ORL", "LYO", "DIJ", "AMI"], "dist":[135.7,187.5,239.5,132.4,391,262,163.2]}#PAR
REN =  {"name":"REN", "adj":["NAN", "CAE", "ORL"], "dist":[113.4,184.6,307.2]}#REN
ORL =  {"name":"ORL", "adj":["REN","PAR","LIM","POI"], "dist":[307.2,132.4,269.6,224.5]}#ORL
STR =  {"name":"STR", "adj":["MET","BES"], "dist":[166.4,242.5]}#STR
NAN =  {"name":"NAN", "adj":["POI", "REN"], "dist":[218.8,113.4]}#NAN
DIJ = {"name":"DIJ", "adj":["MET","CHA","BES","PAR"], "dist":[269.9,258.9,92.9,262]}#DIJ
BOR = {"name":"BOR", "adj":["LIM", "TOU"], "dist":[221.1,244.9]}#BOR
LYO = {"name":"LYO", "adj":["MON","MAR","PAR","BES","LIM"], "dist":[304.2,313.7,391,226.7,411.5]} #LYO
TOU = {"name":"TOU", "adj":["LIM","BOR","MON"], "dist":[290.1,244.9,242.8]}#TOU
MAR = {"name":"MAR", "adj":["MON","LYO"], "dist":[170.0, 313.7]}#MAR
ROU = {"name":"ROU", "adj":["AMI", "PAR", "CAE"], "dist":[119.9,135.7,132.2]}#ROU
CHA = {"name":"CHA", "adj":["PAR","AMI","DIJ","MET"], "dist":[187.5,218.5,258.9,157.1]}#CHA
POI = {"name":"POI", "adj":["NAN", "LIM", "ORL"],"dist":[218.8,133.6,224.5]} #POI
LIM = {"name":"LIM", "adj":["BOR","POI","TOU","LYO","ORL"],"dist":[221.1,133.6,290.1,411.5,269.6]} #LIM
MON = {"name":"MON", "adj":["TOU","MAR","LYO"],"dist":[242.8,170.0,302.9]} #MON
BES = {"name":"BES", "adj":["DIJ","STR","LYO"],"dist":[92.9,242.5,226.7]} #BES


# function that calculates the heuristics---------------------------------------------

def calc_heuristics(destination): #destination -> str
    for key in heuristic: 
        if (key != destination):
            # initializing points in  numpy arrays
            xo = heuristic[key][1][0] #x origin
            yo = heuristic[key][1][1] #y origin
            xd = heuristic[destination][1][0] #x destination
            yd = heuristic[destination][1][1] #y destination
            point1 = np.array((xo,yo)) #origin node and its coordinates
            point2 = np.array((xd,yd)) #destination node and its coordinates
 
            # calculating Euclidean distance using linalg.norm()
            dist = np.linalg.norm(point1 - point2)
            #dist = math.sqrt(math.pow(abs(xd-xo),2)+math.pow(abs(yd-yo),2))
            
            #put the heuristic in the first field of the list (see the definition of the dictionary "heuristic")
            heuristic[key][0] = round(dist*0.6,2) #1px ~ 0.6 km; convert the distance in pixels to a distance in kilometers
        elif (key == destination):
            heuristic[key][0] = 0 #the distance from the destination to the destination

#function that print the distances----------------------------------------------------

def print_dist(xo,yo,xd,yd,dist):
    xc = 0
    yc = 0
    dist_xd_xo = abs(xd-xo)
    dist_yd_yo = abs(yd-yo)
    if(xd >= xo):
        xc = xo+(dist_xd_xo/2)
    else:
        xc = xd+(dist_xd_xo/2)
    if(yd >= yo):
        yc = yo+(dist_yd_yo/2)
    else:
        yc = yd+(dist_yd_yo/2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, str(dist), (int(xc),int(yc)), font,
					1, (255, 0, 0), 2)



#dictionary with the nodes 

nodes = {"LIL":LIL 
,"AMI": AMI
,"ROU": ROU
,"CAE": CAE
,"PAR": PAR
,"CHA": CHA
,"MET": MET
,"STR": STR
,"REN": REN
,"ORL": ORL
,"DIJ": DIJ
,"BES": BES
,"NAN": NAN
,"POI": POI
,"LIM": LIM
,"LYO": LYO
,"BOR": BOR
,"TOU": TOU
,"MON": MON
,"MAR": MAR} 


curr_adj = [] #adjacent nodes of the currrent node
f_ns = [] #list of the evaluation functions for each adjacent of the current node
dist_acc = 0 #distance accumulated from the first node to the current
path = [] #list of the cities that compound the shortest path
to_visit = [] #list of the nodes to visit in each iteration
nodes_adj = [] #pair of nodes that compound an adjacence

stop = False #to stop the main while

print("LIL,AMI,ROU,CAE,PAR,CHA,MET,STR,REN,ORL,\nDIJ,BES,NAN,POI,LIM,LYO,BOR,TOU,MON,MAR")

origin = input("Type the origin: ") #LIL, AMI, ...
dest = input("Type the destination:") #LIL, AMI, ...

origin = origin.upper()
dest = dest.upper()

calc_heuristics(dest)

curr = nodes[origin] #the first node (and the current node for each iteration)
path.append(origin)
curr_adj = curr["adj"]
nodes_adj.append(origin) 

print("\nOrigin: " + origin)
print("*********************************\n")

if(curr["name"] == dest): #if the user typed the destination
    print("You typed the destination")
    stop = True

while not stop:
    i = 0
    for node in curr_adj:
        if(not(node in path)): #if the node was not visited
            f_ns.append(round(heuristic[node][0]+(curr["dist"][i]+dist_acc),2))
            to_visit.append(node)
            print(node + ":" + str(heuristic[node][0]))
        i += 1
    if (len(to_visit) == 0):
        stop = True
        print("**The shortest path cannot be found**")
    print(to_visit)
    print(f_ns)
    aux = f_ns[0]
    index_less = 0 #the index of the current less value of f_ns
    i = 0
    for value in f_ns:
        if(value < aux):
            aux = value
            index_less = i
        i += 1
    dist_acc += curr["dist"][curr["adj"].index(to_visit[index_less])]
    curr = nodes[to_visit[index_less]]
    nodes_adj.append(curr["name"])
    for pair in list_adj: 
        if((nodes_adj[0] in pair[0]) and (nodes_adj[1] in pair[0])):
            cv2.line(image, (pair[1][0], pair[1][1]), (pair[1][2], pair[1][3]), (0,0,255), 5) #draw the adjacence
            print_dist(pair[1][0], pair[1][1], pair[1][2], pair[1][3], round(dist_acc,2))
    nodes_adj.pop(0)
    curr_adj = curr["adj"]
    path.append(curr["name"])
    print("f(n) = " + str(aux) + " -> " + curr["name"])
    for node in to_visit:
         if(node == dest):
             stop = True
             print("**The destination was found**")
             break
    print("---------------------------------")
    f_ns.clear()
    to_visit.clear()

print(path)
print("Shortest distance:" + str(dist_acc))

cv2.namedWindow("image", cv2.WINDOW_NORMAL) #create window with freedom of dimensions
cv2.imshow("image", image)
cv2.resizeWindow("image", 1000, 961) #reduce the dimensions of the original file to 50% (to fit to the screen)
cv2.waitKey(0)
cv2.destroyAllWindows()

