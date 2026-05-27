## class UnitInfo

```cangjie
public class UnitInfo {
    public UnitInfo(
        public var unit: String,
        public var measureSystem: String
    )
}
```

**功能：** 度量衡单位信息。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var measureSystem

```cangjie
public var measureSystem: String
```

**功能：** 单位的度量体系，取值包括：“SI”, “US”, “UK”。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var unit

```cangjie
public var unit: String
```

**功能：** 单位的名称，如：“meter”, “inch”, "cup"等。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### UnitInfo(String, String)

```cangjie
public UnitInfo(
    public var unit: String,
    public var measureSystem: String
)
```

**功能：** 构建度量衡单位信息的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|unit|String|是|-|单位的名称，如：“meter”, “inch”, "cup"等。|
|measureSystem|String|是|-|单位的度量体系，取值包括：“SI”, “US”, “UK”。|

## enum NormalizerMode

```cangjie
public enum NormalizerMode <: Equatable<NormalizerMode> & ToString {
    | NFC
    | NFD
    | NFKC
    | NFKD
    | ...
}
```

**功能：** 文本正则化范式。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**父类型：**

- Equatable\<NormalizerMode>
- ToString

### NFC

```cangjie
NFC
```

**功能：** NFC范式。

**起始版本：** 19

### NFD

```cangjie
NFD
```

**功能：** NFD范式。

**起始版本：** 19

### NFKC

```cangjie
NFKC
```

**功能：** NFKC范式。

**起始版本：** 19

### NFKD

```cangjie
NFKD
```

**功能：** NFKD范式。

**起始版本：** 19

### func !=(NormalizerMode)

```cangjie
public operator func !=(other: NormalizerMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NormalizerMode](#enum-normalizermode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(NormalizerMode)

```cangjie
public operator func ==(other: NormalizerMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NormalizerMode](#enum-normalizermode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|