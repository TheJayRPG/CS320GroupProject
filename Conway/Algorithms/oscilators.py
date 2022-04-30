""""The next 600-700 or so lines are devoted to osicalators for conway. Essentially an osciallator is a shape of alive cells in Conway grid that after some peirod of time returns back into itself These functions are intent to be put into the class SetInitialCells in the algs.py by Kristine Hess. """
#I will put comments on only the first osicalator function
def working_bee_nine(self,currentGeneration,ROWS,COLUMNS):
    #set the x and y boundary to be 16 columns, 11 rows. X and y will be useful for tracking the location of alive cells
    x = floor((COLUMNS - 16)/2)
    y = floor((ROWS - 11)/2)
    #for a line of 3 alive cells, create a loop to initialzie a line
    for a in range(len(2)):
        currentGeneration[y+a][x+1].status = 1
        currentGeneration[y+8+a][x+1].status = 1
        currentGeneration[y+a][x+14].status = 1
        currentGeneration[y+8+a][x+14]
    for b in range(len(1)):
        currentGeneration[y+2+b][x+3].status = 1
        currentGeneration[y+8+b][x+3].status = 1
        currentGeneration[y+b][x+14].status = 1
        currentGeneration[y+7+b][x+12].status =1
    for c in range(len(4)):
        currentGeneration[y+5][x+5+c]
    #set each alive cell to an x,y position on the grid
    currentGeneration[y+3][x+2].status = 1
    currentGeneration[y+10][x].status = 1
    currentGeneration[y+7][x+2].status = 1
    currentGeneration[y+3][x+12].status = 1
    currentGeneration[y][x+15].status = 1
    currentGeneration[y+7][x+13].status = 1
    currentGeneration[y+10][x+15].status = 1
    currentGeneration[y][x].status = 1





def figure_eight(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-10)/2)
    y = floor((ROWS-10)/2)
    for a in range(len(1)):
        currentGeneration[y+a][x].status = 1
        currentGeneration[y+a][x+1].status = 1
        currentGeneration[y+4+a][x+4].status = 1
        currentGeneration[y+4+a][x+5].status = 1
    currentGeneration[y+3][x+1].status = 1
    currentGeneration[y+4][x+2].status = 1
    currentGeneration[y+1][x+3].status = 1
    currentGeneration[y+2][x+4].status = 1





def ak_47(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-10)/2)
    y = floor((ROWS-12)/2)
    for a in range((len(1))):
        currentGeneration[y+8+a][x+3].status = 1
        currentGeneration[y+10+a][x+8].status = 1
        currentGeneration[y+10+a][x+9].status = 1
    for b in range((len(2))):
        currentGeneration[y+10][x+b].status = 1
        currentGeneration[y+2+b][x+3].status = 1
        currentGeneration[y+2+b][x+7].status = 1
    currentGeneration[y+11][x].status = 1
    currentGeneration[y+8][x+2].status = 1
    currentGeneration[y+5][x+4].status = 1
    currentGeneration[y+4][x+5].status = 1
    currentGeneration[y+5][x+6].status = 1
    currentGeneration[y+0][x+4].status = 1
    currentGeneration[y+1][x+5].status = 1
    currentGeneration[y+0][x+6].status = 1





def dinner_table(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-13)/2)
    y = floor((ROWS-13)/2)
    for a in range((len(1))):
        currentGeneration[y+3][x+3+a].status = 1
        currentGeneration[y+4][x+9+a].status = 1
        currentGeneration[y+9][x+3+a].status = 1
        currentGeneration[y+8+a][x+9].status = 1
        currentGeneration[y+6][x+4+a].status = 1
    for b in range(len(2)):
        currentGeneration[y+1][x+1+b].status = 1
        currentGeneration[y+9+b][x+1].status = 1
        currentGeneration[y+11][x+9+b].status = 1
        currentGeneration[y+2+b][x+11].status = 1
    currentGeneration[y+11][x].status = 1
    currentGeneration[y+8][x+2].status = 1
    currentGeneration[y+8][x+6].status = 1
    currentGeneration[y+5][x+6].status = 1
    currentGeneration[y+7][x+6].status = 1
    currentGeneration[y][x+1].start = 1
    currentGeneration[y+2][x+4].status = 1
    currentGeneration[y+3][x+9].status = 1
    currentGeneration[y+2][x+12].status = 1
    currentGeneration[y+10][x+8].status = 1
    currentGeneration[y+12][x+11].status = 1





