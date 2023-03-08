#Hockey Algorithm iteration 1
#Author: Anthony Cuomo
#predict best players based off of coaches bias
#predict which players have highest growth rate
### what factors lead to this
#make list of players in order by ranking
### rank players based off data points
### Data Points 
### size, stick handling, skating, shot, speed, 
# hockey sense, creativity, passing, pedigree -> Total as multiplyer, last spot == total
#make bias per cateagory
## any player abpve 30 ready for peewees
## 5 thru > 15 == Mites
## 15 thru 30  == Squirts
## 31 thru 55 == Peewees 
## 55 + Bantams 

# add test case to check if addition is right then check after each buff to make sure its all right

# original Scores from beginning of season
playerStats = {
    #jake Pat
    "player1":[3,5,5,4,5,5,1,0],
    #Jake E
    "player2":[5,4,4,4,5,4,1,0],
    #Max
    "player3":[4,5,5,5,5,5,1,0],
    #Eli
    "player4":[2,3,5,3,3,5,1,0],
    #Mase
    "player5":[2,4,4,4,3,4,1,0]
}

#scores at end of season
playerStats2 ={
    "PlayerOne": "player1",
    "playerOneAtts": [3,5,5,4,5,5,1,2,4,0],
    "PlayerTwo": "player2",
    "playerTwoAtts": [5,4,4,4,4,4,1,3,4,0],
    "PlayerThree": "player3",
    "playerThreeAtts": [4,5,5,5,5,5,1,5,5,0],
    "PlayerFour": "player4",
    "playerFourAtts": [2,3,4,3,5,3,1,2,3,0],
    "PlayerFive": "player5",
    "playerFiveAtts": [2,4,4,4,4,4,1,4,4,0],
}

playerRanking = []

dictItems = playerStats.items()
dictItems2 = playerStats2.items()
keys = playerStats2.keys()

#----------test statements------------
# print(playerStats2["PlayerOne"])
# print(playerStats2["playerOneAtts"][6])
# print(playerStats2["playerOneAtts"])


# print(playerStats2["PlayerTwo"])
# print(playerStats2["playerTwoAtts"][5])
# print(playerStats2["playerTwoAtts"])
# print(keys)

# buffs considered as a percentage of a full category 
    # for example 30% of 5 for speed buff 

def playerSizeBuff(playerSize):
     #add multiplyers here before geting total
    #print(playerSize)
    if playerSize >= 4:
        holder = playerSize*.015
        playerSize = holder + playerSize

        #print(playerSize)
    return playerSize

def playerSpeedBuff(playerSpeed):
    #add multiplier for speed
    if playerSpeed >= 5:
        holder = playerSpeed*.030
        playerSpeed = holder + playerSpeed
    return playerSpeed


def playerPedigreeBuff(playerPedigree, playerTotal):
    #percentage on player pedigree Buff
    #need tier system example: nhl player dad compared to high school hockey dad
    #this percentage added to bare player total which means total without buffs
    #print(playerTotal)
    if playerPedigree == 0:
        playerTotal = playerTotal
       # print(playerTotal)
    else:    
        holder =  playerTotal * .005
        
    return holder

def playerSkatingBuff(skatingBuff):
    if skatingBuff >= 5:
        holder = skatingBuff*.050
        skatingBuff = holder + skatingBuff
    return skatingBuff

def playerGrowthRate(growthRate):

    # actual growth rate 
    # score at the beginning of the year versus score at end of the year 
    # plus minus higher the plus higher the growth rate 

    #somehow predict players growth rate based out of 5 

    return growthRate

def predictGrowthRate():

    # predicted Growth rate 
    #will be based on original score then a predicted end of the year score 
    #will be determined the difference could be predicted growthrate
    # just spitballin here but maybe a high skating score or high hockey sense score 
    # but low in other category kids have a highe probabilty of thier hands getting 
    # better thus allowing for higher growth then a bad skater  

    return 0

def playerTotalPedigree():
    # sending in all data and calculating total to calculate pedigree
    return 0

def playerTotalFinal():

    #get player total after all buffs calculated

    return 0

