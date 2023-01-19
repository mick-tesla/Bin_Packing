from functions import *
if __name__=='__main__':
    data=[100,22,25,51,95,58,97,30,79,23,53,80,20,65,64,21,26,100,81,98,70,85,92,97,86,71,91,29,63,34,67,23,33,89,94,47,100,37,40,58,73,39,49,79,54,57,98,69,67,49,38,34,96,27,92,82,69,45,69,20,75,97,51,70,29,91,98,77,48,45,43,61,36,82,89,94,26,35,58,58,57,46,44,91,49,52,65,42,33,60,37,57,91,52,95,84,72,75,89,81,67,74,87,60,32,76,85,59,62,39,64,52,88,45,29,88,85,54,40,57]
    print('BIN PACKING AVEC RECHERCHE TABOU')
    bags,mat_x,mat_y=bin_packing(data,tabu_search,150)
    print('Résultats :')
    with open('results.txt','a') as out:out.write(str(bags))
    print(bags)
    print('Nombre de sacs : '+str(len(bags)))
    print('Poids moyen de chaque sac : '+str(round(sum([sum(i) for i in bags])/len(bags),2)))
    print('Pourcentage moyen de remplissage : {}%'.format(round(sum([sum(i) for i in bags])*100/len(bags)/150,2)))    