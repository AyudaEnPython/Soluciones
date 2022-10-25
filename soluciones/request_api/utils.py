"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
from typing import Callable, Dict, Tuple, Optional

import requests

HEADERS: Dict[str, str] = {'content-type': 'application/json; charset=UTF-8'}
methods: Dict[str, Callable] = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE": requests.delete
}


def _read_file(filename: str) -> Dict[str, str]:
    with open(filename) as f:
        return json.load(f)


CONFIG: Dict[str, str] = _read_file("config.json")


def get_response(
    method: str,
    resource: str,
    resource_id: Optional[str] = None,
) -> Tuple[requests.Response, str]:
    if method in ("PUT", "DELETE") and resource_id is None:
        raise ValueError("Se requiere un identificador para PUT y DELETE")
    if resource_id is not None:
        url = CONFIG["url"] + resource + "/" + resource_id
    else:
        url = CONFIG["url"] + resource
    try:
        if resource == "posts":
            data = "posts.json"
        if resource == "comments":
            data = "comments.json"
        if method in ("POST", "PUT", "DELETE"):
            payload = _read_file(data)
            response = methods[method](url, json=payload, headers=HEADERS)
        else:
            response = methods[method](
                url, timeout=CONFIG["request_time_out"]
            )
    except KeyError:
        raise ValueError(f"El método {method} es inválido")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error de conexión: {e}")
    return response, method


def save_results(response: requests.Response, method: str) -> None:
    type_, charset = response.headers["content-type"].split(";")
    _, encoding = charset.split("=")
    with open(CONFIG["response_status"], "w", encoding=encoding) as f:
        json.dump(
            {
                "method": method,
                "url": response.url,
                "status": response.status_code,
                "type": type_,
                "encoding": encoding,
            },
            f,
            indent=4,
        )
    if method == "POST" or method == "GET":
        with open(CONFIG["response_data"], "w", encoding=encoding) as f:
            json.dump(response.json(), f, indent=4)


def show(response: requests.Response, method: str) -> None:
    print(response.text)


if __name__ == "__main__":
    response, method = get_response("GET", "posts", "1")
    save_results(response, method)
    # show(response, method)
