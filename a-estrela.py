#destination: MAR
#TO-DO: Run 'pip install opencv-python' on CMD
import cv2
image = cv2.imread('grafo_franca(pins).png')

#list of adjacences (COORDINATES)
list_adj = [[["CAL","LIL"] , [432,28,508,56]] # [["A","B"], [Xa, Ya, Xb, Yb]]
,[["CAL", "AMI"] , [432,28,455,105]]
,[["LIL", "MET"] , [508,56,689,190]]
,[["LIL", "AMI"] , [508,56,455,105]]
,[["LIL", "PAR"] , [508,56,462,218]]
,[["MET", "STR"] , [689,190,803,245]]
,[["MET", "DIJ"] , [689,190,640,355]]
,[["MET", "PAR"] , [689,190,462,218]]
,[["STR", "DIJ"] , [803,245,640,355]]
,[["STR", "LYO"] , [803,245,615,488]]
,[["LYO", "DIJ"] , [615,488,640,355]]
,[["LYO", "BOU"] , [615,488,459,377]]
,[["LYO", "STE"] , [615,488,596,526]]
,[["LYO", "AVI"] , [615,488,620,666]]
,[["LYO", "NIC"] , [615,488,767,701]]
,[["NIC", "AVI"] , [767,701,620,666]]
,[["NIC", "MAR"] , [767,701,655,726]]
,[["MAR", "AVI"] , [655,726,620,666]]
,[["AVI", "TOU"] , [620,666,410,699]]
,[["TOU", "STE"] , [410,699,596,526]]
,[["TOU", "BOR"] , [410,699,281,580]]
,[["BOR", "STE"] , [281,580,596,526]]
,[["BOR", "LAR"] , [281,580,244,466]]
,[["LAR", "BOU"] , [244,466,459,377]]
,[["LAR", "NAN"] , [244,466,218,357]]
,[["NAN", "REN"] , [218,357,213,285]]
,[["REN", "ORL"] , [213,285,433,297]]
,[["REN", "CAE"] , [213,285,294,192]]
,[["CAE", "PAR"] , [294,192,462,218]]
,[["CAE", "LEH"] , [294,192,331,149]]
,[["LEH", "PAR"] , [331,149,462,218]]
,[["LEH", "AMI"] , [331,149,455,105]]
,[["AMI", "PAR"] , [455,105,462,218]]
,[["PAR", "ORL"] , [462,218,433,297]]
,[["ORL", "BOU"] , [433,297,459,377]]
,[["BOU", "DIJ"] , [459,377,640,355]]
,[["BOU", "LYO"] , [459,377,615,488]]
,[["STE", "LYO"] , [596,526,615,488]]]

#----------------------------------------------------

CAL =  {"name":"CAL", "adj":["AMI", "LIL"], "dist":[122.14, 91.27]} #CAL
LIL =  {"name":"LIL", "adj":["CAL", "AMI", "PAR", "MET"], "dist":[91.27,95.68,205.56,280.15]}#LIL
AMI =  {"name":"AMI", "adj":["CAL", "LIL", "PAR", "LEH"], "dist":[122.14,95.68,117.89,162.39]}#AMI
Le_Havre =  {"name":"LEH", "adj":["AMI", "PAR", "CAE"], "dist":[162.39,178.41,49.56]}#LEH
CAE =  {"name":"CAE", "adj":["LEH", "PAR", "REN"], "dist":[49.56,201.85,152.58]}#CAE
MET =  {"name":"MET", "adj":["LIL", "PAR", "DIJ", "STR"], "dist":[280.15,279.86,214.9,129.82]}#MET
PAR = {"name":"PAR", "adj":["AMI", "LIL", "MET", "ORL", "CAE", "LEH"], "dist":[117.89, 205.56, 279.86,107.5,201.85,178.41]}#PAR
REN =  {"name":"REN", "adj":["CAE", "ORL", "NAN"], "dist":[152.58, 268.94, 99.65]}#REN
ORL =  {"name":"ORL", "adj":["PAR", "REN", "BOU"], "dist":[107.5, 268.94,98.28]}#ORL
STR =  {"name":"STR", "adj":["MET", "DIJ", "LYO"], "dist":[129.82,243.05,381.75]}#STR
NAN =  {"name":"NAN", "adj":["REN", "LAR"], "dist":[99.65,121.32]}#NAN
BOU = {"name":"BOU", "adj":["ORL", "DIJ", "LYO", "LAR"], "dist":[98.28, 201.93, 237.98,288.32]}#BOU
DIJ = {"name":"DIJ", "adj":["MET", "STR", "LYO", "BOU"], "dist":[214.9,243.05,173.84,201.93]}#DIJ
La_Rochelle = {"name":"LAR", "adj":["NAN", "BOR"], "dist":[121.32,152.46]}#LAR
BOR = {"name":"BOR", "adj":["LAR", "STE", "TOU"], "dist":[152.46,395.48,211.43]}#BOR
St_Etienne = {"name":"STE", "adj":["BOR", "TOU", "LYO"], "dist":[395.48,314.15,49.67]}#STE
LYO = {"name":"LYO", "adj":["BOU", "DIJ", "STR", "NIC", "AVI", "STE"], "dist":[237.98,173.84,381.75,297.23,201.71,49.67]} #LYO
TOU = {"name":"TOU", "adj":["BOR", "STE", "AVI"], "dist":[211.43, 314.15,274.17]}#TOU
AVI = {"name":"AVI", "adj":["TOU", "LYO", "NIC", "MAR"], "dist":[274.17,201.71,197.44,81.6]}#AVI
NIC = {"name":"NIC", "adj":["MAR", "AVI", "LYO"], "dist":[159.02, 197.44, 297.23]}#NIC
MAR = {"name":"MAR", "adj":["AVI", "NIC"], "dist":[81.6, 159.02]}#MAR

