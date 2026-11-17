# Day 11 · Ship it in a box
#
# TODO 11.1 · Write a Dockerfile for the API in app/:
#   - start FROM python:3.12-slim
#   - set the WORKDIR to /app
#   - COPY app/requirements.txt first and pip install it (--no-cache-dir), so code changes don't reinstall everything
#   - then COPY the rest of app/ into /app
#   - EXPOSE 8000 and start it with: uvicorn main:app --host 0.0.0.0 --port 8000
#
# Check it with: python quest.py 11


FROM python:3.12-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
