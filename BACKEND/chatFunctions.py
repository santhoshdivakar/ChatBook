"""
  script: BACKEND.getRoomList
  script: BACKEND.getUsersInRoom
  script: BACKEND.getRoomChat
  script: BACKEND.sendChat
  script: BACKEND.changeRoom
  script: BACKEND.registerUser
  script: BACKEND.registerRoom
"""
import sqlFunction

def getRoomList(): # No parameters whatsoever
    roomList = []
    # Log into the SQL DB and fetch the List
    conn = sqlFunction.connect()
    cursor = conn.cursor()
    stmt = "SELECT roomId, roomName, categoryName, userCount from rooms"
    cursor.execute(stmt)
    retVal = cursor.fetchall()
    if len(retVal) > 0:
	for item in retVal:
	    itemDict = {}
	    roomIndex,roomName,category,count = item
	    itemDict[roomIndex] = (roomName,category,count)
	    roomList.append(itemDict)
        pass # Looping the room segment
    pass # If the db fetches the values
    return {'status':'OK', 'roomList':roomList}


def getUsersInRoom(roomIndex=-1): # RoomIndex is number
    userList = []
    if roomIndex == -1:
        return {'status':'NOK', 'message':'RoomIndex is not valid'}
    # Log into the SQL DB and fetch the List
    conn = sqlFunction.connect()
    cursor = conn.cursor()
    # First check if the room is valid
    stmt = "SELECT roomId, roomName from rooms where roomId=%s"
    cursor.execute(stmt,(roomIndex,))
    retVal = cursor.fetchall()
    if len(retVal) == 0:
        return {'status':'NOK', 'message':'RoomIndex is not valid'}
    # Now extract the users who are in the room
    stmt = "SELECT userId,userName where roomIndex=%s"
    cursor.execute(stmt,(roomIndex,))
    retVal = cursor.fetchall()
    if len(retVal) > 0:
	for item in retVal:
	    userTuple = [item[0],item[1]]
	    userList.append(userTuple)
	pass # Looping around list of users
    pass # If the fetch returns more than one user
    return {'status':'OK', 'userList':userList}
    
def getRoomChat(roomName=''): # RoomName is string
    roomChatList = []
    # The roomChat would contain a time/user/chat-string tuple/dictionary. So a list of them.
    # From the room get the number of users in the list
    return {'status':'OK', 'roomChat':roomChatList}
    
def sendChat(roomName='', chatString=''): # RoomName is string
    # Open the SQL instance, fill it into the db and use the time-stamp as well.
    return {'status':'OK'}
    
def changeRoom(roomName=''): # RoomName is string
    # Check if the target room is full, if not then change the room for the user
    return {'status':'OK'}
    
def registerUser(userName=''): # userName is string
    # Note the IP Address and also the userName and return OK. the frontend should set cookie to disable abuse
    return {'status':'OK'}
    
def registerRoom(roomName=''): # userName is string
    # It would simply insert into the rooms table and also add user to that room
    return {'status':'OK'}
