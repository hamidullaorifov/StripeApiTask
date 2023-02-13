FROM python:3.11.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV STRIPE_PUBLISHABLE_KEY pk_test_51MaZiWD1R2u7ntZkYubGwryUdhQhqmvD12Swrew9n1HiGuVSFsBuak4mIZ4MPDPkBszwhlqjfAw34nOC1NEK53x500ZKPGa51q
ENV STRIPE_SECRET_KEY sk_test_51MaZiWD1R2u7ntZkAHD2pBs6TxlkAfTi9arUDjObC9ddkC4jjKEwXum2XBbN3Ca8gVeAN82Fo7nXcIMXwSmqrQuX000rGMD2Sx 
ENV SECRET_KEY=django-insecure-kpb=!*@g7%l5hjvch!1h)48hx!^_jnae4*kwcmi&f%(a!5+2!7
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/