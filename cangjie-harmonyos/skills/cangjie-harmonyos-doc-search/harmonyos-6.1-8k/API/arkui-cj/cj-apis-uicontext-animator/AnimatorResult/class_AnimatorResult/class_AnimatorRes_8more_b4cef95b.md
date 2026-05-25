## class AnimatorResult

```cangjie
public class AnimatorResult {
}
```

**功能：** 定义Animator结果类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop onFrame

```cangjie
public mut prop onFrame: (Float64) -> Unit
```

**功能：** 接收到帧时回调。

**类型：** (Float64) -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### prop onFinish

```cangjie
public mut prop onFinish: () -> Unit
```

**功能：** 动画完成时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### prop onCancel

```cangjie
public mut prop onCancel: () -> Unit
```

**功能：** 动画被取消时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### prop onRepeat

```cangjie
public mut prop onRepeat: () -> Unit
```

**功能：** 动画重复时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func reset(AnimatorOptions)

```cangjie
public func reset(options: AnimatorOptions): Unit
```

**功能：** 重置当前animator动画参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AnimatorOptions](#class-animatoroptions)|是|-|动画选项。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func play()

```cangjie
public func play(): Unit
```

**功能：** 启动动画。动画会保留上一次的播放状态，比如播放状态设置reverse后，再次播放会保留reverse的播放状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|

### func finish()

```cangjie
public func finish(): Unit
```

**功能：** 结束动画，会触发[onFinish](#prop-onfinish)回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:----|:---|
  |100001|Internal error. Possible causes: The specified page is not found or the object property list is not obtained.|