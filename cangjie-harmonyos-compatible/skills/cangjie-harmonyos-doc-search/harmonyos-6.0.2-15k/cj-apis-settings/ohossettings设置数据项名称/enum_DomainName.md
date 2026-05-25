## enum DomainName

```cangjie
public enum DomainName <: ToString {
    | DEVICE_SHARED
    | USER_PROPERTY
    | ...
}
```

**功能：** 提供查询的域名。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### DEVICE_SHARED

```cangjie
DEVICE_SHARED
```

**功能：** 设备属性共享域。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### USER_PROPERTY

```cangjie
USER_PROPERTY
```

**功能：** 为用户属性域。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回查询的域名对应字符串。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 查询的域名对应字符串。 |