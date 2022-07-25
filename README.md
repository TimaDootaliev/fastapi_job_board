# To run project:


1. git clone git@github.com:TimaDootaliev/jobs_fastapi_t.git

2. cd jobs_fastapi_t

3. python3 -m venv <virtual_environment_name>

4. . venv/bin/activate - linux

5. `.env.template >> .env` and fill the file with your credentials

6. `pip install -r backends/requirements-dev.txt`

7. cd backends/


8. uvicorn main:app <some_options(--reload)>


# To run pre-commit hooks:

1. pre-commit run --all-files

### If you don't want to run pre-commit hooks every time you commit, you can make commits with `--no-verify` option:

`git commit --no-verify`
