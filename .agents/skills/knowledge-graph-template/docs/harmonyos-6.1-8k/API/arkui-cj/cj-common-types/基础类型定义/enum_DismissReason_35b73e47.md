## enum DismissReason

```cangjie
public enum DismissReason <: Equatable<DismissReason> {
    | PressBack
    | TouchOutside
    | CloseButton
    | SlideDown
    | ...
}
```

**功能：** 弹窗关闭原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[DismissReason](#enum-dismissreason)>

### PressBack

```cangjie
PressBack
```

**功能：** 点击三键back、左滑/右滑、键盘ESC。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TouchOutside

```cangjie
TouchOutside
```

**功能：** 点击遮障层时。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### CloseButton

```cangjie
CloseButton
```

**功能：** 点击了关闭按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SlideDown

```cangjie
SlideDown
```

**功能：** 下拉关闭。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(DismissReason)

```cangjie
public operator func ==(other: DismissReason): Bool
```

**功能：** 判断两个DismissReason枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DismissReason](#enum-dismissreason)|是|-|要比较的另一个DismissReason枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(DismissReason)

```cangjie
public operator func !=(other: DismissReason): Bool
```

**功能：** 判断两个DismissReason枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DismissReason](#enum-dismissreason)|是|-|要比较的另一个DismissReason枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|