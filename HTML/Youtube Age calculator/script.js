let para = document.querySelector('.count')

const updateAge = () => {
    let age = new Date()

    para.innerText = `You're age: ${age.getSeconds()}d`
}

setInterval(updateAge, 100)