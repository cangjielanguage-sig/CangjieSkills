### 枚举

|                 枚举名             |                功能                |
| --------------------------------- | ---------------------------------- |
| [DiagReportLevel](./ast_package_api/ast_package_enums.md#enum-diagreportlevel) | 表示报错接口的信息等级，支持 `ERROR` 和 `WARNING` 两种格式。|
| [ImportKind](./ast_package_api/ast_package_enums.md#enum-importkind) | 表示导入语句的类型，包括单导入、别名导入、全导入和多导入四种类型。|
| [TokenKind](./ast_package_api/ast_package_enums.md#enum-tokenkind) | 表示仓颉编译内部所有的词法结构，包括符号、关键字、标识符、换行等。|

### 结构体

|                 结构体名           |                功能                |
| --------------------------------- | ---------------------------------- |
| [Position](./ast_package_api/ast_package_structs.md#struct-position) | 表示位置信息的数据结构，包含文件 ID、行号和列号。|
| [Token](./ast_package_api/ast_package_structs.md#struct-token) | 词法单元类型。|

### 异常类

|                 异常类名           |                功能                |
| --------------------------------- | ---------------------------------- |
| [ASTException](./ast_package_api/ast_package_exceptions.md#class-astexception) | ast 库的异常类，在 ast 库调用过程中发生异常时使用。 |
| [MacroContextException](./ast_package_api/ast_package_exceptions.md#class-macrocontextexception) | ast 库的上下文宏异常类，在上下文宏的相关接口中发生异常时使用。 |
| [ParseASTException](./ast_package_api/ast_package_exceptions.md#class-parseastexception) | ast 库的解析异常类，在节点解析过程中发生异常时使用。 |