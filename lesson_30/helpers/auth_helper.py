class AuthHelper:

    @staticmethod
    def with_basic_auth(url: str, user: str, pwd: str) -> str:
        if url.startswith("https://"):
            return url.replace("https://", f"https://{user}:{pwd}@")
        if url.startswith("http://"):
            return url.replace("http://", f"http://{user}:{pwd}@")
        return f"https://{user}:{pwd}@{url}"