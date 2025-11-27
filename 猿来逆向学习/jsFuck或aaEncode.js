// hook eval
(function (){
    var  eval_ = eval;
    eval = function (s) {
        console.log(s);
        debugger;
        return eval_.apply(this,arguments)
    }
})();

// hook Function
var Function_ = Function;
Function = function () {
    debugger
    return Function_.apply(this,arguments)
}


// hook Function.prototype.constructor
var Function_ = Function.prototype.constructor;
Function.prototype.constructor = function () {
    debugger
    return Function_.apply(this,arguments)
}


// VM
// 要么是eval，要么是Function，要么是Function.prototype.constructor
