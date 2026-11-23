"""HTTP client for the Items API."""

from typing import Any, Self

import httpx


class ItemClient:
    """Client for interacting with the Items REST API."""

    def __init__(self, base_url: str = "http://127.0.0.1:8000", timeout: float = 5.0) -> None:
        self.client = httpx.Client(base_url=base_url, timeout=timeout)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        self.client.close()

    def create_item(self, name: str, price: float) -> dict[str, Any]:
        try:
            resp = self.client.post("/items", json={"name": name, "price": price})
            resp.raise_for_status()
            return resp.json() # type: ignore
        except httpx.HTTPStatusError as e:
            print(f"Client error (create): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (create): {e}")
            raise

    def get_item(self, item_id: int) -> dict[str, Any]:
        try:
            resp = self.client.get(f"/items/{item_id}")
            resp.raise_for_status()
            return resp.json() # type: ignore
        except httpx.HTTPStatusError as e:
            print(f"Client error (get): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (get): {e}")
            raise

    def list_items(self, limit: int = 10, offset: int = 0) -> list[dict[str, Any]]:
        try:
            resp = self.client.get("/items", params={"limit": limit, "offset": offset})
            resp.raise_for_status()
            return resp.json() # type: ignore
        except httpx.HTTPStatusError as e:
            print(f"Client error (list): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (list): {e}")
            raise

    def search_items(self, q: str) -> list[dict[str, Any]]:
        try:
            resp = self.client.get("/items/search", params={"q": q})
            resp.raise_for_status()
            return resp.json() # type: ignore
        except httpx.HTTPStatusError as e:
            print(f"Client error (search): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (search): {e}")
            raise

    def update_item(self, item_id: int, name: str, price: float) -> dict[str, Any]:
        try:
            resp = self.client.put(f"/items/{item_id}", json={"name": name, "price": price})
            resp.raise_for_status()
            return resp.json() # type: ignore
        except httpx.HTTPStatusError as e:
            print(f"Client error (update): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (update): {e}")
            raise

    def delete_item(self, item_id: int) -> None:
        try:
            resp = self.client.delete(f"/items/{item_id}")
            resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"Client error (delete): {e.response.status_code}")
            raise
        except httpx.RequestError as e:
            print(f"Network error (delete): {e}")
            raise