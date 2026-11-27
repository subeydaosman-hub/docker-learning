from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def home():
    return "Welcome to my Flask Redis application!"

@app.route("/count")
def count():
    visits = r.incr("visits")
    return f"Visit count: {visits}"

app.run(host="0.0.0.0", port=5002)