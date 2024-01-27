def Result():
    for i in range(2):
        vis=[]
    for j in range(3):
        if pos[i][j]=="Empty":
            vis.append("口")
        elif pos[i][j]=="Wardrobe":
            vis.append("目")
        elif pos[i][j]=="Table":
            vis.append("田")
        elif pos[i][j]=="Chair1":
            vis.append("国")
        elif pos[i][j]=="Chair2":
            vis.append("四")
        elif pos[i][j]=="Armchair":
            vis.append("画")
            print(vis)
    print('------------------')