def david_hilbert(self,currentGeneration,ROWS,COLUMNS):
    x = floor((ROWS-33)/2)
    y = floor((COLUMNS-26)/2)
    for a in range(1):
        currentGeneration[y+16][x+a].status = 1
        currentGeneration[y+21][x+6+a].status = 1
        currentGeneration[y+12][x+10+a].status = 1
        currentGeneration[y+9][x+14+a].status = 1
        currentGeneration[y+10][x+14+a].status = 1
        currentGeneration[y+10+a][x+17].status = 1
        currentGeneration[y][x+24+a].status = 1
        currentGeneration[y+9][x+23+a].status = 1
        currentGeneration[y+10][x+24+a].status = 1
        currentGeneration[y+16][x+23+a].status = 1
        currentGeneration[y+17][x+32+a].status = 1
        currentGeneration[y+21][x+25+a].status = 1
        currentGeneration[y+25][x+24+a].status = 1
    for b in range(2):
        currentGeneration[y+17+b][x+5].status = 1
        currentGeneration[y+13][x+7+b].status = 1
        currentGeneration[y+11][x+8+b].status = 1
        currentGeneration[y+14+b][x+16].status = 1
        currentGeneration[y+14+b][x+17].status = 1
        currentGeneration[y+7+b][x+21].status = 1
        currentGeneration[y+12+b][x+22].status = 1
        currentGeneration[y+17+b][x+27].status = 1
    for c in range(3):
        currentGeneration[y+5][x+4+c].status = 1
        currentGeneration[y+14+c][x+3].status = 1
        currentGeneration[y+6][x+25+c].status = 1
        currentGeneration[y+14+c][x+14].status = 1
    for d in range(4):
        currentGeneration[y+6][x+3+d].status = 1
        currentGeneration[y+22][x+6+d].status = 1
        currentGeneration[y+23][x+22+d].status = 1
        currentGeneration[y+3][x+22+d].status = 1
    currentGeneration[y+1][x+8].status = 1
    currentGeneration[y+2][x+6].status = 1
    currentGeneration[y+4][x+10].status = 1
    currentGeneration[y+6][x+4].status = 1
    currentGeneration[y+6][x+7].status = 1
    currentGeneration[y+9][x+9].status = 1
    currentGeneration[y+11][x+7].status = 1
    currentGeneration[y+17][x].status = 1
    currentGeneration[y+17][x+2].status = 1
    currentGeneration[y+14][x+4].status = 1
    currentGeneration[y+17][x+6].status = 1
    currentGeneration[y+19][x+7].status = 1
    currentGeneration[y+23][x+6].status = 1
    currentGeneration[y+21][x+10].status = 1
    currentGeneration[y+24][x+8].status = 1
    currentGeneration[y+9][x+18].status = 1
    currentGeneration[y+11][x+18].status = 1
    currentGeneration[y+1][x+24].status = 1
    currentGeneration[y+2][x+26].status = 1
    currentGeneration[y+4][x+22].status = 1
    currentGeneration[y+6][x+25].status = 1
    currentGeneration[y+6][x+28].status = 1
    currentGeneration[y+13][x+24].status = 1
    currentGeneration[y+14][x+25].status = 1
    currentGeneration[y+14][x+28].status = 1
    currentGeneration[y+17][x+30].status = 1
    currentGeneration[y+17][x+32].status = 1
    currentGeneration[y+19][x+25].status = 1
    currentGeneration[y+17][x+26].status = 1
    currentGeneration[y+23][x+26].status = 1
    currentGeneration[y+24][x+24].status = 1
    currentGeneration[y+17][x+32].status = 1







def mold_on_fumarole(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-9)/2)
    y = floor((ROWS-14)/2)
    for a in range(1):
        currentGeneration[y+a][x+1].status = 1
        currentGeneration[y+10+a][x+1].status = 1
        currentGeneration[y+17][x+32].status = 1








