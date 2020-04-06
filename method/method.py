from fastapi import FastAPI, Request 

app=FastAPI

@app.api_route(path="/method", methods=["GET","POST","PUT","DELETE","OPTIONS"])
def request_method(request:Request):
	return {"method":request.method}

