### class GutterOption

```cangjie
public class GutterOption {
    public init(x!: ?Length = None, y!: ?Length = None)
    public init(x!: ?GridRowSizeOption, y!: ?GridRowSizeOption)
}
```

**功能：** 栅格布局间距类型，用于描述栅格子组件不同方向的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?Length)

```cangjie
public init(x!: ?Length = None, y!: ?Length = None)
```

**功能：** 构造一个GutterOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 栅格子组件x方向的间距。<br>初始值：0.vp|
|y|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 栅格子组件y方向的间距。<br>初始值：0.vp|

#### init(?GridRowSizeOption, ?GridRowSizeOption)

```cangjie
public init(x!: ?GridRowSizeOption, y!: ?GridRowSizeOption)
```

**功能：** 构造一个GutterOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[GridRowSizeOption](#class-gridrowsizeoption)|是|-| **命名参数。** 栅格子组件x方向的间距。<br>初始值：GridRowSizeOption()|
|y|?[GridRowSizeOption](#class-gridrowsizeoption)|是|-| **命名参数。** 栅格子组件y方向的间距。<br>初始值：GridRowSizeOption()|