def gourmet(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-20)/2)
    y = floor((ROWS-20)/2)
    for a in range(1):
        currentGeneration[y+4][x+2+a].status = 1
        currentGeneration[y+2][x+4+a].status = 1
        currentGeneration[y+2][x+7+a].status = 1
        currentGeneration[y+2][x+16+a].status = 1
        currentGeneration[y+5][x+16+a].status = 1
        currentGeneration[y+7][x+16+a].status = 1
        currentGeneration[y+15][x+16+a].status = 1
        currentGeneration[y+17][x+14+a].status = 1
        currentGeneration[y+17][x+11+a].status = 1
        currentGeneration[y+17][x+3+a].status = 1
        currentGeneration[y+14][x+2+a].status = 1
        currentGeneration[y+12][x+2+a].status = 1
    for b in range(2):
        currentGeneration[y+9][x+b].status = 1
        currentGeneration[y+b][x+10].status = 1
        currentGeneration[y+9][x+10+b].status = 1
        currentGeneration[y+10][x+17+b].status = 1
        currentGeneration[y+17+b][x+10].status = 1
    currentGeneration[y+3][x+2].status = 1
    currentGeneration[y+3][x+5].status = 1
    currentGeneration[y+3][x+7].status = 1
    currentGeneration[y+4][x+8].status = 1
    currentGeneration[y+3][x+9].status = 1
    currentGeneration[y][x+11].status = 1
    currentGeneration[y+3][x+15].status = 1
    currentGeneration[y+4][x+17].status = 1
    currentGeneration[y+8][x+15].status = 1
    currentGeneration[y+9][x+16].status = 1
    currentGeneration[y+11][x+19].status = 1
    currentGeneration[y+8][x+11].status = 1
    currentGeneration[y+11][x+10].status = 1
    currentGeneration[y+10][x+12].status = 1
    currentGeneration[y+17][x+17].status = 1
    currentGeneration[y+16][x+14].status = 1
    currentGeneration[y+16][x+12].status = 1
    currentGeneration[y+15][x+11].status = 1
    currentGeneration[y+16][x+10].status = 1
    currentGeneration[y+20][x+8].status = 1
    currentGeneration[y+17][x+4].status = 1
    currentGeneration[y+15][x+2].status = 1
    currentGeneration[y+11][x+2].status = 1
    currentGeneration[y+11][x+4].status = 1
    currentGeneration[y+10][x+3].status = 1
    currentGeneration[y+8][x].status = 1








def queen_bee_shuttle(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-22)/2)
    y = floor((ROWS-7)/2)
    for a in range(1):
        currentGeneration[y+3][x+a].status = 1
        currentGeneration[y+4][x+a].status = 1
        currentGeneration[y+a][x+9].status = 1
        currentGeneration[y+5+a][x+9].status = 1
        currentGeneration[y+3][x+20].status = 1
        currentGeneration[y+4][x+20].status = 1
    for b in range(2):
        currentGeneration[y+2+b][x+8].status = 1
    currentGeneration[y+1][x+7].status = 1
    currentGeneration[y+2][x+6].status = 1
    currentGeneration[y+3][x+5].status = 1
    currentGeneration[y+4][x+6].status = 1
    currentGeneration[y+5][x+7].status = 1
def octagon_2(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-8)/2)
    y = floor((ROWS-8)/2)
    for a in range(1):
        currentGeneration[y+4+a][x].status = 1
        currentGeneration[y+4+a][x+7].status = 1
        currentGeneration[y+1][x+3+a].status = 1
        currentGeneration[y+8][x+3+a].status = 1
    currentGeneration[y+3][x+1].status = 1
    currentGeneration[y+2][x+2].status = 1
    currentGeneration[y+2][x+5].status = 1
    currentGeneration[y+3][x+6].status = 1
    currentGeneration[y+7][x+5].status = 1
    currentGeneration[y+8][x+2].status = 1
    currentGeneration[y+7][x+1].status = 1







