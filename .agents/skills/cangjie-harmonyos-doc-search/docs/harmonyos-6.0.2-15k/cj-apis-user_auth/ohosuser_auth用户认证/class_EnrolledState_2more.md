## class EnrolledState

```cangjie
public class EnrolledState {
    public let credentialDigest: UInt64
    public let credentialCount: UInt16
}
```

**功能：** 表示用户注册凭据的状态。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### let credentialCount

```cangjie
public let credentialCount: UInt16
```

**功能：** 注册的凭据数量。

**类型：** UInt16

**读写能力：** 只读

**起始版本：** 19

### let credentialDigest

```cangjie
public let credentialDigest: UInt64
```

**功能：** 注册的凭据摘要，在凭据增加时随机生成。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

## class ReuseUnlockResult

```cangjie
public class ReuseUnlockResult {
    public ReuseUnlockResult(
        public let reuseMode: ReuseMode,
        public let reuseDuration: UInt64
    )
}
```

**功能：** 表示复用设备解锁结果。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### let reuseDuration

```cangjie
public let reuseDuration: UInt64
```

**功能：** 允许复用设备解锁结果的有效时长，有效时长的值应大于0，最大值为300000ms。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let reuseMode

```cangjie
public let reuseMode: ReuseMode
```

**功能：** 复用设备解锁结果的模式。

**类型：** [ReuseMode](#enum-reusemode)

**读写能力：** 只读

**起始版本：** 19

### ReuseUnlockResult(ReuseMode, UInt64)

```cangjie
public ReuseUnlockResult(
    public let reuseMode: ReuseMode,
    public let reuseDuration: UInt64
)
```

**功能：** 创建[ReuseUnlockResult](#class-reuseunlockresult)实例。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reuseMode|[ReuseMode](#enum-reusemode)|是|-|复用设备解锁结果的模式。|
|reuseDuration|UInt64|是|-|允许复用设备解锁结果的有效时长，有效时长的值应大于0，最大值为300000ms。|