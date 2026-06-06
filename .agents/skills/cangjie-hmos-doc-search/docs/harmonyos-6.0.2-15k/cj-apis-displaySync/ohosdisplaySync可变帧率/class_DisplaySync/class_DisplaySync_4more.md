## class DisplaySync

```cangjie
public class DisplaySync {}
```

**功能：** 帧率和回调函数设置实例。用于帧率设置和回调函数的注册，以及启动和停止回调函数的调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func create()

```cangjie
public static func create(): DisplaySync
```

**功能：** 创建[DisplaySync](#class-displaysync)对象，通过此对象设置UI自绘制内容帧率。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DisplaySync](#class-displaysync)|返回当前创建的[DisplaySync](#class-displaysync)对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let backDisplaySync: DisplaySync = DisplaySync.create()
```

### func off(OnOffType, ?Callback1Argument\<IntervalInfo>)

```cangjie
public func off(`type`: OnOffType, callback!: ?Callback1Argument<IntervalInfo> = None): Unit
```

**功能：** 取消订阅每一帧的变化。需先使用[displaySync.create()](#static-func-create)方法获取到[DisplaySync](#class-displaysync)实例，再通过此实例调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[OnOffType](#enum-onofftype)|是|-|设置注册回调的类型（只能是OnOffType.FRAME类型）。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[IntervalInfo](#class-intervalinfo)>|否|None| **命名参数。** 订阅函数，参数不填时，默认取消全部订阅函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import ohos.ui_test.Driver

// 所需要的依赖项
class Callback <: Callback1Argument<IntervalInfo> {
    public Callback() {}
    public open func invoke(arg: IntervalInfo): Unit {
        AppLog.info("Callback invoke success")
    }
}

let driver = Driver.create()
let cb = Callback()
let backDisplaySync: DisplaySync = DisplaySync.create()
backDisplaySync.on(OnOffType.FRAME, cb)
backDisplaySync.off(OnOffType.FRAME, callback: cb)
```

### func on(OnOffType, Callback1Argument\<IntervalInfo>)

```cangjie
public func on(`type`: OnOffType, callback: Callback1Argument<IntervalInfo>): Unit
```

**功能：** 订阅每一帧的变化。需先使用[displaySync.create()](#static-func-create)方法获取到[DisplaySync](#class-displaysync)实例，再通过此实例调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|设置注册回调的类型（只能是OnOffType.FRAME类型）。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[IntervalInfo](#class-intervalinfo)>|是|-|订阅函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import ohos.ui_test.Driver

// 所需要的依赖项
class Callback <: Callback1Argument<IntervalInfo> {
    public Callback() {}
    public open func invoke(arg: IntervalInfo): Unit {
        AppLog.info("Callback invoke success")
    }
}

let driver = Driver.create()
let cb = Callback()
let backDisplaySync: DisplaySync = DisplaySync.create()
backDisplaySync.on(OnOffType.FRAME, cb)
```