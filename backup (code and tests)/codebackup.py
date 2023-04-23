from datetime import datetime
from flask import Flask, Response, url_for, request, jsonify, render_template

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


@app.route("/time")
def time():
    date = datetime.now()
    dateStr = str(date)
    return Response(dateStr, mimetype="application/json")


# ------------ TIER 2 ------------

dataVault = {
    "operating-systems": {
        "Debian": [
            {"name": "Debian", "version": "11.0.0", "id": 1},
            {"name": "Debian", "version": "10.0.0", "id": 1},
            {"name": "Debian", "version": "9.0.0", "id": 1},
        ],
        "Oracle Linux": [
            {"name": "Oracle Linux", "version": "9.0.0", "id": 2},
            {"name": "Oracle Linux", "version": "8.7.0", "id": 2},
            {"name": "Oracle Linux", "version": "8.6.0", "id": 2},
        ],
        "Microsoft Windows": [
            {"name": "Microsoft Windows", "version": "11.0.0", "id": 3},
            {"name": "Microsoft Windows", "version": "10.0.0", "id": 3},
            {"name": "Microsoft Windows", "version": "8.0.0", "id": 3},
            {"name": "Microsoft Windows", "version": "7.0.0", "id": 3},
        ],
        "MacOS": [
            {"name": "MacOS", "version": "13.0.0", "id": 4},
            {"name": "MacOS", "version": "12.0.0", "id": 4},
            {"name": "MacOS", "version": "11.0.0", "id": 4},
            {"name": "MacOS", "version": "10.15.1", "id": 4},
        ],
    }
}


@app.get("/dc")
def list_os():
    return {"operating_systems": list(dataVault.values())}


if __name__ == "__main__":
    app.run(port=8000, debug=True)
