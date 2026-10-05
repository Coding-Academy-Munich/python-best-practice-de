# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SRP Workshop</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>

# %% [markdown]
#
# ## Wiederholung: Single Responsibility Principle (SRP, SOLID)
#
# - Ein Modul sollte nur einen einzigen Grund haben, sich zu ändern
# - Alternativ: Ein Modul sollte nur gegenüber einem einzigen Akteur
#   verantwortlich sein.

# %% [markdown]
#
# ## Auflösungs-Strategien
#
# <div>
# <img src="img/book_resolution_1_srp.svg"
#      style="float:left;padding:5px;width:40%"/>
# <img src="img/book_resolution_2_srp.svg"
#      style="float:right;padding:5px;width:50%"/>
# </div>

# %% [markdown]
#
# <img src="img/book_resolution_1.svg"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
#
# <img src="img/book_resolution_2.svg"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
#
# ## Workshop: Wetterstation
#
# Sie arbeiten an einer Wetterstation-Anwendung. Die Klasse `WeatherStation`
# hat sich im Laufe der Zeit zu einem Monolithen entwickelt:
#
# - **Datenbeschaffung:** Abrufen von Wetterdaten aus verschiedenen Quellen
#   mit Caching
# - **Warnungsüberwachung:** Prüfen von Schwellenwerten und Protokollieren
#   von Wetterwarnungen
# - **Datenanzeige:** Darstellung der Daten in verschiedenen
#   Einheitensystemen (metrisch/imperial)
# - **Beobachtungshistorie:** Speichern vergangener Beobachtungen für
#   Statistiken und Trendanalysen
#
# Ihre Aufgabe: Refaktorisieren Sie die Klasse `WeatherStation`, so dass
# jede Klasse im System dem Single Responsibility Principle entspricht.

# %% [markdown]
#
# ### Klassendiagramm der Wetterstation
#
# <img src="img/weather_app_class.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown]
#
# ### `run_weather_app()` Sequenzdiagramm
#
# <img src="img/weather_app_sequence.svg"
#      style="display:block;margin:auto;width:30%"/>

# %%
from datetime import datetime


# %%
class WeatherStation:
    def __init__(self):
        self.sources = {
            "downtown": "https://weather.example.com/downtown",
            "airport": "https://weather.example.com/airport",
        }
        self.cache = {}
        self.cache_ttl = 300
        self.alert_thresholds = {"temperature": 35.0, "wind_speed": 80.0}
        self.alert_log = []
        self.unit_system = "metric"
        self.history = []

    def fetch_data(self, source_name):
        if source_name not in self.sources:
            raise ValueError(f"Unknown source: '{source_name}'")
        now = datetime.now()
        if source_name in self.cache:
            cached_time, cached_data = self.cache[source_name]
            if (now - cached_time).total_seconds() < self.cache_ttl:
                print(f"Cache hit for '{source_name}'")
                return cached_data
        # Simulate API call
        data = {"temperature": 28.5, "humidity": 65.0, "wind_speed": 12.0}
        self.cache[source_name] = (now, data)
        print(f"Fetched data from '{source_name}'")
        return data

    def check_alerts(self, reading):
        for metric, threshold in self.alert_thresholds.items():
            if metric in reading and reading[metric] > threshold:
                alert = f"{metric}={reading[metric]} exceeds {threshold}"
                self.alert_log.append(alert)
                print(f"ALERT: {alert}")

    def display_current(self, reading):
        if self.unit_system == "imperial":
            temp = reading["temperature"] * 9 / 5 + 32
            wind = reading["wind_speed"] * 0.621371
            print(f"{temp:.1f}°F | {reading['humidity']:.0f}% | {wind:.1f} mph")
        else:
            t = reading["temperature"]
            w = reading["wind_speed"]
            print(f"{t:.1f}°C | {reading['humidity']:.0f}% | {w:.1f} km/h")

    def display_forecast(self, readings):
        for i, r in enumerate(readings, 1):
            temp = r["temperature"]
            if self.unit_system == "imperial":
                temp = temp * 9 / 5 + 32
                print(f"  Day {i}: {temp:.1f}°F")
            else:
                print(f"  Day {i}: {temp:.1f}°C")

    def add_to_history(self, reading):
        self.history.append({"reading": reading, "time": datetime.now()})

    def get_average(self, metric):
        values = [e["reading"][metric] for e in self.history
                  if metric in e["reading"]]
        if not values:
            return None
        return sum(values) / len(values)

    def get_trend(self, metric):
        values = [e["reading"][metric] for e in self.history
                  if metric in e["reading"]]
        if len(values) < 2:
            return "insufficient data"
        if values[-1] > values[0]:
            return "rising"
        if values[-1] < values[0]:
            return "falling"
        return "stable"


# %%
def run_weather_app():
    station = WeatherStation()
    reading = station.fetch_data("downtown")
    station.fetch_data("downtown")
    station.check_alerts(reading)
    station.display_current(reading)
    station.unit_system = "imperial"
    station.display_current(reading)
    station.add_to_history(reading)
    hot = {"temperature": 40.0, "humidity": 80.0, "wind_speed": 90.0}
    station.add_to_history(hot)
    station.check_alerts(hot)
    print(f"Avg temp: {station.get_average('temperature'):.1f}")
    print(f"Trend: {station.get_trend('temperature')}")
    print(f"Alerts: {len(station.alert_log)}")


# %%
run_weather_app()
