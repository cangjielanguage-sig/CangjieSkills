## enum Action

```cangjie
public enum Action <: Equatable<Action> & ToString {
    | CANCEL
    | DOWN
    | UP
    |...
}
```

**功能：** 按键事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**父类型：**

- Equatable\<Action>
- ToString

### CANCEL

```cangjie
CANCEL
```

**功能：** 按键取消。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

### DOWN

```cangjie
DOWN
```

**功能：** 按键按下。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

### UP

```cangjie
UP
```

**功能：** 按键抬起。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

### func !=(Action)

```cangjie
public operator func !=(other: Action): Bool
```

**功能：** 对按键动作进行判不等。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Action](../InputKit/cj-apis-multimodalInput-keyEvent.md#enum-action)|是|-|按键动作。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果按键动作不同返回true，否则返回false。|

### func ==(Action)

```cangjie
public operator func ==(other: Action): Bool
```

**功能：** 对按键动作进行判等。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Action](../InputKit/cj-apis-multimodalInput-keyEvent.md#enum-action)|是|-|按键动作。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果按键动作相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将按键动作转换为字符串。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|