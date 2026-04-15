## enum Alignment

```cangjie
public enum Alignment <: Equatable<Alignment> {
    | TopStart
    | Top
    | TopEnd
    | Start
    | Center
    | End
    | BottomStart
    | Bottom
    | BottomEnd
    | ...
}
```

**功能：** 对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Alignment](#enum-alignment)>

### TopStart

```cangjie
TopStart
```

**功能：** 顶部起始端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 顶部横向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopEnd

```cangjie
TopEnd
```

**功能：** 顶部尾端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Start

```cangjie
Start
```

**功能：** 起始端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 横向和纵向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 尾端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomStart

```cangjie
BottomStart
```

**功能：** 底部起始端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 底部横向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomEnd

```cangjie
BottomEnd
```

**功能：** 底部尾端。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Alignment)

```cangjie
public operator func ==(other: Alignment): Bool
```

**功能：** 判断两个Alignment枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Alignment](#enum-alignment)|是|-|要比较的另一个Alignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Alignment)

```cangjie
public operator func !=(other: Alignment): Bool
```

**功能：** 判断两个Alignment枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Alignment](#enum-alignment)|是|-|要比较的另一个Alignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|