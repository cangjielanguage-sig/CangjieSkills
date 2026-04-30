## class MessageOption

```cangjie
public class MessageOption {
    public static const TF_SYNC: Int32 = 0x00
    public static const TF_ASYNC: Int32 = 0x01
    public static const TF_ACCEPT_FDS: Int32 = 0x10
    public static const TF_WAIT_TIME: Int32 = 0x8
    public init(async!: Bool = false, waitTime!: Int32 = MessageOption.TF_WAIT_TIME)
}
```

**功能：** 公共消息选项，使用指定的标志类型，构造指定的MessageOption对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### static const TF_ACCEPT_FDS

```cangjie
public static const TF_ACCEPT_FDS: Int32 = 0x10
```

**功能：** 指示sendMessageRequest9+接口可以传递文件描述符。

**类型：** Int32

**起始版本：** 19

### static const TF_ASYNC

```cangjie
public static const TF_ASYNC: Int32 = 0x01
```

**功能：** 异步调用标识。

**类型：** Int32

**起始版本：** 19

### static const TF_SYNC

```cangjie
public static const TF_SYNC: Int32 = 0x00
```

**功能：** 同步调用标识。

**类型：** Int32

**起始版本：** 19

### static const TF_WAIT_TIME

```cangjie
public static const TF_WAIT_TIME: Int32 = 0x8
```

**功能：** RPC等待时间（单位/秒），不用于IPC的情况。

**类型：** Int32

**起始版本：** 19

### init(Bool, Int32)

```cangjie
public init(async!: Bool = false, waitTime!: Int32 = MessageOption.TF_WAIT_TIME)
```

**功能：** MessageOption构造函数。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|async|Bool|否|false| **命名参数。** true：表示异步调用标志，false：表示同步调用标志。默认同步调用。|
|waitTime|Int32|否|MessageOption.TF_WAIT_TIME| **命名参数。** 调用rpc最长等待时间。默认TF_WAIT_TIME。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
```

### func getFlags()

```cangjie
public func getFlags(): Int32
```

**功能：** 获取同步调用或异步调用标志。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|调用成功返回同步调用或异步调用标志。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.getFlags()
```

### func getWaitTime()

```cangjie
public func getWaitTime(): Int32
```

**功能：** 获取rpc调用的最长等待时间。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|rpc最长等待时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.getWaitTime()
```

### func isAsync()

```cangjie
public func isAsync(): Bool
```

**功能：** 获取SendMessageRequest调用中确定同步或是异步的标志。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：异步调用成功，false：同步调用成功。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.isAsync()
```

### func setAsync(Bool)

```cangjie
public func setAsync(async: Bool): Unit
```

**功能：** 设置SendMessageRequest调用中确定同步或是异步的标志。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|async|Bool|是|-|true：表示异步调用标志，false：表示同步调用标志。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.setAsync(true)
```