def playerOneData():
    print("------------------------")
    print("This is player One")
    
    player1Size = playerStats2["playerOneAtts"][0]
    player1Hands = playerStats2["playerOneAtts"][1]
    player1Skating = playerStats2["playerOneAtts"][2]
    player1Shot = playerStats2["playerOneAtts"][3]
    player1Speed = playerStats2["playerOneAtts"][4]
    player1HockeyIQ = playerStats2["playerOneAtts"][5]
    player1Pedi = playerStats2["playerOneAtts"][6]
    player1Create = playerStats2["playerOneAtts"][7]
    player1Pass = playerStats2["playerOneAtts"][8]
    player1Total = playerStats2["playerOneAtts"][9]
    

    #test line 
    #print(playerStats2["playerOneAtts"][6])

    player1Total = player1Size + player1Hands + player1Skating + player1Shot + player1Speed + player1HockeyIQ + player1Create + player1Pass

    #adding buffs to points
    calcPedigree = playerPedigreeBuff(player1Pedi, player1Total)
    player1Speed = playerSpeedBuff(player1Speed)
    player1Size = playerSizeBuff(player1Size)
    
    
    #print(player1Size)

    player1Total = player1Size + player1Hands + player1Skating + player1Shot + player1Speed + player1HockeyIQ + player1Create + player1Pass + calcPedigree
    #update player total
    #print(player1Total)
    playerStats2["playerOneAtts"][9] += player1Total

    playerRanking.append(playerStats2["playerOneAtts"][9])

    #player total displayed
    print(playerStats2["playerOneAtts"][9])
    #print(player1Total)

def playerTwoData():
    print("------------------------")
    print("This is player Two")
    player2Size = playerStats2["playerTwoAtts"][0]
    player2Hands = playerStats2["playerTwoAtts"][1]
    player2Skating = playerStats2["playerTwoAtts"][2]
    player2Shot = playerStats2["playerTwoAtts"][3]
    player2Speed = playerStats2["playerTwoAtts"][4]
    player2HockeyIQ = playerStats2["playerTwoAtts"][5]
    player2Pedi = playerStats2["playerTwoAtts"][6]
    player2Create = playerStats2["playerTwoAtts"][7]
    player2Pass = playerStats2["playerTwoAtts"][8]
    player2Total = playerStats2["playerTwoAtts"][9]

    #print(playerStats2["playerOneAtts"][6])

    player2Total = player2Size + player2Hands + player2Skating + player2Shot + player2Speed + player2HockeyIQ + player2Create + player2Pass
    player2Total = playerPedigreeBuff(player2Pedi, player2Total)

    #all buff points 
    calcPedigree = playerPedigreeBuff(player2Pedi, player2Total)
    player2Speed = playerSpeedBuff(player2Speed)
    player2Size = playerSizeBuff(player2Size)

    player2Total = player2Size + player2Hands + player2Skating + player2Shot + player2Speed + player2HockeyIQ + player2Create + player2Pass + calcPedigree
    playerStats2["playerTwoAtts"][9] += player2Total

    playerRanking.append(playerStats2["playerTwoAtts"][9])

    #player total displayd
    print(playerStats2["playerTwoAtts"][9])
    #print(player1Total)


def playerThreeData():
    print("------------------------")
    print("This is player Three")
    
    player3Size = playerStats2["playerThreeAtts"][0]
    player3Hands = playerStats2["playerThreeAtts"][1]
    player3Skating = playerStats2["playerThreeAtts"][2]
    player3Shot = playerStats2["playerThreeAtts"][3]
    player3Speed = playerStats2["playerThreeAtts"][4]
    player3HockeyIQ = playerStats2["playerThreeAtts"][5]
    player3Pedi = playerStats2["playerThreeAtts"][6]
    player3Create = playerStats2["playerThreeAtts"][7]
    player3Pass = playerStats2["playerThreeAtts"][8]
    player3Total = playerStats2["playerThreeAtts"][9]
    

    #print(playerStats2["playerOneAtts"][6])

    player3Total = player3Size + player3Hands + player3Skating + player3Shot + player3Speed + player3HockeyIQ+ player3Create + player3Pass
    player3Total = playerPedigreeBuff(player3Pedi, player3Total)

    #all buff points
    calcPedigree = playerPedigreeBuff(player3Pedi, player3Total)
    player3Speed = playerSpeedBuff(player3Speed)
    player3Size = playerSizeBuff(player3Size)

    player3Total = player3Size + player3Hands + player3Skating + player3Shot + player3Speed + player3HockeyIQ + player3Create + player3Pass + calcPedigree
    playerStats2["playerThreeAtts"][9] += player3Total

    playerRanking.append(playerStats2["playerThreeAtts"][9])

    #player total displayed
    print(playerStats2["playerThreeAtts"][9])
    #print(player1Total)

