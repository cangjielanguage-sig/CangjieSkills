## class RectShape

```cangjie
public class RectShape <: BaseShape {
    public init(width!: ?Length = None, height!: ?Length = None)
}
```

**功能：** 用于[clipShape](./cj-universal-attribute-shapclip.md#func-clipshapebaseshape)和[maskShape](./cj-universal-attribute-shapclip.md#func-maskshapebaseshape)接口的矩形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseShape](#class-baseshape)

### init(?Length, ?Length)

```cangjie
public init(width!: ?Length = None, height!: ?Length = None)
```

**功能：** RectShape的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 矩形宽度。<br>初始值：0.vp。|
|height|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 矩形高度。<br>初始值：0.vp。|

### func radius(?Length)

```cangjie
public func radius(value: ?Length): This
```

**功能：** 设置矩形圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|矩形圆角半径。<br>初始值：0.vp。|

### func radiusHeight(?Length)

```cangjie
public func radiusHeight(value: ?Length): This
```

**功能：** 设置矩形垂直圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|矩形垂直圆角半径。<br>初始值：0.vp。|

### func radiusWidth(?Length)

```cangjie
public func radiusWidth(value: ?Length): This
```

**功能：** 设置矩形水平圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|矩形水平圆角半径。<br>初始值：0.vp。|