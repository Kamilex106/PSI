from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from countryapi.container import Container
from countryapi.api.routers.country import router as country_router
from countryapi.api.routers.continent import router as continent_router


container = Container()
container.wire(modules=[
    "countryapi.api.routers.continent",
    "countryapi.api.routers.country",
])

app = FastAPI()
app.include_router(country_router, prefix="/country")
app.include_router(continent_router, prefix="/continent")



@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:

    return await http_exception_handler(request, exception)
