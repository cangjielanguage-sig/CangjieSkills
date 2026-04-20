## enum OnceType

```cangjie
public enum OnceType <: Equatable<OnceType> & ToString {
    | ToastShow
    | DialogShow
    | ...
}
```

**功能：** 控件的类型。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**父类型：**

- Equatable\<OnceType>
- ToString

### DialogShow

```cangjie
DialogShow
```

**功能：** dialog控件类型。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### ToastShow

```cangjie
ToastShow
```

**功能：** toast控件类型。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### func !=(OnceType)

```cangjie
public operator func !=(other: OnceType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnceType](#enum-oncetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(OnceType)

```cangjie
public operator func ==(other: OnceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OnceType](#enum-oncetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## enum ResizeDirection

```cangjie
public enum ResizeDirection {
    | Left
    | Right
    | Up
    | Down
    | LeftUp
    | LeftDown
    | RightUp
    | RightDown
    | ...
}
```

**功能：** 窗口调整大小的方向。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Down

```cangjie
Down
```

**功能：** 下方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Left

```cangjie
Left
```

**功能：** 左方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### LeftDown

```cangjie
LeftDown
```

**功能：** 左下方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### LeftUp

```cangjie
LeftUp
```

**功能：** 左上方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 右方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### RightDown

```cangjie
RightDown
```

**功能：** 右下方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### RightUp

```cangjie
RightUp
```

**功能：** 右上方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Up

```cangjie
Up
```

**功能：** 上方。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

## enum UiDirection

```cangjie
public enum UiDirection {
    | Left
    | Right
    | Up
    | Down
    | ...
}
```

**功能：** 进行抛滑等UI操作时的方向。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Down

```cangjie
Down
```

**功能：** 向下。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Left

```cangjie
Left
```

**功能：** 向左。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 向右。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### Up

```cangjie
Up
```

**功能：** 向上。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22