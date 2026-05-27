```html
<!--index.html-->
<!DOCTYPE html>
<html lang="en-gb">
<head>
    <title>WebView MessagePort Demo</title>
</head>

<body>
<h1>Html5 Send and Receive Message</h1>
<h3 id="msg">Receive string:</h3>
<h3 id="msg2">Receive arraybuffer:</h3>
<div style="font-size: 80pt; text-align: center;">
    <input type="button" value="Send String" onclick="postStringToApp();" /><br/>
    <input type="button" value="Send Number" onclick="postNumberToApp();" /><br/>
    <input type="button" value="Send NumberF" onclick="postNumberFToApp();" /><br/>
    <input type="button" value="Send Bool" onclick="postBoolToApp();" /><br/>
    <input type="button" value="Send Buffer" onclick="postBufferToApp();" /><br/>
    <input type="button" value="Send Array" onclick="postArrayToApp();" /><br/>
    <input type="button" value="Send Error" onclick="postErrorToApp();" /><br/>
</div>
</body>
<script src="index.js"></script>
</html>
```

```js
//index.js
var h5Port;
window.addEventListener('message', function(event) {
    if (event.data == 'init_web_messageport') {
        if(event.ports[0] != null) {
            h5Port = event.ports[0]; // 1. 保存从ets侧发送过来的端口
            h5Port.onmessage = function(event) {
                console.log("hwd In html got message");
                // 2. 接收ets侧发送过来的消息.
                var result = event.data;
                console.log("In html got message, typeof: ", typeof(result));
                console.log("In html got message, result: ", (result));
                if (typeof(result) == "string") {
                    console.log("In html got message, String: ", result);
                    document.getElementById("msg").innerHTML  =  "String: " + result;
                } else if (typeof(result) == "number") {
                    console.log("In html side got message, number: ", result);
                    document.getElementById("msg").innerHTML = "Number: " + result;
                } else if (typeof(result) == "boolean") {
                    console.log("In html side got message, boolean: ", result);
                    document.getElementById("msg").innerHTML = "Boolean: " + result;
                } else if (typeof(result) == "object") {
                    if (result instanceof ArrayBuffer) {
                        const decoder = new TextDecoder();
                        const str = decoder.decode(result);
                        document.getElementById("msg2").innerHTML  =  "ArrayBuffer: " + str + result.byteLength;
                        console.log("In html got message, byteLength: ", result.byteLength);
                    } else if (result instanceof Error) {
                        console.log("In html error message, err: " + (result));
                        console.log("In html error message, typeof err: " + typeof(result));
                        document.getElementById("msg2").innerHTML  =  "Error: " + result.name + ", msg: " + result.message;
                    } else if (result instanceof Array) {
                        console.log("In html got message, Array");
                        console.log("In html got message, Array length: " + result.length);
                        console.log("In html got message, Array[0]: " + (result[0]));
                        console.log("In html got message, typeof Array[0]:" + typeof(result[0]));
                        document.getElementById("msg2").innerHTML  =  "Array len: " + result.length + ", value: " + result;
                    } else {
                        console.log("In html got message, not any instance of support type");
                        document.getElementById("msg").innerHTML  = "not any instance of support type";
                    }
                } else {
                    console.log("In html got message, not support type");
                    document.getElementById("msg").innerHTML  = "not support type";
                }
            }
            h5Port.onmessageerror = (event) => {
                console.error(`hwd In html Error receiving message: ${event}`);
            };
        }
    }
})