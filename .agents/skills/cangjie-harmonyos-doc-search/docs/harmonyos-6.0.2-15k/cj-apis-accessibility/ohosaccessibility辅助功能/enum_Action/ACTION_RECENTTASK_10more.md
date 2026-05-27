### ACTION_RECENTTASK

```cangjie
ACTION_RECENTTASK
```

**功能：** 表示打开最近任务操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SCROLLBACKWARD

```cangjie
ACTION_SCROLLBACKWARD
```

**功能：** 表示向后滚动操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SCROLLFORWARD

```cangjie
ACTION_SCROLLFORWARD
```

**功能：** 表示向前滚动操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SELECT

```cangjie
ACTION_SELECT
```

**功能：** 表示选择操作。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SETCURSORPOSITION

```cangjie
ACTION_SETCURSORPOSITION
```

**功能：** 表示设置光标位置操作，需配置参数offset。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SETSELECTION

```cangjie
ACTION_SETSELECTION
```

**功能：** 表示选择操作，需配置参数selectTextBegin、selectTextEnd、selectTextInForWard。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ACTION_SETTEXT

```cangjie
ACTION_SETTEXT
```

**功能：** 表示设置文本操作，需配置参数setText。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(Action)

```cangjie
public operator func !=(other: Action): Bool
```

**功能：** 对目标动作进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Action](#enum-action)|是|-|目标动作。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若目标动作不同，返回true，否则返回false。|

### func ==(Action)

```cangjie
public operator func ==(other: Action): Bool
```

**功能：** 对目标动作进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Action](#enum-action)|是|-|目标动作。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若目标动作相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将目标动作转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|目标动作的字符串表示。|