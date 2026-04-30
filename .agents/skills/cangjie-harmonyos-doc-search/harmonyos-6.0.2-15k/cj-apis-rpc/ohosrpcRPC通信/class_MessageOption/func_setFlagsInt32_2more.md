### func setFlags(Int32)

```cangjie
public func setFlags(flags: Int32): Unit
```

**功能：** 设置同步调用或异步调用标志。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flags|Int32|是|-|同步调用或异步调用标志。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.setFlags(1)
```

### func setWaitTime(Int32)

```cangjie
public func setWaitTime(waitTime: Int32): Unit
```

**功能：** 设置rpc调用最长等待时间。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|waitTime|Int32|是|-|rpc调用最长等待时间，上限为3000秒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let mo = MessageOption()
mo.setWaitTime(1)
```