def toad_hassler(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-20)/2)
    y = floor((COLUMNS-26)/2)
    for a in range(1):
        currentGeneration[y+3][x+2+a].status = 1
        currentGeneration[y+7][x+2+a].status = 1
        currentGeneration[y+5][x+5+a].status = 1
        currentGeneration[y+5][x+13+a].status = 1
        currentGeneration[y+3][x+16+a].status = 1
        currentGeneration[y+7][x+16+a].status = 1
        currentGeneration[y+10][x+18+a].status = 1
        currentGeneration[y+12+a][x+12].status = 1
        currentGeneration[y+12+a][x+9].status = 1
        currentGeneration[y+18][x+16+a].status = 1
        currentGeneration[y+22][x+16+a].status = 1
        currentGeneration[y+20][x+13+a].status = 1
        currentGeneration[y+20][x+5+a].status = 1
        currentGeneration[y+22][x+2+a].status = 1
        currentGeneration[y+18][x+2+a].status = 1
    for b in range(2):
        currentGeneration[y+b][x+1].status = 1
        currentGeneration[y+8+b][x+1].status = 1
        currentGeneration[y+15+b][x+1].status = 1
        currentGeneration[y+23+b][x+1].status = 1
        currentGeneration[y+23+b][x+18].status = 1
        currentGeneration[y+15+b][x+18].status = 1
        currentGeneration[y+8+b][x+18].status = 1
        currentGeneration[y+b][x+18].status = 1
    for c in range(3):
        currentGeneration[y+20][x+8+c].status = 1
        currentGeneration[y+5][x+8+c].status = 1
    currentGeneration[y][x].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+4][x+7].status = 1
    currentGeneration[y+6][x+7].status = 1
    currentGeneration[y+4][x+12].status = 1
    currentGeneration[y+6][x+12].status = 1
    currentGeneration[y+2][x+16].status = 1
    currentGeneration[y][x+19].status = 1
    currentGeneration[y+8][x+16].status = 1
    currentGeneration[y+10][x+19].status = 1
    currentGeneration[y+15][x+19].status = 1
    currentGeneration[y+17][x+16].status = 1
    currentGeneration[y+11][x+11].status = 1
    currentGeneration[y+14][x+10].status = 1
    currentGeneration[y+23][x+16].status = 1
    currentGeneration[y+25][x+19].status = 1
    currentGeneration[y+21][x+12].status = 1
    currentGeneration[y+19][x+12].status = 1
    currentGeneration[y+21][x+7].status = 1
    currentGeneration[y+19][x+7].status = 1
    currentGeneration[y+23][x+3].status = 1
    currentGeneration[y+25][x].status = 1
    currentGeneration[y+17][x+3].status = 1
    currentGeneration[y+15][x].status = 1
    currentGeneration[y+10][x].status = 1
    currentGeneration[y+8][x+3].status = 1






def four_eaters(self,currentGeneration,ROWS,COLUMNS):
    x = floor((COLUMNS-17)/2)
    y = floor((ROWS-17)/2)
    for a in range(1):
        currentGeneration[y+3][x+4+a].status = 1
        currentGeneration[y+5][x+8+a].status = 1
        currentGeneration[y+5][x+13+a].status = 1
        currentGeneration[y+13][x+11+a].status = 1
        currentGeneration[y+8+a][x+7].status = 1
        currentGeneration[y+11][x+2+a].status = 1
    for b in range(2):
        currentGeneration[y+1][x+2+b].status = 1
        currentGeneration[y+16][x+12+b].status = 1
        currentGeneration[y+2+b][x+15].status = 1
        currentGeneration[y+12+b][x+1].status = 1
    currentGeneration[y][x+2].status = 1
    currentGeneration[y+4][x+13].status = 1
    currentGeneration[y+2][x+16].status = 1
    currentGeneration[y+6][x+7].status = 1
    currentGeneration[y+7][x+6].status = 1
    currentGeneration[y+8][x+9].status = 1
    currentGeneration[y+14][x+11].status = 1
    currentGeneration[y+16][x+14].status = 1
    currentGeneration[y+12][x+3].status = 1
    currentGeneration[y+14][x].status = 1




