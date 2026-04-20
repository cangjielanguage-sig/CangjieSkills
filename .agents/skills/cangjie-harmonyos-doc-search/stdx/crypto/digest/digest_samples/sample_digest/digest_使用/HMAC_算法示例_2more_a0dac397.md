## HMAC 算法示例

> **说明**
>
> 目前只支持 HMAC-SHA512。

### 调用 HMAC-SHA512 成员函数

示例：

<!-- verify -->
```cangjie
import stdx.crypto.digest.*
import stdx.encoding.hex.*

main() {
    var algorithm: HashType = HashType.SHA512
    var key: Array<UInt8> = "cangjie".toArray()
    var data1: Array<UInt8> = "123".toArray()
    var data2: Array<UInt8> = "456".toArray()
    var data3: Array<UInt8> = "789".toArray()
    var data4: Array<UInt8> = "123456789".toArray()
    var hmac = HMAC(key, algorithm)
    hmac.write(data1)
    hmac.write(data2)
    hmac.write(data3)
    var md1: Array<Byte> = hmac.finish()
    var result1: String = toHexString(md1)
    println(result1)

    hmac.reset()
    hmac.write(data4)
    var md2: Array<Byte> = hmac.finish()
    var result2: String = toHexString(md2)
    println(result2)
    println(HMAC.equal(md1, md2))
    return 0
}
```

运行结果：

```text
2bafeb53b60a119d38793a886c7744f5027d7eaa3702351e75e4ff9bf255e3ce296bf41f80adda2861e81bd8efc52219df821852d84a17fb625e3965ebf2fdd9
2bafeb53b60a119d38793a886c7744f5027d7eaa3702351e75e4ff9bf255e3ce296bf41f80adda2861e81bd8efc52219df821852d84a17fb625e3965ebf2fdd9
true
```

## SM3 算法示例

### 调用 SM3 成员函数

示例：

<!-- verify -->
```cangjie
import stdx.crypto.digest.*
import std.convert.*
import std.crypto.digest.*
import stdx.encoding.hex.*

main() {
    var str: String = "helloworld"
    var sm3Instance = SM3()
    sm3Instance.write(str.toArray())
    var md: Array<Byte> = sm3Instance.finish()
    var result: String = toHexString(md)
    println(result)
    return 0
}
```

运行结果：

```text
c70c5f73da4e8b8b73478af54241469566f6497e16c053a03a0170fa00078283
```