## class AppEventPackageHolder

```cangjie
public class AppEventPackageHolder {}
```

**功能：** 订阅数据持有者类，用于对订阅事件进行处理。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### static func constructor(String)

```cangjie
public static func constructor(watcherName: String): AppEventPackageHolder
```

**功能：** 类构造函数，创建订阅数据持有者实例，通过观察者名称关联到应用内已添加的观察者对象。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|watcherName|String|是|-|观察者名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[AppEventPackageHolder](#class-appeventpackageholder)|订阅数据持有者类对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let holder = AppEventPackageHolder.constructor("watcher1")
```

### func setSize(Int32)

```cangjie
public func setSize(size!: Int32 = 512*1024): Unit
```

**功能：** 设置每次取出的应用事件包的数据大小阈值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|否|512 * 1024| **命名参数。** 数据大小阈值，单位为byte，取值范围大于等于0，超出范围会抛异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[应用事件打点错误码](../../errorcodes/cj-errorcode-hiappevent.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11104001|Invalid size value.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let holder = AppEventPackageHolder.constructor("watcher2")
holder.setSize(size: 100)
```

### func takeNext()

```cangjie
public func takeNext(): Option<AppEventPackage>
```

**功能：** 根据设置的数据大小阈值来取出订阅事件数据，当订阅事件数据全部被取出时返回None作为标识。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[AppEventPackage](#class-appeventpackage)>|取出的事件包对象，订阅事件数据被全部取出后会返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let holder = AppEventPackageHolder.constructor("watcher3")
if (let Some(v) <- holder.takeNext()) {
    let eventPkg = v
    Hilog.info(0, "HiAppEnvent", "HiAppEvent packageId=${eventPkg.packageId}")
    Hilog.info(0, "HiAppEnvent", "HiAppEvent row=${eventPkg.row}")
    Hilog.info(0, "HiAppEnvent", "HiAppEvent size=${eventPkg.size}")
}
```