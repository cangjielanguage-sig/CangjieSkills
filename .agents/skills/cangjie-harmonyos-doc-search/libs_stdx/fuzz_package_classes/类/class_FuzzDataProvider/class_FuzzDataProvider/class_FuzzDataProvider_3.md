xception](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| Array\<UInt64> | consumeUInt64s(count: Int64)         | 获取 N 个 UInt64，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。       |
| Array\<Int8>   | consumeInt8s(count: Int64)           | 获取 N 个 Int8，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| Array\<Int16>  | consumeInt16s(count: Int64)          | 获取 N 个 Int16，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Array\<Int32>  | consumeInt32s(count: Int64)          | 获取 N 个 Int32，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Array\<Int64>  | consumeInt64s(count: Int64)          | 获取 N 个 Int64，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。        |
| Rune          | consumeRune()                        | 获取 1 个 Rune，变异数据长度不足时，抛出 [ExhaustedException](fuzz_package_exceptions.md#class-exhaustedexception)。         |
| String        | consumeAsciiString(maxLength: Int64) | 获取 1 个纯 ASCII 的 String，长度为 0 到 maxLength，可以为 0。           |
| String        | consumeString(maxLength: Int64)      | 获取 1 个 UTF8 String，长度为 0 到 maxLength，可以为 0。             |
| Array\<UInt8>  | consumeAll()                         | 将 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 中的剩余内容全部转化为字节数组。                    |
| String        | consumeAllAsAscii()                  | 将 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 中的剩余内容全部转化为纯 ASCII 的 String。           |
| String        | consumeAllAsString()                 | 将 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 中的剩余内容全部转化为 UTF8 String，末尾多余的字符不会被消耗。 |