let data = null;

const url =
  "http://api.weatherapi.com/v1/forecast.json?key=c703fdc01de641bf81b151223232602&q=Izmir&days=7&aqi=no&alerts=no";

function getWeather() {}

function init() {
  data = document.getElementById("data");

  fetch(url)
    .then((resp) => {
      return resp.json();
    })
    .then((json) => {
      json.forecast.forecastday.forEach(({ day }) => {
        data.innerHTML += day.maxtemp_c + "<br/>";
      });
    });

  console.log("data", data);
}

window.onload = init;
