## enum DialogAlignment

```cangjie
public enum DialogAlignment <: Equatable<DialogAlignment> {
    | Top
    | Center
    | Bottom
    | Default
    | TopStart
    | TopEnd
    | CenterStart
    | CenterEnd
    | BottomStart
    | BottomEnd
    | ...
}
```

**功能：** 弹窗在竖直方向上的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[DialogAlignment](#enum-dialogalignment)>

### Top

```cangjie
Top
```

**功能：** 垂直顶部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 垂直居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 底部横向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Default

```cangjie
Default
```

**功能：** 默认对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopStart

```cangjie
TopStart
```

**功能：** 对齐左上角。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopEnd

```cangjie
TopEnd
```

**功能：** 对齐右上角。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### CenterStart

```cangjie
CenterStart
```

**功能：** 左侧居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### CenterEnd

```cangjie
CenterEnd
```

**功能：** 右侧居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomStart

```cangjie
BottomStart
```

**功能：** 底部起始端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomEnd

```cangjie
BottomEnd
```

**功能：** 底部尾端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(DialogAlignment)

```cangjie
public operator func ==(other: DialogAlignment): Bool
```

**功能：** 判断两个DialogAlignment枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogAlignment](#enum-dialogalignment)|是|-|要比较的另一个DialogAlignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(DialogAlignment)

```cangjie
public operator func !=(other: DialogAlignment): Bool
```

**功能：** 判断两个DialogAlignment枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogAlignment](#enum-dialogalignment)|是|-|要比较的另一个DialogAlignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|