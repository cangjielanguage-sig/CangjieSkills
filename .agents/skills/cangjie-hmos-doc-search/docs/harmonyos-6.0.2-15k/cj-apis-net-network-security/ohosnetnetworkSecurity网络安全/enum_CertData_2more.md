## enum CertData

```cangjie
public enum CertData {
    | ArrayData(Array<Byte>)
    | StringData(String)
    | ...
}
```

**功能：** 表示证书内容的枚举类。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

### ArrayData(Array\<Byte>)

```cangjie
ArrayData(Array<Byte>)
```

**功能：** 表示二进制流格式的证书数据。

**起始版本：** 20

### StringData(String)

```cangjie
StringData(String)
```

**功能：** 表示字符串格式的证书数据。

**起始版本：** 20

## enum SecurityCertType

```cangjie
public enum SecurityCertType {
    | CertTypePem
    | CertTypeDer
    | ...
}
```

**功能：** 表示证书编码类型的枚举类。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

### CertTypeDer

```cangjie
CertTypeDer
```

**功能：** DER格式证书。

**起始版本：** 20

### CertTypePem

```cangjie
CertTypePem
```

**功能：** PEM格式证书。

**起始版本：** 20