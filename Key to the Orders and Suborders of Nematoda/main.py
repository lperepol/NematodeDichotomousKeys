# This is a sample Python script.

from graphviz import Digraph
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def example():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    dot = Digraph(comment='The Round Table')
    dot.format = 'svg'
    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')
    dot.render('test-output/round-table.gv', view=True)
    print(dot.source)

def read_excel(fname):
    print(f'File name, {fname}')  # Press Ctrl+F8 to toggle the breakpoint.
    df = pd.read_excel(fname)
    return df

def temp():
    fname = './Input Files/Key to the Orders and Suborders of Nematoda/Key to the Orders and Suborders of Nemato.xlsx'
    df = read_excel(fname)  # Press Ctrl+F8 to toggle the breakpoint.
    for index, row in df.iterrows():
        print('*****************************************************************************')
        print('*****************************************************************************')
        Node = df.loc[index, 'Node']
        nemaClassSet.add(Node)
        SubKey = df.loc[index, 'SubKey']
        Description = df.loc[index, 'Description']
        Edge1 = df.loc[index, 'Edge1']
        Node2 = df.loc[index, 'Node2']
        NodeKey = (Node)
        svgEdge = (SubKey,Description,Edge1,Node2)
        svgDict[NodeKey] = svgEdge

        print(f'Node, {Node}')
        print(f'SubKey, {SubKey}')
        print(f'Description, {Description}')
        print(f'Edge1, {Edge1}')
        print(f'Edge2, {Node2}')
        print('*****************************************************************************')
        print('*****************************************************************************')
        #df.loc[idx,'Description'] = 1


def main_old():
    # Use a breakpoint in the code line below to debug your script.
    fname = './Input Files/Key to the Orders and Suborders of Nematoda/Key to the Orders and Suborders of Nemato.xlsx'
    df = read_excel(fname)  # Press Ctrl+F8 to toggle the breakpoint.
    svgDict = dict()
    nemaClassSet = set()
    # Get Class Pairs
    svgNodeDict = dict()
    for index, row in df.iterrows():
        Node = str(df.loc[index, 'Node']).strip()
        nemaClassSet.add((Node,''))
        Edge1 = str(df.loc[index, 'Edge1'])
        Node2 = str(df.loc[index, 'Node2'])
        Edge1Arr = Edge1.split()
        svgNode = ''
        if len(Edge1Arr) == 2:
            if (';' in Edge1):
                svgNode = Edge1Arr[0].strip().replace(';','')
                svgNodeDict[svgNode] = Node
                svgNode = Edge1Arr[0].strip().replace(';','')
                svgNodeDict[svgNode] = Node
            else:
                svgNode = Edge1Arr[1].strip()
                svgNodeDict[svgNode] = Node

        elif len(Edge1Arr) == 1:
            svgNode = Edge1Arr[0].strip()
            svgNodeDict[svgNode] = Node
        arrIndexNodeAr = Node2.split()
        intNode = ''
        if len(arrIndexNodeAr) == 3:
            intNode = arrIndexNodeAr[len(arrIndexNodeAr)-1]
        #print (intNode)


def get_nodes():
    # Use a breakpoint in the code line below to debug your script.
    fname = './Input Files/Key to the Orders and Suborders of Nematoda/Key to the Orders and Suborders of Nemato.xlsx'
    df = read_excel(fname)  # Press Ctrl+F8 to toggle the breakpoint.
    dot_nodes = set()
    dot_edges = set()

    # Get node names
    Node_des = ('1', 'Start')
    dot_nodes.add(Node_des)
    for index, row in df.iterrows():
        Node_Name = str(df.loc[index, 'Node_Name']).strip()
        Node2 = str(df.loc[index, 'Node2']).strip()
        Description = str(df.loc[index, 'Description']).strip()
        #Description = Description.replace(';', r'\n')
        #Description = Description.replace(',', r',\n')
        Node_Name = Node_Name
        Node_des = (Node2, Node_Name)
        dot_nodes.add(Node_des)

    for index, row in df.iterrows():
        Node = str(df.loc[index, 'Node']).strip()
        Node2 = str(df.loc[index, 'Node2']).strip()
        Description = str(df.loc[index, 'Description']).strip()
        dot_edges.add((Node, Node2,Description))
        sss = 0

    return (dot_nodes,dot_edges)



def main():
    (dot_nodes,dot_edges) = get_nodes()
    dot = Digraph(comment='Key to the Orders and Suborders of Nematoda')
    dot.format = 'svg'
    dot.attr('graph', rankdir="LR")
    #dot.attr('edge', lblstyle="middle, sloped")
    for i in sorted(dot_nodes):
        (Node, des) = i
        dot.node(Node, des)
    for i in dot_edges:
        (Node, Node2, label) = i
        label = label.replace(';', r'\n')
        label = label.replace(',', r',\n')
        dot.edge(Node, Node2, label = label, constraint='true')

    #dot.render('test-output/KeyToTheOrdersAndSubordersOfNematoda.gv', view=True,renderer='cairo')
    dot.render('test-output/KeyToTheOrdersAndSubordersOfNematoda.gv', view=True)
    print(dot.source)

    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start Processing')  # Press Ctrl+F8 to toggle the breakpoint.
    main()
    #example()
    print('End Processing')  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




