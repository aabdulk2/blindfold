const seen = [];

const btn = document.querySelector('#next');
btn.addEventListener('click', async(e) => {
    e.preventDefault();
    console.log(seen);
    const response = await (await fetch('/hello')).json()
    console.log(await response)
});