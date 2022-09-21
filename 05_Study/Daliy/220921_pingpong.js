
function includeSeven(x) {
    if ((x - 1) % 10 == 7 || parseInt((x - 1) / 10) % 10 == 7 || parseInt((x - 1) / 100) % 10 == 7) {
        return true
    } else {
        return false
    }
}

function diff(x) {
    if (x == 1) {
        return 1
    } else {
        if ((x - 1) % 7 == 0 || includeSeven(x)) {
            return -diff(x - 1)
        } else {
            return diff(x - 1)
        }
    }
}

function pingpong(x) {
    if (x == 1) {
        return 1
    } else {
        return pingpong(x - 1) + diff(x)
    }
}

console.log(pingpong(8))
console.log(pingpong(22))
console.log(pingpong(68))
console.log(pingpong(100))