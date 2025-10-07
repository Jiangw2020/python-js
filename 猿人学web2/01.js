const CryptoJS = require('crypto-js');

function get_param(page){
    var time = Date.parse(new Date()).toString()
    var key = '666yuanrenxue66';
    var text = time+page
    text = CryptoJS.enc.Utf8.parse(text)
    key = CryptoJS.enc.Utf8.parse(key)
    v = CryptoJS.AES.encrypt(text, key,{
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
    return  {
        'page': page,
        'token': v,
        'now': time,
    }
}
console.log(get_param(1))
