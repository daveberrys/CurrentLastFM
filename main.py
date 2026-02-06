from flask import Flask, jsonify, request
from api.lastfm import get_lastfm_data

app = Flask(__name__)
@app.route("/api/now_playing", methods=["GET"])
def now_playing():
    username = request.args.get("user")
    api_key = request.args.get("api_key")

    if not username:
        return jsonify({"error": "Query parameter 'user' is required."}), 400

    if not api_key:
        return jsonify({"error": "Query parameter 'api_key' is required."}), 400

    track_data = get_lastfm_data(username=username, api_key=api_key)

    if "error" in track_data:
        return jsonify(track_data), 502

    return jsonify(track_data)


if __name__ == "__main__":
    print("Starting Last.fm proxy server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
