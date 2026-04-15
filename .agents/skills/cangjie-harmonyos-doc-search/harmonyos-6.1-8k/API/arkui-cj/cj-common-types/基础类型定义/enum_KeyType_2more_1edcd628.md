## enum KeyType

```cangjie
public enum KeyType <: Equatable<KeyType> {
    | Unknown
    | Down
    | Up
    | ...
}
```

**功能：** 按键的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<KeyType>

### Unknown

```cangjie
Unknown
```

**功能：** 未知类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Down

```cangjie
Down
```

**功能：** 按键按下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Up

```cangjie
Up
```

**功能：** 按键释放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(KeyType)

```cangjie
public operator func ==(other: KeyType): Bool
```

**功能：** 判断两个KeyType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyType](#enum-keytype)|是|-|要比较的另一个KeyType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(KeyType)

```cangjie
public operator func !=(other: KeyType): Bool
```

**功能：** 判断两个KeyType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyType](#enum-keytype)|是|-|要比较的另一个KeyType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ModifierKey

```cangjie
public enum ModifierKey <: Equatable<ModifierKey> {
    | Ctrl
    | Shift
    | Alt
    | ...
}
```

**功能：** 输入法修饰键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ModifierKey](#enum-modifierkey)>

### Ctrl

```cangjie
Ctrl
```

**功能：** 表示键盘上Ctrl键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Shift

```cangjie
Shift
```

**功能：** 表示键盘上Shift键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Alt

```cangjie
Alt
```

**功能：** 表示键盘上Alt键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ModifierKey)

```cangjie
public operator func ==(other: ModifierKey): Bool
```

**功能：** 判断两个ModifierKey枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ModifierKey](#enum-modifierkey)|是|-|要比较的另一个ModifierKey枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ModifierKey)

```cangjie
public operator func !=(other: ModifierKey): Bool
```

**功能：** 判断两个ModifierKey枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ModifierKey](#enum-modifierkey)|是|-|要比较的另一个ModifierKey枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|