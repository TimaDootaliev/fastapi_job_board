from db.repository.jobs import list_jobs, retrieve_job
from db.session import get_db
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from webapps.jobs import route_jobs

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        'general_pages/homepage.html', {'request': request, 'jobs': jobs, 'msg': msg}
    )


@router.get('/details/{id}')
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    return templates.TemplateResponse('jobs/detail.html', {'request': request, 'job': job})
    