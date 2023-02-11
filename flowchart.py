import re

from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

UNITARY_NODE = """<html>
<head>
  <title>Flow Chart</title>
  <style>
    .flowchart {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 300px;
      width: 500px;
      margin: auto;
    }
    .big_node {
      width: 500px;
      height: 300px;
      margin: auto;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 24px;
      font-weight: bold;
      background-color: #ADD8E6;
    }
    p {
        text-align: center;
        font-size: 20px;
      }
    h1 {
        text-align: center;
      }
  </style>
</head>
<body>
  <div class="header">
    <h1>HEADER_INPUT</h1>
  </div>
  <div class="question">
    <p>QUESTION_INPUT</p>
  </div>
  <div class="flowchart">
    <div class="big_node"><a href="NODE_HREF"><p>NODE_TEXT</p></a></div>
  </div>
</body>
</html>"""

BINARY_NODE = """<html>
<head>
  <title>Flow Chart</title>
  <style>
    .flowchart {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 300px;
      width: 500px;
      margin: auto;
    }

    .node_blue {
      margin: auto;
      border-radius: 50%;
      height: 100px;
      width: 100px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 24px;
      font-weight: bold;
      background-color: #ADD8E6;
    }
    .node_red {
      width: 500px;
      height: 300px;
      margin: auto;
      background-color: #fff;
      border-radius: 50%;
      height: 100px;
      width: 100px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 24px;
      font-weight: bold;
      background-color: #FFB6C1;
    }
    p {
        text-align: center;
        font-size: 20px;
      }
    h1 {
        text-align: center;
      }
  </style>
</head>
<body>
  <div class="header">
    <h1>HEADER_INPUT</h1>
  </div>
  <div class="question">
    <p>QUESTION_INPUT</p>
  </div>
  <div class="flowchart">
    <div class="node_blue"><a href="YES_HREF"><p>Yes</p></a></div>
    <div class="node_red"><a href="NO_HREF"><p>No</p></a></div>
  </div>
</body>
</html>"""


def replace_phrases(string, replacements):
    for phrase, replacement in replacements.items():
        string = re.sub(phrase, replacement, string)
    return string


@app.get("/")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "Want to use chatGPT to learn to code anything and automatize your coding experience?",
        "QUESTION_INPUT": "",
        "NODE_HREF": "/start",
        'NODE_TEXT': 'Follow these steps!'
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/start")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Imagine the final realization. Does it have only a front or a back end?",
        "YES_HREF": "/Y1",
        "NO_HREF": "/N1",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/N1")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "In your planning, separate the front end from back end. <br>"
                          "Do not forget to include connecting elements between these parts in your plans.",
        "NODE_TEXT": "Proceed for each part separately.",
        "NODE_HREF": "/start"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/Y1")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Does it use 2 languages or less?",
        "YES_HREF": "/Y2",
        "NO_HREF": "/N2",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/N2")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Subdivide by language.",
        "NODE_TEXT": "Proceed for each part separately.",
        "NODE_HREF": "/start"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/Y2")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Do you expect less than ~100 lines of code?",
        "YES_HREF": "/Y3",
        "NO_HREF": "/N3",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/N3")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Subdivide by function. If present, reduce repetitive aspects to single instances.",
        "NODE_TEXT": "Proceed for each part separately.",
        "NODE_HREF": "/start"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/Y3")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Ask chatGPT. Does it work?",
        '<div class="node_red">': '<div class="node_red"><a href="/refresh"><p>chatGPT busy</p></a></div><div class="node_red">',
        "YES_HREF": "/Y4",
        "NO_HREF": "/N4",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/Y4")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Yay! Connect the new piece manually to the existing code. Does it work?",
        "YES_HREF": "/Y5",
        "NO_HREF": "/end",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/N4")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Ask chatGPT to fix it. Does it work now?",
        "YES_HREF": "/Y4",
        "NO_HREF": "/end",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/Y5")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Good job!",
        "NODE_TEXT": "Proceed with the next part.",
        "NODE_HREF": "/start"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/refresh")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Try Ctrl+Shoft+R. Now?",
        "YES_HREF": "/Y3",
        "NO_HREF": "/end",
    }
    return HTMLResponse(replace_phrases(BINARY_NODE, replacements))


@app.get("/coffee")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Try Ctrl+Shoft+R. Now?",
        "NODE_TEXT": "Yes",
        "NODE_HREF": "/N3"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))


@app.get("/end")
async def flowchart():
    replacements = {
        "HEADER_INPUT": "",
        "QUESTION_INPUT": "Try GPT4 when it comes out.",
        "NODE_TEXT": "Go to StackOverflow.",
        "NODE_HREF": "https://stackoverflow.com/"
    }
    return HTMLResponse(replace_phrases(UNITARY_NODE, replacements))
