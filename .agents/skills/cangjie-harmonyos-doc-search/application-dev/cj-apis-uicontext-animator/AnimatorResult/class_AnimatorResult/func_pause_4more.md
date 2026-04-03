### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消动画，会触发[onCancel](#prop-oncancel)回调。此接口和[finish](#func-finish)接口功能上没有区别，仅触发的回调不同，建议使用[finish](#func-finish)接口结束动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|AInternal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func reverse()

```cangjie
public func reverse(): Unit
```

**功能：** 以相反的顺序播放动画。使用interpolating-spring曲线时此接口无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func setExpectedFrameRateRange(ExpectedFrameRateRange)

```cangjie
public func setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): Unit
```

**功能：** 设置期望的帧率范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rateRange|[ExpectedFrameRateRange](./cj-common-types.md#class-expectedframeraterange)|是|-|帧率范围。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|