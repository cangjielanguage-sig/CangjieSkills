## enum PreconfigType

```cangjie
public enum PreconfigType {
    | Preconfig720p
    | Preconfig1080p
    | Preconfig4k
    | PreconfigHighQuality
    | ...
}
```

**功能：** 枚举，提供预配置的类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<PreconfigType>
- ToString

### Preconfig1080p

```cangjie
Preconfig1080p
```

**功能：** 1080P预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Preconfig4k

```cangjie
Preconfig4k
```

**功能：** 4K预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Preconfig720p

```cangjie
Preconfig720p
```

**功能：** 720P预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### PreconfigHighQuality

```cangjie
PreconfigHighQuality
```

**功能：** 高质量预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(PreconfigType)

```cangjie
public operator func !=(other: PreconfigType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigType](#enum-preconfigtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PreconfigType)

```cangjie
public operator func ==(other: PreconfigType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigType](#enum-preconfigtype)|是|-|另一个枚举值。|

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