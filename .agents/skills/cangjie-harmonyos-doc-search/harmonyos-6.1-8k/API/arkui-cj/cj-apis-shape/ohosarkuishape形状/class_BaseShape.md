## class BaseShape

```cangjie
public abstract class BaseShape {}
```

**功能：** 图形基类，提供图形的基本属性和方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func fill(?ResourceColor)

```cangjie
public func fill(color: ?ResourceColor): This
```

**功能：** 设置填充区域的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|填充区域的颜色。|

### func height(?Length)

```cangjie
public func height(height: ?Length): This
```

**功能：** 设置图形高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|height|?[Length](./cj-common-types.md#interface-length)|是|-|图形高度。|

### func offset(?Length, ?Length)

```cangjie
public func offset(x!: ?Length, y!: ?Length): This
```

**功能：** 设置图形偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** x轴偏移。<br>初始值：0.0.px。|
|y|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** y轴偏移。<br>初始值：0.0.px。|

### func size(?Length, ?Length)

```cangjie
public func size(width!: ?Length, height!: ?Length): This
```

**功能：** 设置图形尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图形宽度。<br>初始值：0.0.vp。|
|height|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图形高度。<br>初始值：0.0.vp。|

### func width(?Length)

```cangjie
public func width(width: ?Length): This
```

**功能：** 设置图形宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|是|-|图形宽度。|