def rattlesnake(self,currentGeneration,ROWS,COLUMNS):
    y = floor((ROWS-13)/2)
    x = floor((COLUMNS-15)/2)
    for a in range(1):
        currentGeneration[y+9][x+a].status = 1
        currentGeneration[y+10][x+2+a].status = 1
        currentGeneration[y+12][x+7+a].status = 1
        currentGeneration[y+3][x+8+a].status = 1
        currentGeneration[y][x+8+a].status = 1
    for b in range(2):
        currentGeneration[y+8][x+7+b].status = 1
        currentGeneration[y+11][x+9+b].status = 1
        currentGeneration[y+13][x+9+b].status = 1
    for c in range(3):
        currentGeneration[y+5+c][x+7].status = 1
    currentGeneration[y+10][x].status = 1
    currentGeneration[y+9][x+3].status = 1
    currentGeneration[y+8][x+6].status = 1
    currentGeneration[y+11][x+6].status = 1
    currentGeneration[y+10][x+7].status = 1
    currentGeneration[y+10][x+9].status = 1
    currentGeneration[y+12][x+12].status = 1
    currentGeneration[y+14][x+9].status = 1
    currentGeneration[y+2][x+9].status = 1
    currentGeneration[y+1][x+8].status = 1





def honey_thieves(self,currentGeneration,ROWS,COLUMNS):
    y = floor((ROWS-15)/2)
    x = floor((COLUMNS-15)/2)
    for a in range(1):
        currentGeneration[y+9][x+2+a].status = 1
        currentGeneration[y+6][x+5+a].status = 1
        currentGeneration[y+7][x+5+a].status = 1
        currentGeneration[y+7][x+8+a].status = 1
        currentGeneration[y+8][x+8+a].status = 1
        currentGeneration[y+5][x+11+a].status = 1
    for b in range(2):
        currentGeneration[y+b][x+1].status = 1
        currentGeneration[y+10+b][x+1].status = 1
        currentGeneration[y+2+b][x+13].status = 1
        currentGeneration[y+12+b][x+13].status = 1
    currentGeneration[y+3][x+2].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+3][x+4].status = 1
    currentGeneration[y+4][x+11].status = 1
    currentGeneration[y+2][x+14].status = 1
    currentGeneration[y+14][x+14].status = 1
    currentGeneration[y+11][x+12].status = 1
    currentGeneration[y+12][x+11].status = 1
    currentGeneration[y+11][x+10].status = 1
    currentGeneration[y+10][x+3].status = 1
    currentGeneration[y+12][x].status = 1





def shuttle_fifty_four(self,currentGeneration,ROWS,COLUMNS):
    y = floor((ROWS-17)/2)
    x = floor((COLUMNS-29)/2)
    for a in range(1):
        currentGeneration[y+3][x+2+a].status = 1
        currentGeneration[y+6][x+12+a].status = 1
        currentGeneration[y+4][x+18+a].status = 1
        currentGeneration[y+5][x+19+a].status = 1
        currentGeneration[y+6][x+18+a].status = 1
        currentGeneration[y+10][x+18+a].status = 1
        currentGeneration[y+11][x+19+a].status = 1
        currentGeneration[y+12][x+18+a].status = 1
        currentGeneration[y+10][x+13+a].status = 1
        currentGeneration[y+13][x+2+a].status = 1
        currentGeneration[y+5+a][x+8].status = 1
        currentGeneration[y+3+a][x+12].status = 1
        currentGeneration[y+10+a][x+8].status = 1
        currentGeneration[y+12+a][x+12].status = 1
    for b in range(4):
        currentGeneration[y+7][x+9+b].status = 1
        currentGeneration[y+9][x+9+b].status = 1
    currentGeneration[y][x].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+9][x+3+a].status = 1
    currentGeneration[y+11][x+2].status = 1
    currentGeneration[y+3][x+18].status = 1
    currentGeneration[y+13][x+18].status = 1
    currentGeneration[y+14][x+11].status = 1
    currentGeneration[y+13][x+9].status = 1
    currentGeneration[y+14][x+3].status = 1
    currentGeneration[y+16][x].status = 1