nodes = {"CAL": CAL, "LIL": LIL, "AMI": AMI, "LEH": Le_Havre,
"CAE": CAE, "MET": MET, "PAR": PAR, "REN": REN, "ORL": ORL, "STR":STR, "NAN":NAN,
"BOU":BOU, "DIJ": DIJ, "LAR":La_Rochelle, "BOR":BOR, "STE":St_Etienne,"LYO": LYO, "TOU":TOU,
"AVI":AVI,"NIC":NIC,"MAR":MAR}

heuristic = {"CAL":890.59, "LIL":832.45, "AMI":768.69, "LEH":796.98, "CAE":787.53,"MET":649.03,"PAR":659.4,"REN":764.26,
"ORL":577.16,"STR":613.55,"NAN":696.16,"BOU":475.15,"DIJ":441.84,"LAR":615.94,"BOR":501.12,"STE":251.17,"LYO":274.93,
"TOU":318.32,"AVI":81.6,"NIC":159.02,"MAR":0} #distance from each node to the destination in straight line
curr_adj = [] #adjacent nodes of the currrent node
f_ns = [] #list of the evaluation functions for each adjacent of the current node
dist_acc = 0 #distance accumulated from the first node to the current
path = [] #list of the cities that compound the shortest path
nodes_adj = [] #pair of nodes that compound an adjacence

stop = False
origin = "CAL"
curr = nodes[origin] #the first node
path.append(origin)
curr_adj = curr["adj"]
dest = nodes["MAR"] #destination
nodes_adj.append(origin) 

print("Origin: " + origin)
print("********************************")
while not stop:
    i = 0
    for node in curr_adj:
         f_ns.append(heuristic[node]+(curr["dist"][i]+dist_acc))
         i += 1
    for node in curr_adj:
         if(node == dest["name"]):
             stop = True
             print("The shorter path was found")
    print(curr_adj)
    print(f_ns)
    aux = f_ns[0]
    index_less = 0 #the index of the current less value of f_ns
    i = 0
    for value in f_ns:
        if(value < aux):
            aux = value
            index_less = i
        i += 1
    dist_acc += curr["dist"][index_less]
    curr = nodes[curr_adj[index_less]]
    nodes_adj.append(curr["name"])
    for pair in list_adj: 
        if((nodes_adj[0] in pair[0]) and (nodes_adj[1] in pair[0])):
            cv2.line(image, (pair[1][0], pair[1][1]), (pair[1][2], pair[1][3]), (0,0,255), 5) #draw the adjacence
    nodes_adj.pop(0)
    curr_adj = curr["adj"]
    f_ns.clear()
    path.append(curr["name"])
    print("f(n) = " + str(aux) + " -> " + curr["name"])
    print("---------------------------------")
    if(len(curr_adj) == 0):
        stop = True
        print("The shortest path was not found")
print(path)
print("Shortest distance:" + str(dist_acc))

cv2.namedWindow("image", cv2.WINDOW_NORMAL) #create window with freedom of dimensions
cv2.imshow("image", image)
cv2.resizeWindow("image", 581, 593) #reduce the dimensions of the original file to 70% (to fit to the screen)
cv2.waitKey(0)
cv2.destroyAllWindows()