## class KeyPair

```cangjie
public class KeyPair {}
```

**功能：** 非对称密钥对，包含：公钥与私钥。

可以通过非对称密钥生成器[AsyKeyGenerator](#class-asykeygenerator)、[AsyKeyGeneratorBySpec](#class-asykeygeneratorbyspec)来生成。

> **说明：**
>
> - KeyPair对象中的pubKey对象和priKey对象，作为KeyPair对象中的一个参数存在，当离开KeyPair对象作用域时，其内部对象可能被析构。
> - 使用时应持有KeyPair对象的引用，而非内部pubKey或priKey对象的引用。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop priKey

```cangjie
public prop priKey: PriKey
```

**功能：** 私钥。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [PriKey](#class-prikey)

**读写能力：** 只读

**起始版本：** 19

### prop pubKey

```cangjie
public prop pubKey: PubKey
```

**功能：** 公钥。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [PubKey](#class-pubkey)

**读写能力：** 只读

**起始版本：** 19