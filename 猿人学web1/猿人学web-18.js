const CryptoJS = require('crypto-js');

function get_param(page){
    var time = Date.parse(new Date())/1000;
    // var time = 1759801488;

    var key = time.toString(16) + time.toString(16);
    console.log(key)
    var text = page +"|756d103,757m103,758m103,758m103,758u103"
    text = CryptoJS.enc.Utf8.parse(text)
    key = CryptoJS.enc.Utf8.parse(key)
    v = CryptoJS.AES.encrypt(text, key,{
        iv: key,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
    return  {
        'v': v,
        't': time,
    }
}
// console.log(get_param(1))