def jason_p22(self,currentGeneration,ROWS,COLUMNS):
    y = ((ROWS-14)/2)
    x = ((COLUMNS-27)/2)
    for a in range(1):
        currentGeneration[y+3][x+2+a].status = 1
        currentGeneration[y+4][x+8+a].status = 1
        currentGeneration[y+5][x+17+a].status = 1
        currentGeneration[y+6][x+23+a].status = 1
        currentGeneration[y+5+a][x+10].status = 1
        currentGeneration[y+3+a][x+16].status = 1
    for b in range(2):
        currentGeneration[y+7][x+7+b].status = 1
        currentGeneration[y+2][x+17+a].status = 1
        currentGeneration[y+b][x+3].status = 1
        currentGeneration[y+7+b][x+25].status = 1
    currentGeneration[y][x].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+5][x+5].status = 1
    currentGeneration[y+4][x+6].status = 1
    currentGeneration[y+6][x+6].status = 1
    currentGeneration[y+3][x+7].status = 1
    currentGeneration[y+6][x+19].status = 1
    currentGeneration[y+5][x+20].status = 1
    currentGeneration[y+4][x+21].status = 1
    currentGeneration[y+3][x+20].status = 1
    currentGeneration[y+7][x+23].status = 1
    currentGeneration[y+9][x+26].status = 1




def mold(self,currentGeneration,ROWS,COLUMNS):
    x = ((ROWS-8)/2)
    y = ((COLUMNS-8)/2)
    for a in range(1):
        currentGeneration[y+4][x+2+a].status = 1
        currentGeneration[y][x+3+a].status = 1
        currentGeneration[y+1+a][x+5].status = 1
    currentGeneration[y+4][x].status = 1
    currentGeneration[y+5][x+1].status = 1
    currentGeneration[y+2][x].status = 1
    currentGeneration[y+1][x+2].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+3][x+4].status = 1





def pre_pulsar_shuttle_29(self,currentGeneration,ROWS,COLUMNS):
    y = ((ROWS-6)/2)
    x = ((COLUMNS-6)/2)
    for a in range(1):
        currentGeneration[y+3][x+12+a].status = 1
        currentGeneration[y+7][x+15+a].status = 1
        currentGeneration[y+8][x+15+a].status = 1
        currentGeneration[y+11][x+19+a].status = 1
        currentGeneration[y+12][x+19+a].status = 1
        currentGeneration[y+15][x+24+a].status = 1
    for b in range(2):
        currentGeneration[y+6][x+6+b].status = 1
        currentGeneration[y+8][x+6+b].status = 1
        currentGeneration[y+12][x+6+b].status = 1
        currentGeneration[y+14][x+6+b].status = 1
        currentGeneration[y+19][x+13+b].status = 1
        currentGeneration[y+21][x+13+b].status = 1
        currentGeneration[y+19][x+19+b].status = 1
        currentGeneration[y+1][x+13+b].status = 1
        currentGeneration[y+12+b][x+26].status = 1
    currentGeneration[y+6][x].status = 1
    currentGeneration[y+6][x+2].status = 1
    currentGeneration[y+5][x+1].status = 1
    currentGeneration[y+7][x+1].status = 1
    currentGeneration[y+13][x+1].status = 1
    currentGeneration[y+14][x].status = 1
    currentGeneration[y+14][x+2].status = 1
    currentGeneration[y+15][x+1].status = 1
    currentGeneration[y+7][x+6].status = 1
    currentGeneration[y+7][x+8].status = 1
    currentGeneration[y+13][x+6].status = 1
    currentGeneration[y+13][x+8].status = 1
    currentGeneration[y+2][x+12].status = 1
    currentGeneration[y][x+15].status = 1
    currentGeneration[y+25][x+13].status = 1
    currentGeneration[y+26][x+12].status = 1
    currentGeneration[y+26][x+14].status = 1
    currentGeneration[y+27][x+13].status = 1
    currentGeneration[y+25][x+21].status = 1
    currentGeneration[y+26][x+20].status = 1
    currentGeneration[y+26][x+22].status = 1
    currentGeneration[y+27][x+21].status = 1
    currentGeneration[y+20][x+15].status = 1
    currentGeneration[y+20][x+13].status = 1
    currentGeneration[y+20][x+21].status = 1
    currentGeneration[y+20][x+23].status = 1
    currentGeneration[y+14][x+24].status = 1
    currentGeneration[y+12][x+27].status = 1





