from fastapi import FastAPI
import blog.models as models
from blog.database import engine
from blog.routers import blog, user, authentification


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentification.router)
app.include_router(blog.router)
app.include_router(user.router)


