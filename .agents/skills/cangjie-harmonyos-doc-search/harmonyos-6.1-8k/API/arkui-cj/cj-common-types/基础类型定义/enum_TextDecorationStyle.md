## enum TextDecorationStyle

```cangjie
public enum TextDecorationStyle <: Equatable<TextDecorationStyle> {
    | Solid
    | Double
    | Dotted
    | Dashed
    | Wavy
    | ...
}
```

**功能：** 设置文本装饰线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextDecorationStyle](#enum-textdecorationstyle)>

### Solid

```cangjie
Solid
```

**功能：** 单实线（默认值）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Double

```cangjie
Double
```

**功能：** 双实线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dotted

```cangjie
Dotted
```

**功能：** 点线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dashed

```cangjie
Dashed
```

**功能：** 虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Wavy

```cangjie
Wavy
```

**功能：** 波浪线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextDecorationStyle)

```cangjie
public operator func ==(other: TextDecorationStyle): Bool
```

**功能：** 判断两个TextDecorationStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextDecorationStyle](#enum-textdecorationstyle)|是|-|要比较的另一个TextDecorationStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextDecorationStyle)

```cangjie
public operator func !=(other: TextDecorationStyle): Bool
```

**功能：** 判断两个TextDecorationStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextDecorationStyle](#enum-textdecorationstyle)|是|-|要比较的另一个TextDecorationStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|