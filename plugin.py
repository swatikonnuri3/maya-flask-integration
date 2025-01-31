import maya.cmds as cmds
import requests
import json

SERVER_URL = "http://127.0.0.1:5000"

def get_selected_object():
    selected = cmds.ls(selection=True)
    return selected[0] if selected else None

def get_transform_data(obj):
    position = cmds.xform(obj, query=True, translation=True, worldSpace=True)
    rotation = cmds.xform(obj, query=True, rotation=True, worldSpace=True)
    scale = cmds.xform(obj, query=True, scale=True, worldSpace=True)

    return {"position": position, "rotation": rotation, "scale": scale}

def send_transform(endpoint):
    obj = get_selected_object()
    if not obj:
        cmds.warning("No object selected!")
        return
    
    data = get_transform_data(obj)
    response = requests.post(f"{SERVER_URL}/{endpoint}", json=data)
    print(f"Server Response: {response.json()}")

cmds.window(title="Maya Plugin", widthHeight=(200, 150))
cmds.columnLayout(adjustableColumn=True)
cmds.button(label="Send Transform", command=lambda _: send_transform("transform"))
cmds.button(label="Send Translation", command=lambda _: send_transform("translation"))
cmds.button(label="Send Rotation", command=lambda _: send_transform("rotation"))
cmds.button(label="Send Scale", command=lambda _: send_transform("scale"))
cmds.showWindow()
