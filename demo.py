import os
from quart import Quart, render_template, send_file, abort

app = Quart(__name__, template_folder="src/templates")

@app.route("/")
async def home():
    return await render_template("index.html")

# static path
@app.route("/src/<path:name>", methods=["GET"]) # this is vunerable to attacks using ..
async def get_static(name:str):
    if os.path.exists(f"src/static/{name}"):
        return await send_file(f"src/static/{name}")
    abort(404)

# style path
@app.route("/style.css", methods=["GET"])
async def get_style():
    return await send_file("src/static/style.css")

if __name__ == "__main__":
    app.run("127.0.0.1", 8000) # Hypercorn would be used in production
    # Using port 8000 instead of 80 since my laptop has an Apache server running for some reason