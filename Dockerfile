FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT streamlit run app.py --server.address=0.0.0.0 --server.port=8080