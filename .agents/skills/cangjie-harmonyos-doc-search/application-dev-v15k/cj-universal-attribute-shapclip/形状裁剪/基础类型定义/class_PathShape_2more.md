### class PathShape

```cangjie
public class PathShape <: ShapeAbstract {
    public init()
    public init(commands!: String)
    public init(width!: Length, height!: Length, commands!: String = "")
}
```

**功能：** 用于clip和mask接口的自定义绘制路径形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

[ShapeAbstract](#class-shapeabstract)

#### init()

```cangjie
public init()
```

**功能：** 构造一个默认参数的自定义形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(String)

```cangjie
public init(commands!: String)
```

**功能：** 根据路径绘制的命令字符串，构造一个自定义形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|commands|String|是|-| **命名参数。** 路径绘制的命令字符串。|

#### init(Length, Length, String)

```cangjie
public init(width!: Length, height!: Length, commands!: String = "")
```

**功能：** 根据设定的长宽、路径绘制的命令字符串，构造一个自定义形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径所在矩形的宽度。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径所在矩形的高度。|
|commands|String|否|""| **命名参数。** 路径绘制的命令字符串。|

### class ProgressMask

```cangjie
public class ProgressMask {
    public init(value!:Float32,total!:Float32,color!:Color)
}
```

**功能：** 设置遮罩的进度、最大值和遮罩颜色的形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, Float32, Color)

```cangjie
public init(value!:Float32,total!:Float32,color!:Color)
```

**功能：** 构造ProgressMask对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是| - | 进度遮罩的当前值。|
|total|Float32|是| - |进度遮罩的最大值。 |
|color|[Color](./cj-common-types.md#class-color)|是| - |进度遮罩的颜色。 |

#### func updateProgress(Float32)

```cangjie
public func updateProgress(number: Float32): Unit
```

**功能：** 更新进度遮罩的进度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|Float32|是| - | 进度遮罩的当前值。|

#### func updateColor(Color)

```cangjie
public func updateProgress(color: Color): Unit
```

**功能：** 更新进度遮罩的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[Color](./cj-common-types.md#class-color)|是| - | 进度遮罩的颜色。|

#### func enableBreathingAnimation(Bool)

```cangjie
public func enableBreathingAnimation(value:Bool):Unit
```

**功能：** 进度满时的呼吸光晕动画开关。默认关闭呼吸光晕动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是| - | 是否开启呼吸光晕动画。</br> 设置为true则开启呼吸光晕动画。初始值：false。 |