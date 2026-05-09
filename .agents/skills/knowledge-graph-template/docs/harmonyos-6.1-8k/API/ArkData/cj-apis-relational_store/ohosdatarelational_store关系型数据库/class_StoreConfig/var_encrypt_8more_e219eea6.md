### var encrypt

```cangjie
public var encrypt: Bool
```

**功能：**  指定数据库是否加密。

true：加密。

false：非加密。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var isReadOnly

```cangjie
public var isReadOnly: Bool
```

**功能：** 指定数据库是否只读，默认为数据库可读写。

true：只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。

false：允许对数据库进行读写操作。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 数据库文件名，也是数据库唯一标识符。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var persist

```cangjie
public var persist: Bool
```

**功能：** 指定数据库是否需要持久化。true表示持久化，false表示不持久化，即内存数据库。

内存数据库不支持加密、backup、restore、跨进程访问及分布式能力，securityLevel属性会被忽略。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var pluginLibs

```cangjie
public var pluginLibs: Array<String>
```

**功能：** 表示包含有fts（Full-Text Search，即全文搜索引擎）等能力的动态库名的数组。

使用约束：

1. 动态库名的数量限制最多为16个，如果超过该数量会开库失败，返回错误。

2. 动态库名需为本应用沙箱路径下或系统路径下的动态库，如果动态库无法加载会开库失败，返回错误。

3. 动态库名需为完整路径，用于被sqlite加载。

    样例：[context.bundleCodeDir+ "/libs/arm64/" + libtokenizer.so]，其中context.bundleCodeDir是应用沙箱对应的路径，"/libs/arm64/"表示子目录，libtokenizer.so表示动态库的文件名。当此参数不填时，默认不加载动态库。

4. 动态库需要包含其全部依赖，避免依赖项丢失导致无法运行。

例如：在ndk工程中，使用默认编译参数构建libtokenizer.so，此动态库依赖c++标准库。在加载此动态库时，由于namespace与编译时不一致，链接到了错误的libc++_shared.so，导致__emutls_get_address符号找不到。要解决此问题，需在编译时静态链接c++标准库，具体请参见NDK工程构建概述。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var rootDir

```cangjie
public var rootDir: String
```

**功能：** 指定数据库根路径。

将从如下目录打开或删除数据库：rootDir + "/" + customDir。通过设置此参数打开的数据库为只读模式，不允许对数据库进行写操作，否则返回错误码801。配置此参数打开或删除数据库时，应确保对应路径下数据库文件存在，并且有读取权限，否则返回错误码14800010。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var securityLevel

```cangjie
public var securityLevel: RelationalStoreSecurityLevel
```

**功能：** 设置数据库安全级别。

**类型：** [RelationalStoreSecurityLevel](#enum-relationalstoresecuritylevel)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### var tokenizer

```cangjie
public var tokenizer: Tokenizer
```

**功能：** 指定用户在fts场景下使用哪种分词器。

当此参数不填时，则在fts下不支持中文以及多国语言分词，但仍可支持英文分词。

**类型：** [Tokenizer](#enum-tokenizer)

**读写能力：** 可读写

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22