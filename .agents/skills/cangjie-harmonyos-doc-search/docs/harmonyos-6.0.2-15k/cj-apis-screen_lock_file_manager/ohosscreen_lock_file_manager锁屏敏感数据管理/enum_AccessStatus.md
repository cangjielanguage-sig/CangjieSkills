## enum AccessStatus

```cangjie
public enum AccessStatus <: Equatable<AccessStatus> & ToString {
    | ACCESS_DENIED
    | ACCESS_GRANTED
    | ...
}
```

**功能：** 锁屏下敏感数据访问权限申请的状态。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**父类型：**

- Equatable\<AccessStatus>
- ToString

### ACCESS_DENIED

```cangjie
ACCESS_DENIED
```

**功能：** 拒绝授予锁屏下敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

### ACCESS_GRANTED

```cangjie
ACCESS_GRANTED
```

**功能：** 授予锁屏下敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

### func !=(AccessStatus)

```cangjie
public operator func !=(other: AccessStatus): Bool
```

**功能：** 对锁屏下敏感数据访问权限的申请状态进行判不等。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AccessStatus](#enum-accessstatus)|是|-|锁屏下敏感数据访问权限的申请状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果锁屏下敏感数据访问权限申请的状态不同，返回true，否则返回false。|

### func ==(AccessStatus)

```cangjie
public operator func ==(other: AccessStatus): Bool
```

**功能：** 对锁屏下敏感数据访问权限的申请状态进行判等。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AccessStatus](#enum-accessstatus)|是|-|锁屏下敏感数据访问权限的申请状态。|

**返回值：**

|类型|说明|
| :---- | :---- |
|Bool|如果锁屏下敏感数据访问权限申请的状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回锁屏下敏感数据访问权限的申请状态的字符串表示。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**起始版本：** 19

**返回值：**

|类型|说明|
| :--- | :--- |
|String|锁屏下敏感数据访问权限的申请状态的字符串表示。|