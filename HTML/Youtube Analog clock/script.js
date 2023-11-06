const body = document.querySelector('body')
const hourHand = document.querySelector('.hour')
const minuteHand = document.querySelector('.minute')
const secondHand = document.querySelector('.second')
const modeSwitch = document.querySelector('.mode-switch')

modeSwitch.addEventListener('click', () => {
    body.classList.toggle('dark')

    const isDarkmode = body.classList.contains('dark')

    if (isDarkmode) {
        modeSwitch.textContent = 'Dark mode'
    } else {
        modeSwitch.textContent = 'Light mode'
    }
})

modeSwitch.addEventListener('mouseover', () => {
    const isDarkmode = body.classList.contains('dark')

    if (isDarkmode) {
        modeSwitch.textContent = 'Light mode'
    } else {
        modeSwitch.textContent = 'Dark mode'
    }
})

modeSwitch.addEventListener('mouseout', () => {
    const isDarkmode = body.classList.contains('dark')

    if (isDarkmode) {
        modeSwitch.textContent = 'Dark mode'
    } else {
        modeSwitch.textContent = 'Light mode'
    }
})

const updateTime = () => {
    let date = new Date()
    let secToDeg = date.getSeconds() * 6
    let minToDeg = date.getMinutes() * 6
    let hrToGet = date.getHours() * 30

    secondHand.style.transform = `rotate(${secToDeg}deg)`
    minuteHand.style.transform = `rotate(${minToDeg}deg)`
    hourHand.style.transform = `rotate(${hrToGet}deg)`
}

setInterval(updateTime, 1000)