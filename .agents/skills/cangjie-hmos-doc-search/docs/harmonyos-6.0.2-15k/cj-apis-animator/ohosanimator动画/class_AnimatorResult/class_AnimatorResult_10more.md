## class AnimatorResult

```cangjie
public class AnimatorResult {
    public init(options: AnimatorOptions)
}
```

**功能：** 定义动画的初始化类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop oncancel

```cangjie
public mut prop oncancel: () -> Unit
```

**功能：** 动画被取消时回调。即将废弃，推荐使用onCancel。

**类型：** () -> Unit

**读写能力：** 可读写

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onCancel

```cangjie
public mut prop onCancel: () -> Unit
```

**功能：** 动画被取消时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onfinish

```cangjie
public mut prop onfinish: () -> Unit
```

**功能：** 动画完成时回调。即将废弃，推荐使用onFinish。

**类型：** () -> Unit

**读写能力：** 可读写

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onFinish

```cangjie
public mut prop onFinish: () -> Unit
```

**功能：** 动画完成时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onframe

```cangjie
public mut prop onframe: (Float64) -> Unit
```

**功能：** 接收到帧时回调。即将废弃，推荐使用onFrame。

**类型：** (Float64) -> Unit

**读写能力：** 可读写

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onFrame

```cangjie
public mut prop onFrame: (Float64) -> Unit
```

**功能：** 接收到帧时回调。

**类型：** (Float64) -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onrepeat

```cangjie
public mut prop onrepeat: () -> Unit
```

**功能：** 动画重复时回调。即将废弃，推荐使用onRepeat。

**类型：** () -> Unit

**读写能力：** 可读写

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### prop onRepeat

```cangjie
public mut prop onRepeat: () -> Unit
```

**功能：** 动画重复时回调。

**类型：** () -> Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**异常：**

- BusinessException：对应错误码如下表。

  |错误码ID|错误信息|
  |:---|:---|
  |100001|AnimatorResult play failed: Internal error.|

### init(AnimatorOptions)

```cangjie
public init(options: AnimatorOptions)
```

**功能：** 创建一个AnimatorResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AnimatorOptions](#class-animatoroptions)|是|-|定义动画选项。|