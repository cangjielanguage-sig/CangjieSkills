# MeasureUtils

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供文本宽度、高度等相关计算。

> **说明：**
>
> 以下API需先使用[UIContext](./cj-apis-uicontext-uicontext.md#class-uicontext)中的[getMeasureUtils()](./cj-apis-uicontext-uicontext.md#func-getmeasureutils)方法获取MeasureUtils实例，再通过此实例调用对应方法。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## class MeasureUtils

```cangjie
public class MeasureUtils {}
```

**功能：** 提供文本宽度、高度等相关计算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func measureText(MeasureOptions)

```cangjie
public func measureText(options: MeasureOptions): Float64
```

**功能：** 计算指定文本单行布局下的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[MeasureOptions](#class-measureoptions)|是|-|被计算文本描述信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Float64|文本宽度。单位：px。|

### func measureTextSize(MeasureOptions)

```cangjie
public func measureTextSize(options: MeasureOptions): SizeOptions
```

**功能：** 测量文本的宽度和高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[MeasureOptions](#class-measureoptions)|是|-|被计算文本描述信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[SizeOptions](#class-sizeoptions)|返回文本所占布局宽度和高度。单位：px。|