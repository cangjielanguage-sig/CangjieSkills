### func getCapacity()

```cangjie
public func getCapacity(): UInt32
```

**功能：** 获取当前MessageSequence对象的容量大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取的MessageSequence实例的容量大小。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let result = data.getCapacity()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getRawDataCapacity()

```cangjie
public func getRawDataCapacity(): UInt32
```

**功能：** 获取MessageSequence可以容纳的最大原始数据量。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence可以容纳的最大原始数据量，即128MB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let capacity = data.getRawDataCapacity()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getReadPosition()

```cangjie
public func getReadPosition(): UInt32
```

**功能：** 获取MessageSequence的读位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence实例中的当前读取位置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let pos = data.getReadPosition()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getReadableBytes()

```cangjie
public func getReadableBytes(): UInt32
```

**功能：** 获取MessageSequence的可读字节空间。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取到的MessageSequence实例的可读字节空间。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let bytes = data.getReadableBytes()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getSize()

```cangjie
public func getSize(): UInt32
```

**功能：** 获取当前创建的MessageSequence对象的数据大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取的MessageSequence实例的数据大小。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let size = data.getSize()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```