def twin_bees_shuttle(self,currentGeneration,ROWS,COLUMNS):
    y = ((ROWS-13)/2)
    x = ((COLUMNS-32)/2)
    for a in range(1):
        currentGeneration[y+1][x+a].status = 1
        currentGeneration[y+2][x+a].status = 1
        currentGeneration[y+8][x+a].status = 1
        currentGeneration[y+9][x+a].status = 1
        currentGeneration[y][x+17+a].status = 1
        currentGeneration[y+10][x+17+a].status = 1
        currentGeneration[y+1][x+27+a].status = 1
        currentGeneration[y+2][x+27+a].status = 1
        currentGeneration[y+1+a][x+19].status = 1
        currentGeneration[y+8+a][x+19].status = 1
    for b in range(2):
        currentGeneration[y+3][x+17+b].status = 1
        currentGeneration[y+7][x+17+b].status = 1
    currentGeneration[y+1][x+17].status = 1
    currentGeneration[y+9][x+17].status = 1





def two_blockers_hassling_r_pento(self,currentGeneration,ROWS,COLUMNS):
    x = ((COLUMNS-30)/2)
    y = ((ROWS-19)/2)
    for a in range(1):
        currentGeneration[y][x+4+a].status = 1
        currentGeneration[y+2][x+4+a].status = 1
        currentGeneration[y+1][x+8+a].status = 1
        currentGeneration[y+2][x+8+a].status = 1
        currentGeneration[y+7][x+7+a].status = 1
        currentGeneration[y+8][x+7+a].status = 1
        currentGeneration[y+13][x+18+a].status = 1
        currentGeneration[y+7][x+21+a].status = 1
        currentGeneration[y+8][x+21+a].status = 1
        currentGeneration[y+3][x+24+a].status = 1
        currentGeneration[y+1][x+24+a].status = 1
        currentGeneration[y+1][x+28+a].status = 1
        currentGeneration[y+2][x+28+a].status = 1
        currentGeneration[y+11+a][x+17].status = 1
    for b in range(2):
        currentGeneration[y+2][x+b].status = 1
        currentGeneration[y+10][x+18+a].status = 1
        currentGeneration[y+1][x+20+a].status = 1
    for c in range(3):
        currentGeneration[y+1][x+c].status = 1
        currentGeneration[y+2][x+20+c].status = 1
    currentGeneration[y+3][x+5].status = 1
    currentGeneration[y+12][x+20].status = 1
    currentGeneration[y][x+25].status = 1




def mezernich_p31(self,currentGeneration,ROWS,COLUMNS):
    x = ((ROWS-8)/2)
    y = ((COLUMNS-8)/2)
    for a in range(1):
        currentGeneration[y+1][x+a].status = 1
        currentGeneration[y+2][x+a].status = 1
        currentGeneration[y][x+7+a].status = 1
        currentGeneration[y][x+15+a].status = 1
        currentGeneration[y+1][x+22+a].status = 1
        currentGeneration[y+2][x+22+a].status = 1
        currentGeneration[y+10][x+22+a].status = 1
        currentGeneration[y+11][x+23+a].status = 1
        currentGeneration[y+12][x+15+a].status = 1
        currentGeneration[y+12][x+16+a].status = 1
        currentGeneration[y+11][x+a].status = 1
        currentGeneration[y+10][x+a].status = 1
        currentGeneration[y+1+a][x+9].status = 1
        currentGeneration[y+1+a][x+14].status = 1
        currentGeneration[y+10+a][x+9].status = 1
        currentGeneration[y+10+a][x+14].status = 1
    currentGeneration[y+1][x+6].status = 1
    currentGeneration[y+2][x+7].status = 1
    currentGeneration[y+3][x+8].status = 1
    currentGeneration[y][x+10].status = 1
    currentGeneration[y][x+13].status = 1
    currentGeneration[y+3][x+15].status = 1
    currentGeneration[y+2][x+16].status = 1
    currentGeneration[y+1][x+17].status = 1
    currentGeneration[y+9][x+15].status = 1
    currentGeneration[y+10][x+16].status = 1
    currentGeneration[y+11][x+17].status = 1
    currentGeneration[y+12][x+13].status = 1
    currentGeneration[y+12][x+10].status = 1
    currentGeneration[y+11][x+6].status = 1
    currentGeneration[y+10][x+7].status = 1
    currentGeneration[y+11][x+8].status = 1





