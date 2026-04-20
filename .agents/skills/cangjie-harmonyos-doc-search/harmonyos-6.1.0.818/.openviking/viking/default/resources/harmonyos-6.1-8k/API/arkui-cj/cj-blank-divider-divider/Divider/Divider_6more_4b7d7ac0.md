# Divider

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供分隔器组件，分隔不同内容块/内容元素。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个分隔器组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func color(?ResourceColor)

```cangjie
public func color(value: ?ResourceColor): This
```

**功能：** 设置分割线的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | ?[ResourceColor](./cj-common-types.md#interface-resourcecolor) | 是   | -   | 分割线颜色。初始值: 0x33182431 |

### func lineCap(?LineCapStyle)

```cangjie
public func lineCap(value: ?LineCapStyle): This
```

**功能：** 设置当前在容器中的分割线端点样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | ?[LineCapStyle](./cj-common-types.md#enum-linecapstyle) | 是  | - | 分割线条的端点样式。初始值: LineCapStyle.Butt |

### func strokeWidth(?Length)

```cangjie
public func strokeWidth(value: ?Length): This
```

**功能：** 设置当前在容器中的分割线宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | ?[Length](./cj-common-types.md#interface-length)| 是 | - | 分割线宽度。不指定像素单位时，默认单位vp。不支持百分比设置。不支持百分比设置。优先级低于通用属性[height](./cj-universal-attribute-size.md#func-heightoptionlength)，超过通用属性设置大小时，按照通用属性进行裁切。部分设备硬件中存在1像素取整后分割线不显示问题，建议使用2像素。初始值: 1.0.px |

### func vertical(?Bool)

```cangjie
public func vertical(value: ?Bool): This
```

**功能：** 设置分割线的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | ?Bool | 是   | -   | 设置分割线的方向。初始值: false |