FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV DD_LOGS_INJECTION=true
ENV DD_PROPAGATION_STYLE_INJECT=Datadog,B3
ENV DD_ENV='yssy-demo'
ENV DD_SERVICE='api-estoque'
#ENV DD_AGENT_HOST=?
EXPOSE 8888

ENTRYPOINT ["python"]
CMD ["app.py"]