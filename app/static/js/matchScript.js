const seen = [];
let unseen_match;

const btn = document.querySelector('#next');
const like = document.querySelector('#like');

document.addEventListener('DOMContentLoaded', () => {
    findNewMatch();
})

// LOGIC TO MAKE NEXT BUTTON DYNAMIC
// FETCH REQUEST TO BACKEND, STORING DATA RETURNED AND DISPLAYING IT USING JS

async function findNewMatch(){
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
    unseen_match = response.match
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
}

btn.addEventListener('click', async(e) => {
    e.preventDefault();
    findNewMatch();
});

// LOGIC TO MAKE LIKE BUTTON DYNAMIC
// FETCH REQUEST TO BACKEND, CREATE NEW LIKE BASED ON CURRENT USER AND LIKED USER
// NOTIFY MATCH HAS BEEN MADE, IF BOTH USERS MATCHED THEN NOTIFY AS WELL
// AFTER USER LIKES, FIND A NEW MATCH

like.addEventListener('click', async(e) => {
    e.preventDefault();
    const response = await (
        await fetch(`/matched/${unseen_match.id}`, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            }
        })
    ).json()
    const modal = document.querySelector('.match-popup');
    modal.innerHTML = `
        <img src={{ ${currentuser.image} if ${currentuser.image} else "../static/images/default-profile.webp"}} alt="default"><img src={{ ${unseen_match.image} if ${unseen_match.image} else "../static/images/default-profile.webp"}} alt="default">
        <h2>${response.Message}</h2>
    `;
    const modal_wrap = document.querySelector('.modal-wrapper');
    if(response.Mutual) modal_wrap.classList.add('show')

    findNewMatch();

})