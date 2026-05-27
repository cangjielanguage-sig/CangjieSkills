### func readParcelableArray(Array\<Parcelable>)

```cangjie
public func readParcelableArray(parcelableArray: Array<Parcelable>): Unit
```

**功能：** 从MessageSequence实例读取可序列化对象数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parcelableArray|Array\<[Parcelable](#interface-parcelable)>|是|-|要读取的可序列化对象数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The length of the array passed when reading is not equal to the length passed when writing to the array;<br>5.The element does not exist in the array.|
  |1900010|Failed to read data from the message sequence.|
  |1900012|Failed to call the JS callback function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

// 此处代码可添加在依赖项定义中
class MyParcelable <: Parcelable {
    var num: Int32 = 0
    var str: String = ''

    init() {}

    init(num: Int32, str: String) {
        this.num = num
        this.str = str
    }
    public func marshalling(messageSequence: MessageSequence): Bool {
        messageSequence.writeInt(this.num)
        messageSequence.writeString(this.str)
        return true
    }
    public func unmarshalling(messageSequence: MessageSequence): Bool {
        this.num = messageSequence.readInt()
        this.str = messageSequence.readString()
        return true
    }
}

let parcelable = MyParcelable(1, "aaa")
let parcelable2 = MyParcelable(2, "bbb")
let parcelable3 = MyParcelable(3, "ccc")
let data = MessageSequence.create()
data.writeParcelableArray(parcelable,parcelable2,parcelable3)
let ret: Array<Parcelable> = [MyParcelable(0, ""), MyParcelable(0, ""), MyParcelable(0, "")]
data.readParcelableArray(ret)
```