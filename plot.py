from matplotlib import pyplot as plt

from prefixTree import Trie

decisionNode = dict(boxstyle="round4", fc="1.0")#设置结点格式
leafNode = dict(boxstyle="round4", fc="1.0")#设置叶结点格式
arrow_args = dict(arrowstyle="<-")#设置箭头格式

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args, fontsize = 20)

def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=0)

def getNumLeafs(n):
    numLeafs = 0
    for c in n.children:
        current = n.children.get(c)
        if current.children != {}:
            numLeafs += getNumLeafs(current)
        else:   numLeafs += 1
    return numLeafs

def getTreeDepth(n):
    maxDepth = 0
    for c in n.children:
        current = n.children.get(c)
        if current.children != {}:
            thisDepth = 1 + getTreeDepth(current)
        # include root node
        else:   thisDepth = 2
        if thisDepth > maxDepth:    maxDepth = thisDepth
    return maxDepth

def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(nodeTxt, cntrPt, parentPt, decisionNode)
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for c in myTree.children:
        current = myTree.children.get(c)
        if current.children != {}:
            plotTree(current,cntrPt,c)
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(c, (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, c)
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0
    plotTree(inTree, (0.5,1.0), 'Root')
    # plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['font.sans-serif']=['DejaVu Sans']
    plt.rcParams['axes.unicode_minus']=False
    plt.show()

if __name__ == "__main__":
    t = Trie()
    t.insert('apple')
    t.insert('adapt')
    t.insert('add')
    t.insert('addams')
    t.insert('addict')
    t.insert('go')
    t.insert('god')
    t.insert('good')
    t.insert('great')
    t.insert('ground')
    t.insert('gradient')
    t.search('apple')
    # t.delete('apple')
    # t.delete('great')
    # t.delete('gradient')
    createPlot(t.root)
    # t.deleteTrie()