'''
DFS 
Καραμποϊκης Νικολαος Π17040
'''


maze = [   #dhmiourgia labirinthoy me thn xrhsh listas.to 1 anaparista monopati, to 0 toixo
        [0,0,0,0,0],
        [0,1,0,1,0],
        [0,1,1,1,1],
        [0,1,1,0,1],
        [1,1,0,0,0],
        ]
R = 5
C = 5
paidia=[] #dhmiourgia listas paidia

def findNext(i,j):#methodos pou elegxei an to geitoniko keli
    if i < C and i>=0 and j>=0 and j<R:  # (efooson einai mesa sta oria)exei thn timh 1 dhladh mporei na proxwrhsei
        if maze[i][j] == 1:
            paidia.append([i,j])



ma = [[4,0]]          #arxikopoihsh lista metwpou anazhthshs.h thesi 4,0 einai h afethria toy labirinthou
ks = []               #arxikopoihsh listas kleistoy synolou
while(len(ma)>0):     #an to length ths listas tou metwpou anazhthshs einai megalyterh apo to 0 emfanizoyme ta akoloutha mhnymata
    print('-'*100)
    print('Μέτωπο Αναζήτησης:', ma )
    print('Κλειστό σύνολο: ', ks)
    node = ma.pop(0)  #pairnome kathe fora to prwto stoixeio apo thn lista ma kai to bazoume sto node este na to eksetasoume(mikroskopio)
    print('Μελετάμε το: ',node)
    if node in ks:    #an to node yparxei hdh sto kleisto sunolo dhladh to exoume eksetasei pame pali sthn arxh tou while
        print('Καταστάσεις παιδιά: ----------')
        continue
    if node == [2,4]: #an to node einai to einai to [2,4] stoixeio ths listas diladi o termatismos tote emfanizetai analogo mhnyma
        print('Βρέθηκε Λύση!')
        break
    findNext(node[0]+1,node[1])#me thn methodo findNext elegxoume panw katw aristera kai deksia apo to node kai emfanizoume ta antistoixa paidia
    findNext(node[0]-1,node[1])
    findNext(node[0],node[1]-1)
    findNext(node[0],node[1]+1)
    print("Καταστάσεις παιδιά: ",paidia)
    while len(paidia) > 0: #an yparxoun paidia ta bazoume stis prwtes theseis tou metwpou anazhthshs
        ma.insert(0,paidia.pop(0))#topethetoume ta stoixeia ths listas paidia stis prwtes theseis ths listas ma
    ks.append(node)   #prosthetoume to node pou eksetasame shn lista ks