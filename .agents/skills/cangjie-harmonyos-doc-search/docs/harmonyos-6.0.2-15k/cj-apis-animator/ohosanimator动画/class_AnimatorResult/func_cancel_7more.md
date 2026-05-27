### func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func finish()

```cangjie
public func finish(): Unit
```

**功能：** 结束动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### func play()

```cangjie
public func play(): Unit
```

**功能：** 启动动画。动画会保留上一次的播放状态，比如播放状态设置reverse后，再次播放会保留reverse的播放状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### func reset(AnimatorOptions)

```cangjie
public func reset(options: AnimatorOptions): Unit
```

**功能：** 更新当前动画器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AnimatorOptions](#class-animatoroptions)|是|-|定义动画选项。|

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### func reverse()

```cangjie
public func reverse(): Unit
```

**功能：** 以相反的顺序播放动画。使用interpolating-spring曲线时此接口无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### func setExpectedFrameRateRange(ExpectedFrameRateRange)

```cangjie
public func setExpectedFrameRateRange(framerateRange: ExpectedFrameRateRange): Unit
```

**功能：** 设置期望的帧率范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|framerateRange|[ExpectedFrameRateRange](./cj-animation-animateto.md#class-expectedframeraterange)|是|-|设置期望的帧率范围。要求满足约束：0 < ExpectedFrameRateRange.min <= ExpectedFrameRateRange.expected <= ExpectedFrameRateRange.max，如不满足要求，按照默认值 ExpectedFrameRateRange(min:60, max:120, expected:60) 传参。|

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|