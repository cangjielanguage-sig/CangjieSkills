## enum BlurStyle

```cangjie
public enum BlurStyle <: Equatable<BlurStyle> {
    | Thin
    | Regular
    | Thick
    | BackgroundThin
    | BackgroundRegular
    | BackgroundThick
    | BackgroundUltraThick
    | None
    | ComponentUltraThin
    | ComponentThin
    | ComponentRegular
    | ComponentThick
    | ComponentUltraThick
    | ...
}
```

**功能：** 前景模糊样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BlurStyle](#enum-blurstyle)>

### Thin

```cangjie
Thin
```

**功能：** 薄模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Regular

```cangjie
Regular
```

**功能：** 普通模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Thick

```cangjie
Thick
```

**功能：** 厚模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BackgroundThin

```cangjie
BackgroundThin
```

**功能：** 近距景深模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BackgroundRegular

```cangjie
BackgroundRegular
```

**功能：** 中距景深模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BackgroundThick

```cangjie
BackgroundThick
```

**功能：** 远距景深模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BackgroundUltraThick

```cangjie
BackgroundUltraThick
```

**功能：** 超远距景深模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 无模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ComponentUltraThin

```cangjie
ComponentUltraThin
```

**功能：** 组件超薄材质模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ComponentThin

```cangjie
ComponentThin
```

**功能：** 组件轻薄材质模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ComponentRegular

```cangjie
ComponentRegular
```

**功能：** 组件普通材质模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ComponentThick

```cangjie
ComponentThick
```

**功能：** 组件厚材质模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ComponentUltraThick

```cangjie
ComponentUltraThick
```

**功能：** 组件超厚材质模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BlurStyle)

```cangjie
public operator func ==(other: BlurStyle): Bool
```

**功能：** 判断两个BlurStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BlurStyle](#enum-blurstyle)|是|-|要比较的另一个BlurStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BlurStyle)

```cangjie
public operator func !=(other: BlurStyle): Bool
```

**功能：** 判断两个BlurStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BlurStyle](#enum-blurstyle)|是|-|要比较的另一个BlurStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|