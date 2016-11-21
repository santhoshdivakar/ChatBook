"""
  script: BACKEND.getRoomList
  script: BACKEND.getUsersInRoom
  script: BACKEND.getRoomChat
  script: BACKEND.sendChat
  script: BACKEND.changeRoom
  script: BACKEND.registerUser
  script: BACKEND.registerRoom
"""

def getRoomList(): # No parameters whatsoever
    roomList = []
    # Log into the SQL DB and fetch the List
    return {'status':'OK', 'roomList':roomList}


def getUsersInRoom(roomName=''): # RoomName is string
    userList = []
    # From the room get the number of users in the list
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
