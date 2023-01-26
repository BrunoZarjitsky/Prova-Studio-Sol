#pip install requests
#pip install fastapi
#pip install uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import uvicorn

app = FastAPI()

class RequestModel(BaseModel):
    password: Union[str, None] = None
    rules: Union[list, None] = None

@app.post("/verify")
def password_check(request: RequestModel = None):
    password_verification = PasswordVerification(
        password = request.password,
        rules = request.rules
    )
    payload = {
        "verify": password_verification.pass_verify,
        "noMatch": password_verification.no_match
    }
    return payload

class PasswordVerification:
    def __init__(self, password: str, rules: list):
        self.password = password
        self.rules = rules
        self.no_match = []
        self.pass_verify = False
        self.verify_rules()

    # This method will be used to check if a character is a special character
    @staticmethod
    def is_spec(char):
        spec = "!@#$%^&*()-+\\/{}[]"
        if char in spec:
            return True
        return False

    # This method calls each verification method in the list of rules
    # With the eval function i was able to abstract the call of the verification methods
    def verify_rules(self):
        for rule in self.rules:
            rule_name = rule.get("rule")
            rule_value = rule.get("value")
            eval(f"self.verify_{rule_name}({rule_value})")
        self.pass_verify = not bool(self.no_match)

    # This method check if the password have the minimun required size
    def verify_minSize(self, value:int = 0)-> None:
        if len(self.password) < value:
            self.no_match.append("minSize")

    # This method check if the password have the minimun required uppercase letters
    def verify_minUppercase(self, value:int = 0):
        if sum(map(str.isupper, self.password)) < value:
            self.no_match.append("minUppercase")

    # This method check if the password have the minimun required lowwercase letters
    def verify_minLowercase(self, value:int = 0):
        if sum(map(str.islower, self.password)) < value:
            self.no_match.append("minLowercase")

    # This method check if the password have the minimun required numbers
    def verify_minDigit(self, value:int = 0):
        if sum(map(str.isdigit, self.password)) < value:
            self.no_match.append("minDigit")

    # This method check if the password have the minimun required special characters
    def verify_minSpecialChars(self, value:int = 0):
        if sum(map(self.is_spec, self.password)) < value:
            self.no_match.append("minSpecialChars")

    # This method check if the password have repeated characters
    def verify_noRepeted(self, value:int = 0)-> None:
        last_char = None
        for char in self.password:
            if char == last_char:
                self.no_match.append("noRepeted")
                return None
            last_char = char

# Runs the API server at localhost:8080
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)