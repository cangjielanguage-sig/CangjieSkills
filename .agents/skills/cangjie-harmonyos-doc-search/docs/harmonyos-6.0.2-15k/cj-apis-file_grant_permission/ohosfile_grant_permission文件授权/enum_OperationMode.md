## enum OperationMode

```cangjie
public enum OperationMode <: Equatable<OperationMode> & ToString {
    | ReadMode
    | WriteMode
    | ...
}
```

**功能：** 枚举，授予或使能权限的URI访问模式。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**父类型：**

- Equatable\<OperationMode>
- ToString

**起始版本：** 20

### ReadMode

```cangjie
ReadMode
```

**功能：** 读权限。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### WriteMode

```cangjie
WriteMode
```

**功能：** 写权限。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### func !=(OperationMode)

```cangjie
public operator func !=(other: OperationMode): Bool
```

**功能：** 对访问模式进行判不等。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OperationMode](#enum-operationmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态不同，返回true，否则返回false。|

### func ==(OperationMode)

```cangjie
public operator func ==(other: OperationMode): Bool
```

**功能：** 对访问模式进行判等。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[OperationMode](#enum-operationmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果授权状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回访问模式的字符串表示。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|访问模式的字符串表示。|