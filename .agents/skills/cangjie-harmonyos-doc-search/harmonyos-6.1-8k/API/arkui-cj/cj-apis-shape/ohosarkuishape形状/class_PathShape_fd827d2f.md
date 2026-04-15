## class PathShape

```cangjie
public class PathShape <: BaseShape {
    public init(commands!: ?ResourceStr = None)
    public init(width!: ?Length, height!: ?Length, commands!: ?ResourceStr = None)
}
```

**功能：** 用于[clipShape](./cj-universal-attribute-shapclip.md#func-clipshapebaseshape)和[maskShape](./cj-universal-attribute-shapclip.md#func-maskshapebaseshape)接口的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseShape](#class-baseshape)

### init(?ResourceStr)

```cangjie
public init(commands!: ?ResourceStr = None)
```

**功能：** PathShape的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|commands|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 路径的绘制指令。<br>初始值：""。<br>更多说明请参考commands支持的[绘制命令](./cj-graphic-drawing-path.md#func-commandsresourcestr)。|

### init(?Length, ?Length, ?ResourceStr)

```cangjie
public init(width!: ?Length, height!: ?Length, commands!: ?ResourceStr = None)
```

**功能：** PathShape的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径宽度。<br>初始值：0.vp。|
|height|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径高度。<br>初始值：0.vp。|
|commands|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 路径命令。<br>初始值：""。<br>更多说明请参考commands支持的[绘制命令](./cj-graphic-drawing-path.md#func-commandsresourcestr)。|