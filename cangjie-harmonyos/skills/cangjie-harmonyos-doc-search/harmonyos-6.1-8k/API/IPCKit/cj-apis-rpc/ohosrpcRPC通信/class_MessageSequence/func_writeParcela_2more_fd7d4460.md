### func writeParcelable\<T>(T) where T \<: Parcelable

```cangjie
public func writeParcelable<T>(val: T): Unit where T <: Parcelable
```

**功能：** 将自定义序列化对象写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|T|是|-|要写入的可序列对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900009 | Failed to write data to the message sequence. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class MyParcelable4 <: Parcelable {
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

try {
    let parcelable = MyParcelable4(1, "aaa")
    let data = MessageSequence.create()
    data.writeParcelable(parcelable)
    let ret = MyParcelable4()
    data.readParcelable(ret)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeParcelableArray\<T>(Array\<T>) where T \<: Parcelable

```cangjie
public func writeParcelableArray<T>(parcelableArray: Array<T>): Unit where T <: Parcelable
```

**功能：** 将可序列化对象数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parcelableArray|Array\<T>|是|-|要写入的可序列化对象数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900009 | Failed to write data to the message sequence. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class MyParcelable5 <: Parcelable {
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

try {
    let parcelable = MyParcelable5(1, "aaa")
    let parcelable2 = MyParcelable5(2, "bbb")
    let parcelable3 = MyParcelable5(3, "ccc")
    let data = MessageSequence.create()
    data.writeParcelableArray(parcelable,parcelable2,parcelable3)
    let ret: Array<Parcelable> = [MyParcelable5(0, ""), MyParcelable5(0, ""), MyParcelable5(0, "")]
    data.readParcelableArray(ret)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```