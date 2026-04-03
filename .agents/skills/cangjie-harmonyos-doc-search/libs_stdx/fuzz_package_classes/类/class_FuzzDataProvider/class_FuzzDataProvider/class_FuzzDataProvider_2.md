| 目标类型          | API                                  | 说明                                               |
|---------------|--------------------------------------|--------------------------------------------------|
| Bool          | consumeBool()                        | 获取 1 个 Bool，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| Array\<Bool>   | consumeBools(count: Int64)           | 获取 N 个 Bool，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| Byte          | consumeByte()                        | 获取 1 个 Byte，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| Array\<Byte>   | consumeBytes(count: Int64)           | 获取 N 个 Byte，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| UInt8         | consumeUInt8()                       | 获取 1 个 UInt8，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| UInt16        | consumeUInt16()                      | 获取 1 个 UInt16，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| UInt32        | consumeUInt32()                      | 获取 1 个 UInt32，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| UInt64        | consumeUInt64()                      | 获取 1 个 UInt64，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| Int8          | consumeInt8()                        | 获取 1 个 Int8，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| Int16         | consumeInt16()                       | 获取 1 个 Int16，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Int32         | consumeInt32()                       | 获取 1 个 Int32，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Int64         | consumeInt64()                       | 获取 1 个 Int64，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Float32         | consumeFloat32()                       | 获取 1 个 Float32，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Float64         | consumeFloat64()                       | 获取 1 个 Float64，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Array\<UInt8>  | consumeUInt8s(count: Int64)          | 获取 N 个 UInt8，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Array\<UInt16> | consumeUInt16s(count: Int64)         | 获取 N 个 UInt16，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| Array\<UInt32> | consumeUInt32s(count: Int64)         | 获取 N 个 UInt32，变异数据长度不足时，抛出 [ExhaustedE