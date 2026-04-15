### func readParcelable\<T>(T) where T \<: Parcelable

```cangjie
public func readParcelable<T>(dataIn: T): Unit where T <: Parcelable
```

**功能：** 从MessageSequence实例中读取成员变量到指定的对象（dataIn）。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataIn|T|是|-|需要从MessageSequence读取成员变量的对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900010 | Failed to read data from the message sequence. |
  | 1900012 | Failed to call the JS callback function. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class MyParcelable2 <: Parcelable {
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
    let parcelable = MyParcelable2(1, "aaa")
    let data = MessageSequence.create()
    data.writeParcelable(parcelable)
    let ret = MyParcelable2()
    data.readParcelable(ret)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readParcelableArray\<T>(Array\<T>) where T \<: Parcelable

```cangjie
public func readParcelableArray<T>(parcelableArray: Array<T>): Unit where T <: Parcelable
```

**功能：** 从MessageSequence实例读取可序列化对象数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parcelableArray|Array\<T>|是|-|要读取的可序列化对象数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900010 | Failed to read data from the message sequence. |
  | 1900012 | Failed to call the JS callback function. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class MyParcelable3 <: Parcelable {
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
    let parcelable = MyParcelable3(1, "aaa")
    let parcelable2 = MyParcelable3(2, "bbb")
    let parcelable3 = MyParcelable3(3, "ccc")
    let data = MessageSequence.create()
    data.writeParcelableArray(parcelable,parcelable2,parcelable3)
    let ret: Array<Parcelable> = [MyParcelable3(0, ""), MyParcelable3(0, ""), MyParcelable3(0, "")]
    data.readParcelableArray(ret)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```