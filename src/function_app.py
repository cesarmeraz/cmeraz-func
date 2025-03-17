import azure.functions as func
import logging

app = func.FunctionApp()


@app.route(route="func-dir", auth_level=func.AuthLevel.ANONYMOUS, methods=[func.HttpMethod.GET])
def GetFunctionDir(req: func.HttpRequest,  context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(f"Function name: {context.function_directory}")


@app.route(route="health-check", auth_level=func.AuthLevel.ANONYMOUS, methods=[func.HttpMethod.GET])
def HealthCheck(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )