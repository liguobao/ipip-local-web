FROM python:3.7.1-slim


# set working directory
RUN mkdir -p /app
WORKDIR /app

# add requirements
COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# # add entrypoint.sh
# COPY ./entrypoint.sh /app/entrypoint.sh

# add app
COPY . /app

# run server
# CMD ["./entrypoint.sh"]
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", ":8000","-t","80", "-w", "4", "--access-logfile", "-","manage:app"]