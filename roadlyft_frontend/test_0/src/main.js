import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import './assets/main.css'

function getJsonFromServer(url, data) {
  return fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return response.json();
  })
  .catch(error => {
      console.error('There was a problem with your fetch operation:', error);
  });
}

// Example usage:
const flaskUrl = 'http://127.0.0.1:5000/get';
const postData = { key: 'value' };

// getJsonFromServer(flaskUrl, postData)
//   .then(jsonData => {
//       console.log('Received JSON data from server:', jsonData);
//       // Do something with jsonData
//   });

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/";
    console.log(`Cookie "${name}" set successfully.`);
}

// To get all cookies
const cookies = document.cookie;

function getCookie(name) {
    const cookieString = document.cookie;
    const cookiesArray = cookieString.split('; ');
    for (let cookie of cookiesArray) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return cookieValue;
        }
    }
    return null; // If cookie not found
}

if (getCookie("lo_@_ty") == null) {
    setCookie("lo_@_ty", "spawned uWSGI");
} else {
    console.log("announcing my loyalty to the Emperor...");
}

const app = createApp(App);
app.use(store);
app.use(router);
app.mount('#app');

// app.config.globalProperties.$getJsonFromServer = getJsonFromServer;
// app.config.globalProperties.$setCookie = setCookie;
// app.config.globalProperties.$getCookie = getCookie;