def playerFourData():
    print("------------------------")
    print("This is player Four")
    
    player4Size = playerStats2["playerFourAtts"][0]
    player4Hands = playerStats2["playerFourAtts"][1]
    player4Skating = playerStats2["playerFourAtts"][2]
    player4Shot = playerStats2["playerFourAtts"][3]
    player4Speed = playerStats2["playerFourAtts"][4]
    player4HockeyIQ = playerStats2["playerFourAtts"][5]
    player4Pedi = playerStats2["playerFourAtts"][6]
    player4Create = playerStats2["playerFourAtts"][7]
    player4Pass = playerStats2["playerFourAtts"][8]
    player4Total = playerStats2["playerFourAtts"][9]

    #print(playerStats2["playerOneAtts"][6])

    player4Total = player4Size + player4Hands + player4Skating + player4Shot + player4Speed + player4HockeyIQ + player4Create + player4Pass
    player4Total = playerPedigreeBuff(player4Pedi, player4Total)

    #all buff Points
    calcPedigree = playerPedigreeBuff(player4Pedi, player4Total)
    player4Speed = playerSpeedBuff(player4Speed)
    player4Size = playerSizeBuff(player4Size)

    player4Total = player4Size + player4Hands + player4Skating + player4Shot + player4Speed + player4HockeyIQ + player4Create + player4Pass + calcPedigree
    playerStats2["playerFourAtts"][9] += player4Total

    playerRanking.append(playerStats2["playerFourAtts"][9])
    
    #player total displayed
    print(playerStats2["playerFourAtts"][9])
    #print(player1Total)

def playerFiveData():
    print("------------------------")
    print("This is player Five")
    
    player5Size = playerStats2["playerFiveAtts"][0]
    player5Hands = playerStats2["playerFiveAtts"][1]
    player5Skating = playerStats2["playerFiveAtts"][2]
    player5Shot = playerStats2["playerFiveAtts"][3]
    player5Speed = playerStats2["playerFiveAtts"][4]
    player5HockeyIQ = playerStats2["playerFiveAtts"][5]
    player5Pedi = playerStats2["playerFiveAtts"][6]
    player5Create = playerStats2["playerFourAtts"][7]
    player5Pass = playerStats2["playerFourAtts"][8]
    player5Total = playerStats2["playerFiveAtts"][9]

    player5Total = player5Size + player5Hands + player5Skating + player5Shot + player5Speed + player5HockeyIQ + player5Create + player5Pass
    player5Total = playerPedigreeBuff(player5Pedi, player5Total)

    #all buff points 
    calcPedigree = playerPedigreeBuff(player5Pedi, player5Total)
    player5Speed = playerSpeedBuff(player5Speed)
    player5Size = playerSizeBuff(player5Size)

    player5Total = player5Size + player5Hands + player5Skating + player5Shot + player5Speed + player5HockeyIQ + player5Create + player5Pass + calcPedigree
    playerStats2["playerFiveAtts"][9] += player5Total
    
    playerRanking.append(playerStats2["playerFiveAtts"][9])
    
    #player total displayed
    print(playerStats2["playerFiveAtts"][9])
    #print(player1Total)

print("---------Method Calls-----------")
playerOneData()
playerTwoData()
playerThreeData()
playerFourData()
playerFiveData()

playerRanking.sort(reverse=True)

print(playerRanking)






