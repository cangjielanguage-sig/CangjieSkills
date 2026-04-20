## enum FontWeight

```cangjie
public enum FontWeight <: Equatable<FontWeight> {
    | Normal
    | Bold
    | Bolder
    | Lighter
    | Medium
    | Regular
    | W100
    | W200
    | W300
    | W400
    | W500
    | W600
    | W700
    | W800
    | W900
    | ...
}
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FontWeight](#enum-fontweight)>

### Normal

```cangjie
Normal
```

**功能：** 字体粗细正常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bold

```cangjie
Bold
```

**功能：** 字体较粗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bolder

```cangjie
Bolder
```

**功能：** 字体非常粗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Lighter

```cangjie
Lighter
```

**功能：** 字体较细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Medium

```cangjie
Medium
```

**功能：** 字体粗细适中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Regular

```cangjie
Regular
```

**功能：** 字体粗细稍粗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W100

```cangjie
W100
```

**功能：** 100（最细）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W200

```cangjie
W200
```

**功能：** 200。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W300

```cangjie
W300
```

**功能：** 300。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W400

```cangjie
W400
```

**功能：** 400（正常）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W500

```cangjie
W500
```

**功能：** 500。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W600

```cangjie
W600
```

**功能：** 600。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W700

```cangjie
W700
```

**功能：** 700。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W800

```cangjie
W800
```

**功能：** 800。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### W900

```cangjie
W900
```

**功能：** 900（最粗）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FontWeight)

```cangjie
public operator func ==(other: FontWeight): Bool
```

**功能：** 判断两个FontWeight枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FontWeight](#enum-fontweight)|是|-|要比较的另一个FontWeight枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FontWeight)

```cangjie
public operator func !=(other: FontWeight): Bool
```

**功能：** 判断两个FontWeight枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FontWeight](#enum-fontweight)|是|-|要比较的另一个FontWeight枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|