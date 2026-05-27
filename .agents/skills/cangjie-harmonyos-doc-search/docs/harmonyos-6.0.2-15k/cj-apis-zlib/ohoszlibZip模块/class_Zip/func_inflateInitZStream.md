### func inflateInit(ZStream)

```cangjie
public func inflateInit(strm: ZStream): ReturnStatus
```

**功能：** 初始化内部流状态以进行解压缩，成功时返回结果状态。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|strm|[ZStream](#class-zstream)|是|参考[ZStream定义](#class-zstream)。|

**返回值：**

|类型|说明|
|:----|:----|
|[ReturnStatus](#enum-returnstatus)|返回结果状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
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
let arrayBufferOut = Array<Byte>(300, repeat: 0)
let zstream = ZStream(
    nextIn: arrayBufferIn,
    availableIn: UInt32(arrayBufferIn.size),
    nextOut: arrayBufferOut,
    availableOut: UInt32(arrayBufferOut.size)
)
var ret = zip.deflateInit2(zstream, CompressLevel.COMPRESS_LEVEL_BEST_SPEED, CompressMethod.Deflated, 15,
    MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
AppLog.info("deflateInit2 return status: ${ret}")
ret = zip.deflate(ZStream(), CompressFlushMode.Finish)
AppLog.info("deflate return status: ${ret}")
ret = zip.deflateEnd(ZStream())
AppLog.info("deflateEnd return status: ${ret}")

let decompOut = Array<Byte>(100, repeat: 0)
let retStream = zip.getZStream()
ret = zip.inflateInit(ZStream(nextIn: arrayBufferOut, availableIn: UInt32(retStream.totalOut.getOrThrow()),
    nextOut: decompOut, availableOut: UInt32(decompOut.size)))
AppLog.info("inflateInit return status: ${ret}")
ret = zip.inflate(ZStream(), CompressFlushMode.Finish)
AppLog.info("inflate return status: ${ret}")
ret = zip.inflateEnd(ZStream())
AppLog.info("inflateEnd return status: ${ret}")
```