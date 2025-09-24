import frida
import sys

rdev = frida.get_usb_device()
print(frida.get_remote_device())
print(frida.get_usb_device())
pid = rdev.spawn("com.che168.autotradercloud")
# pid = 25850

print('pid' + str(pid))
session = rdev.attach(pid)
scr = """
Java.perform(function(){
let SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
SecurityUtil["encodeMD5"].implementation = function(str){
    console.log(`SecurityUtil.encodeMD5 is called: str =${str}`);
let result = this["encodeMD5"](str);
console.log(`SecurityUtil.encodeMD5 result =${result}`);
return '123';
}
});
"""

script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()
