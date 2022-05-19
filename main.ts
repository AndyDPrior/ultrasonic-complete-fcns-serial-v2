function Spin(direction: string) {
    if (direction.substr(0, 1) == "L") {
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.Left, speed)
    } else {
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.Right, speed)
    }
    
    basic.pause(pause2)
    Kitronik_Move_Motor.stop()
}

//  Used to back out of the situation
serial.onDataReceived(serial.delimiters(Delimiters.Hash), function on_data_received() {
    
    Exit = 1
    action = serial.readUntil(serial.delimiters(Delimiters.Hash))
    if (action == "F") {
        Move()
    } else if (action == "L") {
        Spin("R")
    } else {
        moveMotorZIP = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
        moveMotorZIP.showRainbow(1, 360)
    }
    
    basic.pause(pause2)
})
function Move() {
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, speed)
    basic.pause(pause2)
    Kitronik_Move_Motor.stop()
}

let distance = 0
let moveMotorZIP : Kitronik_Move_Motor.MoveMotorZIP = null
let action = ""
let pause2 = 0
let speed = 0
let Exit = 0
Exit = 0
speed = 50
pause2 = 250
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BaudRate115200)
serial.writeLine("S")
basic.showIcon(IconNames.Chessboard)
basic.forever(function on_forever() {
    
    if (Exit == 0) {
        distance = Kitronik_Move_Motor.measure()
        if (distance > 10) {
            Move()
            serial.writeLine("F")
        } else if (distance < 10) {
            serial.writeLine("L")
            Spin("L")
        }
        
    }
    
})
