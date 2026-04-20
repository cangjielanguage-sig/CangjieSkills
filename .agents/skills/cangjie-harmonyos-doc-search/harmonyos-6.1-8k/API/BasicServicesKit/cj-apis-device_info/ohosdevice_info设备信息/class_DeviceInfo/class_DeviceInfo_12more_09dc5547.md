## class DeviceInfo

```cangjie
public class DeviceInfo {}
```

**功能：** 提供终端设备信息查询方法。

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop ODID

```cangjie
public static prop ODID: String
```

**功能：** 开发者匿名设备标识符。例如“1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX”。

ODID值会在以下场景重新生成：

- 手机恢复出厂设置。

- 同一设备上同一个开发者(developerId相同)的应用全部卸载后重新安装时。

ODID生成规则：

- 根据签名信息里developerId解析出的groupId生成，developerId规则为groupId.developerId，若无groupId则取整个developerId作为groupId。

- 同一设备上运行的同一个开发者(developerId相同)的应用，ODID相同。

- 同一个设备上不同开发者(developerId不同)的应用，ODID不同。

- 不同设备上同一个开发者(developerId相同)的应用，ODID不同。

- 不同设备上不同开发者(developerId不同)的应用，ODID不同。

> **说明：**
>
> 数据长度为37字节。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop abiList

```cangjie
public static prop abiList: String
```

**功能：** 应用二进制接口（Abi）。例如“arm64-v8a”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop bootloaderVersion

```cangjie
public static prop bootloaderVersion: String
```

**功能：** Bootloader版本号。例如“bootloader”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop brand

```cangjie
public static prop brand: String
```

**功能：** 设备品牌名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildHost

```cangjie
public static prop buildHost: String
```

**功能：** 构建主机。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildRootHash

```cangjie
public static prop buildRootHash: String
```

**功能：** 构建版本Hash。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildTime

```cangjie
public static prop buildTime: String
```

**功能：** 构建时间。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildType

```cangjie
public static prop buildType: String
```

**功能：** 构建类型。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildUser

```cangjie
public static prop buildUser: String
```

**功能：** 构建用户。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop buildVersion

```cangjie
public static prop buildVersion: Int32
```

**功能：** Build版本号，标识编译构建的版本号，值为osFullName中的第四位数值，建议直接使用deviceInfo.buildVersion获取，可提升效率，不建议开发者自主解析osFullName获取。例如“1”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop deviceType

```cangjie
public static prop deviceType: String
```

**功能：** 设备类型。详细请参考[deviceTypes标签](../../cj-start/basic-knowledge/cj-module-configuration-file.md#devicetypes标签)。例如“<!--RP1-->tablet<!--RP1End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22