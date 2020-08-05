FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV DD_LOGS_INJECTION=true
#ENV DD_AGENT_HOST=?
EXPOSE 8888

ENTRYPOINT ["python"]
CMD ["app.py"]