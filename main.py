from datetime import datetime
from flask import Flask, Response, url_for, request, jsonify, render_template
import requests
import json

app = Flask("__name__")

# ------------ TIER 1 ------------

# should be endpoint, not html, and should be accessed via Postman


@app.route("/stringcounter-response", methods=["POST"])
def post_input():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json = request.get_json()
        stringVar = json["array"]

        def countOccurrence(a):
            k = {}
            for j in a:
                if j in k:
                    k[j] += 1
                else:
                    k[j] = 1
            return k

        return str(countOccurrence(stringVar))
    else:
        return "Content-Type not supported!"


@app.route("/time", methods=["GET"])
def time():
    date = datetime.now()
    dateStr = str(date)
    return Response(dateStr, mimetype="application/json")


# ------------ TIER 2 ------------


@app.route("/os_versions", methods=["POST"])
def os_versions():
    data = request.json
    results = {}
    for os in data:
        name = os["name"]
        version_str = os["version"]
        version_num = tuple(map(int, version_str.split(".")))
        if name in results:
            results[name]["highest"] = max(results[name]["highest"], version_num)
            results[name]["lowest"] = min(results[name]["lowest"], version_num)
        else:
            results[name] = {"highest": version_num, "lowest": version_num}
    for os in results:
        results[os]["highest"] = ".".join(map(str, results[os]["highest"]))
        results[os]["lowest"] = ".".join(map(str, results[os]["lowest"]))
    return jsonify(results)


# ------------ TIER 3 ------------
# check test_tier2.py and README.txt

# ------------ TIER 4 ------------
# check dbs.py and README.txt

if __name__ == "__main__":
    app.run(debug=True)
