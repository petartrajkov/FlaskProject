import json
from flask import Flask
from flask import jsonify
from flask import request
import pytest

from main import app


def test_os_versions():
    payload = [
        {"name": "Debian", "version": "11", "id": 1},
        {"name": "Debian", "version": "10", "id": 2},
        {"name": "Debian", "version": "9", "id": 3},
        {"name": "Oracle Linux", "version": "9.2.3", "id": 4},
        {"name": "Oracle Linux", "version": "10.2.3", "id": 5},
        {"name": "Oracle Linux", "version": "11.2.3", "id": 6},
        {"name": "Microsoft Windows", "version": "11.0.0", "id": 7},
        {"name": "Microsoft Windows", "version": "10.0.0", "id": 8},
        {"name": "Microsoft Windows", "version": "8.0.0", "id": 9},
        {"name": "Microsoft Windows", "version": "7.0.0", "id": 10},
        {"name": "MacOS", "version": "13.0.0", "id": 11},
        {"name": "MacOS", "version": "12.0.0", "id": 12},
        {"name": "MacOS", "version": "11.0.0", "id": 13},
        {"name": "MacOS", "version": "10.15.1", "id": 14},
    ]

    with app.test_client() as client:
        response = client.post("/os_versions", json=payload)

        assert response.status_code == 200
        assert json.loads(response.data) == {
            "Debian": {"highest": "11", "lowest": "9"},
            "Oracle Linux": {"highest": "11.2.3", "lowest": "9.2.3"},
            "Microsoft Windows": {"highest": "11.0.0", "lowest": "7.0.0"},
            "MacOS": {"highest": "13.0.0", "lowest": "10.15.1"},
        }
