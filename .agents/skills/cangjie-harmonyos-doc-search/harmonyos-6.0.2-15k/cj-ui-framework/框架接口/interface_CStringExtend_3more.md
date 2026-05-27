## interface CStringExtend

```cangjie
public interface CStringExtend {
    func free(): Unit
    func toStringOption(): ?String
}
```

**功能：** 仓颉与C互操作字符串类型。内部接口，框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func free()

```cangjie
func free(): Unit
```

**功能：** 释放字符串内存。UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func toStringOption()

```cangjie
func toStringOption(): ?String
```

**功能：** 将CStringExtend类型对象转换为Option类型字符串。UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|?String|Option类型字符串。|

## interface ComponentRender

```cangjie
public interface ComponentRender {
    func initial(): Unit
    func update(): Unit
}
```

**功能：** 组件渲染接口，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func initial()

```cangjie
func initial(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func update()

```cangjie
func update(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## interface LengthProp

```cangjie
public interface LengthProp {
    prop px: Length
    prop vp: Length
    prop fp: Length
    prop percent: Length
    prop lpx: Length
}
```

**功能：** 像素单位。UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop fp

```cangjie
prop fp: Length
```

**功能：** 字体像素，与vp类似适用屏幕密度变化，随系统字体大小设置变化。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 12

### prop lpx

```cangjie
prop lpx: Length
```

**功能：** 视窗逻辑像素单位，l.px单位为实际屏幕宽度与逻辑宽度（通过designWidth配置）的比值，designWidth默认值为720。当designWidth为720时，在实际宽度为1440物理像素的屏幕上，1l.px为2.px大小。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 12

### prop percent

```cangjie
prop percent: Length
```

**功能：** 百分比类型，用于描述以percent像素单位为单位的长度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 12

### prop px

```cangjie
prop px: Length
```

**功能：** 屏幕物理像素单位。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 12

### prop vp

```cangjie
prop vp: Length
```

**功能：** 屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。在实际宽度为1440物理像素的屏幕上，1vp约等于3px。<br/>**说明：** <br/> vp与px的比例与屏幕像素密度有关。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 12