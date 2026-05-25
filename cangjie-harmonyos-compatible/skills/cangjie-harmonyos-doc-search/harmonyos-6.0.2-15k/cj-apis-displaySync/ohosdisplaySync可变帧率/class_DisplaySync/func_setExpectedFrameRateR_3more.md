### func setExpectedFrameRateRange(ExpectedFrameRateRange)

```cangjie
public func setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : Unit
```

**功能：** 设置期望的帧率范围。需先使用[displaySync.create()](#static-func-create)方法获取到[DisplaySync](#class-displaysync)实例，再通过此实例调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rateRange|[ExpectedFrameRateRange](../../arkui-cj/cj-animation-animateto.md#struct-expectedframeraterange)|是|-|设置DisplaySync期望的帧率。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.Incorrect parameters types. 3. Parameter verification failed. or check ExpectedFrameRateRange if valid.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import ohos.component.ExpectedFrameRateRange

let range : ExpectedFrameRateRange = ExpectedFrameRateRange(expected: 10, min:0, max:120)
let backDisplaySync: DisplaySync = DisplaySync.create()
backDisplaySync.setExpectedFrameRateRange(range)
```

### func start()

```cangjie
public func start() : Unit
```

**功能：** 开始每帧回调。需先使用[displaySync.create()](#static-func-create)方法获取到[DisplaySync](#class-displaysync)实例，再通过此实例调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

// 所需要的依赖项
class Callback <: Callback1Argument<IntervalInfo> {
    public Callback() {}
    public open func invoke(arg: IntervalInfo): Unit {
        AppLog.info("Callback invoke success")
    }
}

let cb = Callback()
let backDisplaySync: DisplaySync = DisplaySync.create()
backDisplaySync.on(OnOffType.FRAME, cb)
backDisplaySync.start()
```

### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止每帧回调。需先使用[displaySync.create()](#static-func-create)方法获取到[DisplaySync](#class-displaysync)实例，再通过此实例调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

// 所需要的依赖项
class Callback <: Callback1Argument<IntervalInfo> {
    public Callback() {}
    public open func invoke(arg: IntervalInfo): Unit {
        AppLog.info("Callback invoke success")
    }
}

let cb = Callback()
let backDisplaySync: DisplaySync = DisplaySync.create()
backDisplaySync.on(OnOffType.FRAME, cb)
backDisplaySync.start()
backDisplaySync.stop()
```