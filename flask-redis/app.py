from flask import Flask, render_template
import redis
import os
import socket

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/count")
def count():
    visits = r.incr("visits")
    return render_template(
        "index.html",
        visits=visits,
        hostname=socket.gethostname()
    )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)