from fastapi import FastAPI, HTTPException


class Day:
    def __init__(self, id, town, date, morning, daytime, night, humidity):
        self.id = id
        self.town = town
        self.date = date
        self.morning = morning
        self.daytime = daytime
        self.night = night
        self.humidity = humidity


days_list = [Day(0, "Moscow", "01.01.2023", "-2", "1", "0", "80%"),
             Day(1, "Moscow", "29.12.2022", "-6", "-4", "-3", "65%"),
             Day(2, "Taganrog", "01.01.2023", "-8", "-10", "-7", "50%")]

app = FastAPI()


@app.get("/v1/weather/{town}")
async def weather(town):
    result = []
    for day in days_list:
        if day.town == town:
            result.append(day)
    return result


@app.get("/v1/weather/{town}/{date}")
async def weather(town, date):
    for day in days_list:
        if day.town == town and day.date == date:
            return day
    raise HTTPException(status_code=404, detail="Error")
