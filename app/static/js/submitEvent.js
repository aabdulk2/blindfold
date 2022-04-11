const textarea = document.querySelector(".message-box")
textarea.addEventListener("keyup",(e)=>{
    if (e.key === "Enter")
    {
        e.preventDefault()
        textarea.closest("form").submit()
    }
})