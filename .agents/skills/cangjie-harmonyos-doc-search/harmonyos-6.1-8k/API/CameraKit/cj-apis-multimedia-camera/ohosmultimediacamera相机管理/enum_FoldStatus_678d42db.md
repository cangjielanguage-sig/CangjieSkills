## enum FoldStatus

```cangjie
public enum FoldStatus {
    | NonFoldable
    | Expanded
    | Folded
    | ...
}
```

**功能：** 枚举，折叠机折叠状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<FoldStatus>
- ToString

### Expanded

```cangjie
Expanded
```

**功能：** 表示当前设备折叠状态为完全展开。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Folded

```cangjie
Folded
```

**功能：** 表示当前设备折叠状态为折叠。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### NonFoldable

```cangjie
NonFoldable
```

**功能：** 表示当前设备不可折叠。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(FoldStatus)

```cangjie
public operator func !=(other: FoldStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FoldStatus)

```cangjie
public operator func ==(other: FoldStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|