## enum ReleaseStatus

```cangjie
public enum ReleaseStatus <: Equatable<ReleaseStatus> & ToString {
    | RELEASE_DENIED
    | RELEASE_GRANTED
    | ...
}
```

**功能：** 锁屏下敏感数据访问权限释放的状态。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**父类型：**

- Equatable\<ReleaseStatus>
- ToString

### RELEASE_DENIED

```cangjie
RELEASE_DENIED
```

**功能：** 拒绝锁屏下敏感数据访问权限的释放。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

### RELEASE_GRANTED

```cangjie
RELEASE_GRANTED
```

**功能：** 释放锁屏下敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

### func !=(ReleaseStatus)

```cangjie
public operator func !=(other: ReleaseStatus): Bool
```

**功能：** 对锁屏下敏感数据访问权限的释放状态进行判不等。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ReleaseStatus](#enum-releasestatus)|是|-|锁屏下敏感数据访问权限的释放状态。|

**返回值：**

|类型|说明|
| :---- | :---- |
|Bool|如果锁屏下敏感数据访问权限释放的状态不同，返回true，否则返回false。|

### func ==(ReleaseStatus)

```cangjie
public operator func ==(other: ReleaseStatus): Bool
```

**功能：** 对锁屏下敏感数据访问权限的释放状态进行判等。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ReleaseStatus](#enum-releasestatus)|是|-|锁屏下敏感数据访问权限的释放状态。|

**返回值：**

|类型|说明|
| :---- | :---- |
|Bool|如果锁屏下敏感数据访问权限释放的状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回锁屏下敏感数据访问权限的释放状态的字符串表示。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**返回值：**

|类型|说明|
| :--- | :--- |
|String|锁屏下敏感数据访问权限的释放状态的字符串表示。|