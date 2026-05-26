## interface Parcelable

```cangjie
public interface Parcelable {
    func marshalling(dataOut: MessageSequence): Bool
    func unmarshalling(dataIn: MessageSequence): Bool
}
```

**功能：** 在进程间通信（IPC）期间，将类的对象写入MessageSequence并从MessageSequence中恢复它们。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### func marshalling(MessageSequence)

```cangjie
func marshalling(dataOut: MessageSequence): Bool
```

**功能：** 将此可序列对象封送到MessageSequence中。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataOut|[MessageSequence](#class-messagesequence)|是|-|可序列对象将被封送到的MessageSequence对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：封送成功，false：封送失败。|

### func unmarshalling(MessageSequence)

```cangjie
func unmarshalling(dataIn: MessageSequence): Bool
```

**功能：** 从MessageSequence中解封此可序列对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataIn|[MessageSequence](#class-messagesequence)|是|-|已将可序列对象封送到其中的MessageSequence对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：反序列化成功，false：反序列化失败。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

// 此处代码可添加在依赖项定义中
class MyParcelable <: Parcelable {
    var num: Int32 = 0
    var str: String = ''
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
let data = MessageSequence.create()
parcelable.marshalling(data)
parcelable.unmarshalling(data)
```