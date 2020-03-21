from flask import Flask
import requests


def foo2():
    file = open('hw.csv', 'r')
    line = file.read()
    file.close()
    line = line.strip()
    line = line.split('\n')
    headers = line[0].split(',')
    data = line[1:]

    Height_Sum = 0
    Weight_Sum = 0

    for i in range(len(data)):
        data[i] = data[i].strip()
        data[i] = data[i].split(',')
        Height_Sum += float(data[i][1])
        Weight_Sum += float(data[i][2])
    Height_av = Height_Sum / len(data)
    Weight_av = Weight_Sum / len(data)

    Height_av *= 2.54
    Weight_av *= 0.453592
    return Height_av, Weight_av


def foo():
    for i in range(100):
        url = 'http://api.open-notify.org/astros.json'
        r = requests.get(url, auth=('user', 'pass'))
        return r.json()


app = Flask(__name__)  # __main__


@app.route('/')
def astronaut():
    data = foo()
    out_put = 'В данный момент на орбите  ' + str(data['number']) + ' астронавтов!'
    return out_put


@app.route('/hw/')
def hw():
    data = foo()
    out_put = 'В данный момент на орбите  ' + str(data['number']) + ' астронавтов!'
    return out_put