def centinel(self,currentGeneration,ROWS,COLUMNS):
    x = ((ROWS-17)/2)
    y = ((COLUMNS-52)/2)
    for a in range(1):
        currentGeneration[y+3][x+2+a].status = 1
        currentGeneration[y+4][x+11+a].status = 1
        currentGeneration[y+5][x+10+a].status = 1
        currentGeneration[y+6][x+11+a].status = 1
        currentGeneration[y+6][x+15+a].status = 1
        currentGeneration[y+2][x+25+a].status = 1
        currentGeneration[y+3][x+25+a].status = 1
        currentGeneration[y+13][x+25+a].status = 1
        currentGeneration[y+14][x+25+a].status = 1
        currentGeneration[y+10][x+15+a].status = 1
        currentGeneration[y+12][x+11+a].status = 1
        currentGeneration[y+11][x+10+a].status = 1
        currentGeneration[y+10][x+11+a].status = 1
        currentGeneration[y+13][x+2+a].status = 1
    for b in range(2):
        currentGeneration[y+b][x+1].status = 1
        currentGeneration[y+14+b][x+1].status = 1
    currentGeneration[y+16][x].status = 1
    currentGeneration[y+14][x+3].status = 1
    currentGeneration[y][x].status = 1
    currentGeneration[y+2][x+3].status = 1
    currentGeneration[y+3][x+12].status = 1
    currentGeneration[y+13][x+12].status = 1






def pentadecathlon(self,currentGeneration,ROWS,COLUMNS):
    x = ((ROWS-8)/2)
    y = ((COLUMNS-8)/2)
    for a in range(1):
        currentGeneration[y+1][x+a].status = 1
        currentGeneration[y+1][x+8+a].status = 1
    for b in range(3):
        currentGeneration[y+1][x+3+b].status = 1
    currentGeneration[y][x+2].status = 1
    currentGeneration[y][x+7].status = 1
    currentGeneration[y+2][x+7].status = 1
    currentGeneration[y+2][x+2].status = 1





def mango_with_beacon_on_clock(self,currentGeneration,ROWS,COLUMNS):
    y = ((ROWS-16)/2)
    x = ((COLUMNS-9)/2)
    for a in range(1):
        currentGeneration[y][x+1+a].status = 1
        currentGeneration[y+3][x+3+a].status = 1
        currentGeneration[y+6+a][x].status = 1
        currentGeneration[y+7+a][x+4].status = 1
        currentGeneration[y+8+a][x+7].status = 1
        currentGeneration[y+6+a][x+5+a].status = 1
        currentGeneration[y+9+a][x+5+a].status = 1
    for b in range(3):
        currentGeneration[y+5][x+1+b].status = 1
    currentGeneration[y+1][x+1].status = 1
    currentGeneration[y+2][x+4].status = 1
    currentGeneration[y+7][x+1].status = 1





def candlefrobra(self,currentGeneration,ROWS,COLUMNS):
    x = ((COLUMNS-10)/2)
    y = ((ROWS-5)/2)
    for a in range(1):
        currentGeneration[y][x+2+a].status = 1
        currentGeneration[y+1][x+2+a].status = 1
        currentGeneration[y+5+a][x+3].status = 1
        currentGeneration[y+8-a][x+1+a].status = 1
        currentGeneration[y+9-a][x+3+a].status = 1
    currentGeneration[y+4][x].status = 1
    currentGeneration[y+4][x+4].status = 1


        

    



    
    

