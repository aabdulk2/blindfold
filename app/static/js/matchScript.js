const seen = [];

const btn = document.querySelector('#next');
btn.addEventListener('click', async(e) => {
    e.preventDefault();
    console.log(seen);
    const response = await (
        await fetch('/hello', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(seen)
        })
    ).json()
    console.log(response)
    const unseen_match = response.match
    seen.push(unseen_match.id)

    const username_field = document.querySelector('.match-username');
    const name_field = document.querySelector('.match-name');
    const age_field = document.querySelector('.match-age');
    const gender_field = document.querySelector('.match-gender');
    const preference_field = document.querySelector('.match-preference');
    const bio_field = document.querySelector('.match-bio');
    const email_field = document.querySelector('.match-email');
    
    username_field.innerHTML = unseen_match.username
    age_field.innerHTML = unseen_match.age
    name_field.innerHTML = `${unseen_match.firstName} ${unseen_match.lastName}`
    bio_field.innerHTML = unseen_match.bio
    email_field.innerHTML = unseen_match.email
    gender_field.innerHTML = `Gender: ${unseen_match.gender}`
    preference_field.innerHTML = `Preference: ${unseen_match.preference}`
});