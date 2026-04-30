### func compress2(Array\<Byte>, Array\<Byte>, CompressLevel, Int64)

```cangjie
public func compress2(dest: Array<Byte>, source: Array<Byte>, level: CompressLevel,
    sourceLen!: Int64 = 0): ZipOutputInfo
```

**功能：** 将源缓冲区压缩到目标缓冲区，成功时返回结果状态和目标缓冲区的总大小。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|默认值|说明|
|:---|:---|:---|:---|:---|
|dest|Array\<Byte>|是|-|目标缓冲区。|
|source|Array\<Byte>|是|-|目标缓冲区。|
|level|[CompressLevel](#enum-compresslevel)|是|-|压缩级别。|
|sourceLen|Int64|否|0|**命名参数。** 参考CompressLevel枚举定义。|

**返回值：**

|类型|说明|
|:----|:----|
|[ZipOutputInfo](#class-zipoutputinfo)|返回结果状态和目标缓冲区的总大小。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800004|ZStream error.|
  |17800007|Buffer error.|
  |17800009|Internal structure error.|

- IllegalArgumentException：参数校验错误。

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The parameter check failed.|参数校验错误。|请检查传入的参数是否正确。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let zip = createZip()
let arrayBufferIn = Array<Byte>(100, { i => UInt8(i)})
let data = zip.compressBound(Int32(arrayBufferIn.size))
let arrayBufferOut = Array<Byte>(Int64(data), repeat: 0)
var zipOutputInfo = zip.compress2(arrayBufferOut, arrayBufferIn, CompressLevel.COMPRESS_LEVEL_BEST_SPEED, sourceLen: 80)
AppLog.info("compress return state: ${zipOutputInfo.status}, destLen: ${zipOutputInfo.destLen}")
AppLog.info("compress arrayBufferOut: ${arrayBufferOut}")
let uncompressOut = Array<Byte>(100, repeat: 0)
zipOutputInfo = zip.uncompress(uncompressOut, arrayBufferOut)
AppLog.info("uncompress return state: ${zipOutputInfo.status}, destLen: ${zipOutputInfo.destLen}")
AppLog.info("uncompress Out: ${uncompressOut}")
```