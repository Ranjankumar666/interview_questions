function tailRecursion(x, total = 1) {
    if (x == 1) return total
    
    return tailRecursion(x-1, total*x)
}

console.log(tailRecursion(5))