FROM python:3.11-slim
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    APP_PORT=7446
WORKDIR $HOME/app
COPY --chown=user . $HOME/app
RUN pip install --no-cache-dir fastapi uvicorn[standard]
EXPOSE 7446
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7446"]
