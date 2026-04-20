## enum ArrowPosition

```cangjie
public enum ArrowPosition <: Equatable<ArrowPosition> {
    | End
    | Start
    | ...
}
```

**功能：** 下拉菜单项的文本与箭头之间的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ArrowPosition](#enum-arrowposition)>

### End

```cangjie
End
```

**功能：** 文字在前，箭头在后。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Start

```cangjie
Start
```

**功能：** 箭头在前，文字在后。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ArrowPosition)

```cangjie
public operator func ==(other: ArrowPosition): Bool
```

**功能：** 判断两个ArrowPosition枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ArrowPosition](#enum-arrowposition)|是|-|要比较的另一个ArrowPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ArrowPosition)

```cangjie
public operator func !=(other: ArrowPosition): Bool
```

**功能：** 判断两个ArrowPosition枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ArrowPosition](#enum-arrowposition)|是|-|要比较的另一个ArrowPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum MenuAlignType

```cangjie
public enum MenuAlignType <: Equatable<MenuAlignType> {
    | Start
    | Center
    | End
    | ...
}
```

**功能：** 菜单对齐类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[MenuAlignType](#enum-menualigntype)>

### Start

```cangjie
Start
```

**功能：** 按照语言方向起始端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 按照语言方向末端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(MenuAlignType)

```cangjie
public operator func ==(other: MenuAlignType): Bool
```

**功能：** 判断两个MenuAlignType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MenuAlignType](#enum-menualigntype)|是|-|要比较的另一个MenuAlignType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(MenuAlignType)

```cangjie
public operator func !=(other: MenuAlignType): Bool
```

**功能：** 判断两个MenuAlignType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MenuAlignType](#enum-menualigntype)|是|-|要比较的另一个MenuAlignType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|