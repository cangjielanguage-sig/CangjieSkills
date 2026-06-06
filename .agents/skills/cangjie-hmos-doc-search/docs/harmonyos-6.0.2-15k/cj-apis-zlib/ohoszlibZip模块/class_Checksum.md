## class Checksum

```cangjie
public class Checksum {}
```

**功能：** 校验对象。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

### func crc32(UInt64, Array\<Byte>)

```cangjie
public func crc32(crc: UInt64, buf: Array<Byte>): UInt64
```

**功能：** 更新CRC-32校验，成功时返回更新后的CRC-32校验，失败时返回错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|crc|UInt64|是|CRC-32校验的初始值。|
|buf|Array\<Byte>|是|计算校验数据缓冲区。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回更新后的CRC-32校验。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let checksum = createChecksum()
let checksumData: Array<Byte> = [1, 2, 3, 4, 5]
let ret = checksum.crc32(0, checksumData)
```