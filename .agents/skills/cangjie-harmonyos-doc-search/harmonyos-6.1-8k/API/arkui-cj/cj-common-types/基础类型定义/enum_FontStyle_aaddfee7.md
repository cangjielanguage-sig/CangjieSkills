## enum FontStyle

```cangjie
public enum FontStyle <: Equatable<FontStyle> {
    | Normal
    | Italic
    | ...
}
```

**功能：** 字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FontStyle](#enum-fontstyle)>

### Normal

```cangjie
Normal
```

**功能：** 标准字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Italic

```cangjie
Italic
```

**功能：** 斜体字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FontStyle)

```cangjie
public operator func ==(other: FontStyle): Bool
```

**功能：** 判断两个FontStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FontStyle](#enum-fontstyle)|是|-|要比较的另一个FontStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FontStyle)

```cangjie
public operator func !=(other: FontStyle): Bool
```

**功能：** 判断两个FontStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FontStyle](#enum-fontstyle)|是|-|要比较的另一个FontStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|