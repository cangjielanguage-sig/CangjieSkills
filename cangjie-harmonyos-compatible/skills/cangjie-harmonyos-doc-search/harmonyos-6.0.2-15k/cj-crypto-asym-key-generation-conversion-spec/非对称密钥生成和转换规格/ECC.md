## ECC

ECC（Elliptic Curve Cryptography），是一种基于椭圆曲线数学的公钥密码算法。

椭圆曲线算法可以看作是定义在特殊集合下数的运算，当前算法库支持的ECC密钥均为Fp域的椭圆曲线，p为素数，Fp域也称素数域。

当前支持使用字符串参数和密钥参数两种方式生成ECC密钥，且支持通过曲线名生成公共密钥参数。

### 使用字符串参数生成

以字符串参数生成ECC密钥，具体的“字符串参数”由“非对称密钥算法”和“密钥长度”拼接而成，用于在创建非对称密钥生成器时，指定密钥规格。

| 非对称密钥算法 | 密钥长度（bit） | 曲线名 | 字符串参数 | API版本 |
| -------- | -------- | -------- | -------- | -------- |
| ECC | 224 | NID_secp224r1 | ECC224 | 12+ |
| ECC | 256 | NID_X9_62_prime256v1 | ECC256 | 12+ |
| ECC | 384 | NID_secp384r1 | ECC384 | 12+ |
| ECC | 521 | NID_secp521r1 | ECC521 | 12+ |
| ECC | 160 | NID_brainpoolP160r1 | ECC_BrainPoolP160r1 | 12+ |
| ECC | 160 | NID_brainpoolP160t1 | ECC_BrainPoolP160t1 | 12+ |
| ECC | 192 | NID_brainpoolP192r1 | ECC_BrainPoolP192r1 | 12+ |
| ECC | 192 | NID_brainpoolP192t1 | ECC_BrainPoolP192t1 | 12+ |
| ECC | 224 | NID_brainpoolP224r1 | ECC_BrainPoolP224r1 | 12+ |
| ECC | 224 | NID_brainpoolP224t1 | ECC_BrainPoolP224t1 | 12+ |
| ECC | 256 | NID_brainpoolP256r1 | ECC_BrainPoolP256r1 | 12+ |
| ECC | 256 | NID_brainpoolP256t1 | ECC_BrainPoolP256t1 | 12+ |
| ECC | 320 | NID_brainpoolP320r1 | ECC_BrainPoolP320r1 | 12+ |
| ECC | 320 | NID_brainpoolP320t1 | ECC_BrainPoolP320t1 | 12+ |
| ECC | 384 | NID_brainpoolP384r1 | ECC_BrainPoolP384r1 | 12+ |
| ECC | 384 | NID_brainpoolP384t1 | ECC_BrainPoolP384t1 | 12+ |
| ECC | 512 | NID_brainpoolP512r1 | ECC_BrainPoolP512r1 | 12+ |
| ECC | 512 | NID_brainpoolP512t1 | ECC_BrainPoolP512t1 | 12+ |
| ECC | 256 | NID_secp256k1 | ECC_Secp256k1 | 12+ |

> **注意：**
>
> 创建的ECC非对称密钥生成器，如果用于随机生成密钥，则生成的ECC密钥的规格与创建密钥生成器时参数中指定的密钥规格一致；如果用于密钥转换，则生成的ECC密钥的规格与密钥转换时参数中指定的密钥数据的密钥规格一致。

### 使用密钥参数生成

Fp域下的ECC密钥参数，包括：

- p：素数，用于确定Fp。
- a, b：确定椭圆曲线的方程。
- g：椭圆曲线的一个基点(base point)，可由gx，gy表示。
- n：基点g的阶(order)。
- h：余因子(cofactor)。
- sk：私钥，是一个随机整数，小于n。
- pk：公钥，是椭圆曲线上的一个点， pk = sk \* g。

当创建非对称密钥生成器时，对于指定公/私钥参数生成ECC密钥的支持情况如表所示：

√：表示需要指定这一列中的具体属性，来构成密钥参数。

|  | 公共参数 | 公钥参数 | 私钥参数 | 公私钥对参数 |
| -------- | -------- | -------- | -------- | -------- |
| fieldType | √ | √ | √ | √ |
| p | √ | √ | √ | √ |
| a | √ | √ | √ | √ |
| b | √ | √ | √ | √ |
| g | √ | √ | √ | √ |
| n | √ | √ | √ | √ |
| h | √ | √ | √ | √ |
| pk | N/A | √ | N/A | √ |
| sk | N/A | N/A | √ | √ |

> **说明：**
>
> - 当前ECC只支持Fp域，因此fieldType固定为"Fp"。fieldType和p构成了属性field，当前field只支持[ECFieldFp](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-ecfieldfp)。
>
> - g和pk为ECC曲线上的点，属于[Point](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-point)类型，需要指定具体X，Y坐标。

### 使用曲线名生成密钥参数

> **说明：**
>
> - 曲线名为要求输入的字符串参数，支持的曲线名请参见[ECC密钥字符串参数表](#使用字符串参数生成-1)中的“曲线名”一列。
>
> - 生成的公共密钥参数可以直接随机生成公私钥，也可用于构造公、私以及公私钥对密钥参数。