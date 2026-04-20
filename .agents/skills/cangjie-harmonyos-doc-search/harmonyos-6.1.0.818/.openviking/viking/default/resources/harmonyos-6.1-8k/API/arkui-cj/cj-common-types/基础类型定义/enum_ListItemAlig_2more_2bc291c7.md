## enum ListItemAlign

```cangjie
public enum ListItemAlign <: Equatable<ListItemAlign> {
    | Start
    | Center
    | End
    | ...
}
```

**功能：** ListItem在List中，交叉轴方向的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ListItemAlign](#enum-listitemalign)>

### Start

```cangjie
Start
```

**功能：** ListItem在List中，交叉轴方向首部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** ListItem在List中，交叉轴方向居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** ListItem在List中，交叉轴方向尾部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ListItemAlign)

```cangjie
public operator func ==(other: ListItemAlign): Bool
```

**功能：** 判断两个ListItemAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListItemAlign](#enum-listitemalign)|是|-|要比较的另一个ListItemAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ListItemAlign)

```cangjie
public operator func !=(other: ListItemAlign): Bool
```

**功能：** 判断两个ListItemAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ListItemAlign](#enum-listitemalign)|是|-|要比较的另一个ListItemAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum StickyStyle

```cangjie
public enum StickyStyle <: Equatable<StickyStyle> {
    | None
    | Header
    | Footer
    | ...
}
```

**功能：** 设置ListItemGroup中header和footer是否要吸顶或吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[StickyStyle](#enum-stickystyle)>

### None

```cangjie
None
```

**功能：** 设置ListItemGroup的headerh不吸顶，footer不吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Header

```cangjie
Header
```

**功能：** 设置ListItemGroup的headerh吸顶。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Footer

```cangjie
Footer
```

**功能：** 设置ListItemGroup的footer吸底。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(StickyStyle)

```cangjie
public operator func ==(other: StickyStyle): Bool
```

**功能：** 判断两个StickyStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StickyStyle](#enum-stickystyle)|是|-|要比较的另一个StickyStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(StickyStyle)

```cangjie
public operator func !=(other: StickyStyle): Bool
```

**功能：** 判断两个StickyStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StickyStyle](#enum-stickystyle)|是|-|要比较的另一个StickyStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|