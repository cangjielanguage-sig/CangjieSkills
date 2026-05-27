## enum AreaMode

```cangjie
public enum AreaMode <: Equatable<AreaMode> & ToString {
    | EL1
    | EL2
    | EL3
    | EL4
    | EL5
    | ...
}
```

**功能：** 数据加密等级。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**父类型：**

- Equatable\<AreaMode>

- ToString

### EL1

```cangjie
EL1
```

**功能：** 设备级加密区，设备开机后可访问的数据区。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### EL2

```cangjie
EL2
```

**功能：** 用户级加密区，设备开机，首次输入密码后才能够访问的数据区。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### EL3

```cangjie
EL3
```

**功能：** 用户级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，可读写；解锁后，可读写。

未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，可创建、可打开、可写不可读；解锁后，可创建、可打开、可读写。

### EL4

```cangjie
EL4
```

**功能：** 用户级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，不可读写；解锁后，可读写。

未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，不可创建；解锁后，可创建、可打开、可读写。

### EL5

```cangjie
EL5
```

**功能：** 应用级加密区，不同场景的文件权限如下：

已打开文件：锁屏时，可读写；解锁后，可读写。

未打开文件：锁屏时，调用Access接口获取保留密钥后，可打开、可读写，否则不可打开、不可读写；解锁后，可打开、可读写。

创建新文件：锁屏时，可创建、可打开、可读写；解锁后，可创建、可打开、可读写。

### func !=(AreaMode)

```cangjie
public operator func !=(other: AreaMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AreaMode](#enum-areamode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AreaMode)

```cangjie
public operator func ==(other: AreaMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AreaMode](#enum-areamode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|