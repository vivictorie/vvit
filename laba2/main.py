# from fastapi import FastAPI
#
# app = FastAPI()
# @app.get('/')
# def hello():
#     return {"Hello": "World"}
# @app.get("/{name}")
# def hello_friend(name: str):
#     return {"Hello": name}
# # @app.get("/greeting/{name}")
# # def special_hello_friend(greeting: str, name: str):
#  #   return {greeting: name}
#
# from pydantic import BaseModel
#
#
# class Greeting(BaseModel):
#     action: str
#     name: str
#
#
# @app.post("/")
# def greeting(greeting: Greeting):
#     return {greeting.action: greeting.name}
#
# @app.get("/greeting/{name}", response_model=Greeting)
# def special_hello_friend(greeting: str, name: str):
#     """Особое приветствие"""
#     return Greeting(action=greeting, name=name)
#
#

