# ohos.measure（文本计算）

提供文本宽度、高度等相关计算。

## 导入模块

```cangjie
import kit.UIKit.*
```

## class Measure

```cangjie
public class Measure {}
```

**功能：** 计算文本布局占用宽度和高度的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func MeasureText(MeasureOptions)

```cangjie
public static func MeasureText(options: MeasureOptions): Float64
```

**功能：** 计算指定文本的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[MeasureOptions](#class-measureoptions)|是|-|被计算文本描述信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Float64|返回文本宽度，单位px。|

### static func MeasureTextSize(MeasureOptions)

```cangjie
public static func MeasureTextSize(options: MeasureOptions): Size
```

**功能：** 计算指定文本的宽度和高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[MeasureOptions](#class-measureoptions)|是|-|被计算文本描述信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[Size](#struct-size)|返回文本所占布局宽度和高度，单位均为px。|