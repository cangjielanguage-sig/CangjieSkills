// 使用h5Port往ets侧发送String类型的消息.
function postStringToApp() {
    if (h5Port) {
        console.log("In html send string message");
        h5Port.postMessage("hello");
        console.log("In html send string message end");
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送Number类型的消息.
function postNumberToApp() {
    if (h5Port) {
        h5Port.postMessage(12349);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送Number类型的消息.
function postNumberFToApp() {
    if (h5Port) {
        h5Port.postMessage(12349.8);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送Bool类型的消息.
function postBoolToApp() {
    if (h5Port) {
        h5Port.postMessage(false);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送ArrayBuffer类型的消息.
function postBufferToApp() {
    if (h5Port) {
        let a = new ArrayBuffer(12);
        h5Port.postMessage(a);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送Array类型的消息.
function postArrayToApp() {
    if (h5Port) {
        h5Port.postMessage([true, false]);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
// 使用h5Port往ets侧发送Error类型的消息.
function postErrorToApp() {
    if (h5Port) {
        let e = new RangeError("errormessage")
        h5Port.postMessage(e);
    } else {
        console.error("In html h5port is null, please init first");
    }
}
```