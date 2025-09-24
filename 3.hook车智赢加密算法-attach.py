import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("车智赢+") # 需要hook的app名称

scr = """
Java.perform(function(){
let SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
SecurityUtil["encodeMD5"].implementation = function(str){
    console.log(`SecurityUtil.encodeMD5 is called: str =${str}`);
let result = this["encodeMD5"](str);
console.log(`SecurityUtil.encodeMD5 result =${result}`);
return str;
}
});
"""


script = session.create_script(scr)

def on_message(message,data):
    print(11)

script.on("message",on_message)
script.load()
sys.stdin.read()
