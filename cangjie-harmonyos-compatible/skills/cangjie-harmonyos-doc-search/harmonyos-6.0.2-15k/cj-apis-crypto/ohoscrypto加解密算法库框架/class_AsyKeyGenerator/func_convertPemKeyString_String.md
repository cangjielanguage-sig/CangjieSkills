### func convertPemKey(?String, ?String)

```cangjie
public func convertPemKey(pubKey: ?String, priKey: ?String): KeyPair
```

**功能：** 获取指定数据生成非对称密钥。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pubKey|?String|是|-|指定的公钥材料。如果公钥不需要转换，可直接传入None。|
|priKey|?String|是|-|指定的私钥材料。如果私钥不需要转换，可直接传入None。注：公钥和私钥材料不能同时为None。|

**返回值：**

|类型|说明|
|:----|:----|
|[KeyPair](#class-keypair)|非对称密钥。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17630001|crypto operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let priKeyPkcs1Str1024 = "-----BEGIN RSA PRIVATE KEY-----\n"
    + "MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n"
    + "Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n"
    + "YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n"
    + "AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n"
    + "LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n"
    + "7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n"
    + "D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n"
    + "e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n"
    + "a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n"
    + "MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n"
    + "DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n"
    + "qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n"
    + "akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n"
    + "-----END RSA PRIVATE KEY-----\n"
let publicPkcs1Str1024 = "-----BEGIN RSA PUBLIC KEY-----\n"
    + "MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n"
    + "h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n"
    + "SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n"
    + "-----END RSA PUBLIC KEY-----\n"
let asyKeyGenerator = createAsyKeyGenerator('RSA1024')
let keyPairData = asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024)
```