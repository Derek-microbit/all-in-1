input.onButtonPressed(Button.A, function () {
    basic.showNumber(step)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.compassHeading())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature() * (9 / 5) + 32)
})
input.onGesture(Gesture.Shake, function () {
    step += 1
})
input.onGesture(Gesture.ThreeG, function () {
    basic.showNumber(input.lightLevel())
})
let step = 0
step = 0
