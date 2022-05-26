const fetch = require('node-fetch')

const seen = [];

const btn = document.querySelector('#next');
btn.addEventListener('click', (e) => {
    e.preventDefault();
    console.log(seen);
    const response = fetch('https://random-data-api.com/api/color/random_color')
    console.log(response)
});