#!/usr/bin/env python3
"""
ArkTS-Cangjie 互操作结构验证脚本

验证 HarmonyOS 混合工程的互操作文件结构是否完整且配置正确。

用法：
    python verify_interop_structure.py --module <module-name>
    python verify_interop_structure.py --module filedownloader --project-root /path/to/project
    python verify_interop_structure.py --module filedownloader --check-types
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class Colors:
    """终端颜色"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class InteropValidator:
    """互操作结构验证器"""

    def __init__(self, project_root: Path, module_name: str):
        self.project_root = project_root
        self.module_name = module_name
        self.module_path = project_root / module_name
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed: List[str] = []

    def validate_all(self, check_types: bool = False) -> bool:
        """执行所有验证"""
        print(f"{Colors.BOLD}验证 {self.module_name} 模块的互操作结构...{Colors.ENDC}\n")

        # 1. 验证模块目录存在
        if not self.module_path.exists():
            self.errors.append(f"模块目录不存在: {self.module_path}")
            return False

        # 2. 验证仓颉桥接类
        self._validate_bridge_class()

        # 3. 验证 loader 目录
        self._validate_loader_dir()

        # 4. 验证 types 目录
        self._validate_types_dir()

        # 5. 验证模块配置
        self._validate_module_config()

        # 5b. cjpm / build-profile / package.cj 互操作配置
        self._validate_interop_static_config()

        # 6. 验证 ArkTS 包装层
        self._validate_arkts_wrapper()

        # 7. 可选：验证类型映射
        if check_types:
            self._validate_type_mapping()

        # 输出结果
        return self._print_results()

    def _validate_bridge_class(self):
        """验证仓颉桥接类"""
        cangjie_dir = self.module_path / "src/main/cangjie"

        if not cangjie_dir.exists():
            self.errors.append(f"仓颉目录不存在: {cangjie_dir}")
            return

        self._validate_business_dir_layout(cangjie_dir)

        # 查找 Bridge.cj 文件
        bridge_files = list(cangjie_dir.glob("*Bridge.cj"))

        if not bridge_files:
            self.errors.append(f"未找到桥接类文件 (*Bridge.cj) in {cangjie_dir}")
            return

        for bridge_file in bridge_files:
            self.passed.append(f"找到桥接类: {bridge_file.name}")

            # 检查文件内容
            content = bridge_file.read_text(encoding='utf-8')

            if '@Interop[ArkTS]' not in content:
                self.errors.append(f"{bridge_file.name}: 缺少 @Interop[ArkTS] 标记")
            else:
                self.passed.append(f"{bridge_file.name}: 包含 @Interop[ArkTS] 标记")

            if 'import ohos.ark_interop.*' not in content:
                self.errors.append(f"{bridge_file.name}: 缺少 'import ohos.ark_interop.*'")

            if 'import ohos.ark_interop_macro.*' not in content:
                self.errors.append(f"{bridge_file.name}: 缺少 'import ohos.ark_interop_macro.*'")

    def _validate_business_dir_layout(self, cangjie_dir: Path) -> None:
        """强制业务代码收口到 src/main/cangjie/business。"""
        business_dir = cangjie_dir / "business"
        if not business_dir.exists():
            self.errors.append(
                f"未找到业务目录: {business_dir}。请创建 src/main/cangjie/business 并将业务代码移入该目录。"
            )
            # continue to provide more hints even if missing

        # Exclude generated/known directories
        exclude = {"bridge", "mock", "loader", "types", "ark_interop_api", "business"}
        # Any .cj directly under src/main/cangjie (root) is considered misplaced business code
        root_cj = [p.name for p in cangjie_dir.glob("*.cj") if p.is_file()]
        if root_cj:
            self.errors.append(
                "发现仓颉源码散落在 src/main/cangjie 根目录（应迁移到 business/、bridge/ 或 mock/）："
                + ", ".join(root_cj)
            )

        misplaced: list[str] = []
        for p in cangjie_dir.rglob("*.cj"):
            if not p.is_file():
                continue
            rel = p.relative_to(cangjie_dir)
            if not rel.parts:
                continue
            top = rel.parts[0]
            if top in exclude:
                continue
            # ignore hidden / build artifacts by convention
            if top.startswith("."):
                continue
            misplaced.append(str(rel))
        if misplaced:
            self.errors.append(
                "发现业务代码不在 src/main/cangjie/business（且不在生成目录 bridge/mock/loader/types/ark_interop_api）："
                + ", ".join(sorted(misplaced))
            )

    def _validate_loader_dir(self):
        """验证 loader 目录"""
        loader_dir = self.module_path / "src/main/cangjie/loader"

        if not loader_dir.exists():
            self.errors.append(f"loader 目录不存在: {loader_dir}")
            return

        self.passed.append(f"loader 目录存在: {loader_dir}")

        # 检查 Index.d.ts
        index_dts = loader_dir / "Index.d.ts"
        if not index_dts.exists():
            self.errors.append(f"loader/Index.d.ts 不存在")
        else:
            self.passed.append("loader/Index.d.ts 存在")

            content = index_dts.read_text(encoding='utf-8')
            if 'requireCJLib' not in content:
                self.errors.append("loader/Index.d.ts: 缺少 requireCJLib 函数声明")
            else:
                self.passed.append("loader/Index.d.ts: 包含 requireCJLib 声明")

        # 检查 oh-package.json5
        oh_package = loader_dir / "oh-package.json5"
        if not oh_package.exists():
            self.errors.append(f"loader/oh-package.json5 不存在")
        else:
            self.passed.append("loader/oh-package.json5 存在")

            try:
                # 简单解析 JSON5（仅支持基本格式）
                content = oh_package.read_text(encoding='utf-8')
                content_clean = content.replace('\n', ' ').replace(',}', '}').replace(',]', ']')

                if '"name"' in content and '"libark_interop_loader.so"' in content:
                    self.passed.append("loader/oh-package.json5: name 字段正确")
                else:
                    self.errors.append("loader/oh-package.json5: name 字段不是 'libark_interop_loader.so'")
            except Exception as e:
                self.warnings.append(f"无法解析 loader/oh-package.json5: {e}")

    def _validate_types_dir(self):
        """验证 types 目录"""
        types_base = self.module_path / "src/main/cangjie/types"

        if not types_base.exists():
            self.errors.append(f"types 目录不存在: {types_base}")
            return

        # 查找 lib<module> 目录
        expected_dir_name = f"lib{self.module_name}"
        types_dir = types_base / expected_dir_name

        if not types_dir.exists():
            # 列出实际存在的目录
            actual_dirs = [d.name for d in types_base.iterdir() if d.is_dir()]
            self.errors.append(
                f"types/lib{self.module_name} 目录不存在。"
                f"实际存在的目录: {actual_dirs if actual_dirs else '无'}"
            )
            return

        self.passed.append(f"types/{expected_dir_name} 目录存在")

        # 检查 Index.d.ts
        index_dts = types_dir / "Index.d.ts"
        if not index_dts.exists():
            self.errors.append(f"types/{expected_dir_name}/Index.d.ts 不存在")
        else:
            self.passed.append(f"types/{expected_dir_name}/Index.d.ts 存在")

            content = index_dts.read_text(encoding='utf-8')

            # 检查是否使用 declare
            if 'export declare class' in content:
                self.passed.append("类型声明使用 'export declare class'")
            elif 'export class' in content:
                self.errors.append("类型声明使用了 'export class' 而不是 'export declare class'")

            # 检查 CustomLib
            if 'interface CustomLib' in content or 'CustomLib' in content:
                self.passed.append("包含 CustomLib 接口定义")
            else:
                self.warnings.append("未找到 CustomLib 接口定义")

        # 检查 oh-package.json5
        oh_package = types_dir / "oh-package.json5"
        if not oh_package.exists():
            self.errors.append(f"types/{expected_dir_name}/oh-package.json5 不存在")
        else:
            self.passed.append(f"types/{expected_dir_name}/oh-package.json5 存在")

            try:
                content = oh_package.read_text(encoding='utf-8')
                expected_name = f'"lib{self.module_name}.so"'

                if expected_name in content:
                    self.passed.append(f"types oh-package.json5: name 字段是 {expected_name}")
                else:
                    self.errors.append(
                        f"types oh-package.json5: name 字段不是 {expected_name}"
                    )
            except Exception as e:
                self.warnings.append(f"无法解析 types oh-package.json5: {e}")

    def _validate_module_config(self):
        """验证模块配置"""
        oh_package = self.module_path / "oh-package.json5"

        if not oh_package.exists():
            self.errors.append(f"模块 oh-package.json5 不存在: {oh_package}")
            return

        self.passed.append("模块 oh-package.json5 存在")

        try:
            content = oh_package.read_text(encoding='utf-8')

            # 检查 main 字段
            if '"main"' in content:
                if '"./src/main/ets/Index.ets"' in content:
                    self.passed.append("main 字段正确: './src/main/ets/Index.ets'")
                else:
                    self.errors.append("main 字段不是 './src/main/ets/Index.ets'")
            else:
                self.errors.append("缺少 main 字段")

            # 检查 dependencies
            if '"dependencies"' in content:
                # 检查 libark_interop_loader.so
                if '"libark_interop_loader.so"' in content:
                    if '"file:src/main/cangjie/loader"' in content:
                        self.passed.append("libark_interop_loader.so 依赖配置正确")
                    else:
                        self.errors.append("libark_interop_loader.so 依赖路径不正确")
                else:
                    self.errors.append("缺少 libark_interop_loader.so 依赖")

                # 检查 lib<module>.so
                expected_lib = f'"lib{self.module_name}.so"'
                if expected_lib in content:
                    expected_path = f'"file:src/main/cangjie/types/lib{self.module_name}"'
                    if expected_path in content:
                        self.passed.append(f"lib{self.module_name}.so 依赖配置正确")
                    else:
                        self.errors.append(f"lib{self.module_name}.so 依赖路径不正确")
                else:
                    self.errors.append(f"缺少 lib{self.module_name}.so 依赖")
            else:
                self.errors.append("缺少 dependencies 字段")

        except Exception as e:
            self.warnings.append(f"无法解析模块 oh-package.json5: {e}")

    def _validate_interop_static_config(self) -> None:
        """校验 cjpm.toml、build-profile.json5、package.cj（与技能文档一致）。"""
        try:
            from interop_config_checks import validate_interop_config_for_cjpm
        except ImportError as e:
            self.warnings.append(f"无法加载 interop_config_checks: {e}")
            return

        cjpm = self.module_path / "src/main/cangjie/cjpm.toml"
        if not cjpm.is_file():
            self.warnings.append(
                "未找到 src/main/cangjie/cjpm.toml，跳过 cjpm / build-profile / package.cj 互操作配置校验。"
            )
            return

        msgs = validate_interop_config_for_cjpm(cjpm)
        if not msgs:
            self.passed.append("cjpm.toml / build-profile.json5 / package.cj 互操作配置校验通过")
            return
        for msg in msgs:
            self.errors.append(msg)

    def _validate_arkts_wrapper(self):
        """验证 ArkTS 包装层"""
        ets_dir = self.module_path / "src/main/ets"

        if not ets_dir.exists():
            self.errors.append(f"ets 目录不存在: {ets_dir}")
            return

        self.passed.append("ets 目录存在")

        # 检查 Index.ets
        index_ets = ets_dir / "Index.ets"
        if not index_ets.exists():
            self.errors.append("src/main/ets/Index.ets 不存在")
        else:
            self.passed.append("src/main/ets/Index.ets 存在")

        # 检查根目录的 Index.d.ets
        index_dets = self.module_path / "Index.d.ets"
        if not index_dets.exists():
            self.warnings.append("根目录 Index.d.ets 不存在")
        else:
            self.passed.append("根目录 Index.d.ets 存在")

    # 类型映射表：仓颉类型 -> TypeScript 类型
    TYPE_MAPPING = {
        # 数值类型
        'Int8': 'number',
        'Int16': 'number',
        'Int32': 'number',
        'Int64': 'number',
        'UInt8': 'number',
        'UInt16': 'number',
        'UInt32': 'number',
        'UInt64': 'number',
        'Float32': 'number',
        'Float64': 'number',
        # 布尔类型
        'Bool': 'boolean',
        'Boolean': 'boolean',
        # 字符串类型
        'String': 'string',
        'JSStringEx': 'string',
        # 无返回值
        'Unit': 'undefined',
        # 数组类型
        'JSArrayEx': 'Array',
        'Array': 'Array',
        # 映射类型
        'JSHashMapEx': 'Map',
        # 字节数组
        'ArrayByte': 'ArrayBuffer',
    }

    # 仓颉类型 -> 允许的 TypeScript 类型列表（用于联合类型匹配）
    TYPE_ALIASES = {
        'Unit': ['void', 'undefined'],
    }

    def _parse_cangjie_methods(self, content: str) -> Dict[str, Dict]:
        """解析仓颉文件中的方法签名

        返回格式: {
            'methodName': {
                'params': [('paramName', 'Type'), ...],
                'return': 'ReturnType'
            }
        }
        """
        methods = {}

        # 匹配 public func 方法定义
        # 支持以下格式:
        # public func methodName(param: Type): ReturnType { }
        # public func methodName(param: Type): ReturnType
        # public func methodName(): ReturnType
        # public func methodName(param: Type)  // 返回 Unit
        method_pattern = re.compile(
            r'public\s+func\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?::\s*([A-Za-z_]\w*(?:<[^>]+>)?))?',
            re.MULTILINE
        )

        for match in method_pattern.finditer(content):
            method_name = match.group(1)
            params_str = match.group(2).strip()
            return_type = match.group(3) if match.group(3) else 'Unit'

            # 解析参数
            params = []
            if params_str:
                # 分割参数，处理可能的泛型
                param_pattern = re.compile(r'([A-Za-z_]\w*)\s*:\s*([A-Za-z_]\w*(?:<[^>]+>)?)')
                for param_match in param_pattern.finditer(params_str):
                    param_name = param_match.group(1)
                    param_type = param_match.group(2)
                    params.append((param_name, param_type))

            methods[method_name] = {
                'params': params,
                'return': return_type
            }

        return methods

    def _parse_typescript_methods(self, content: str) -> Dict[str, Dict]:
        """解析 TypeScript 声明文件中的方法签名

        返回格式: {
            'methodName': {
                'params': [('paramName', 'Type'), ...],
                'return': 'ReturnType'
            }
        }
        """
        methods = {}

        # 匹配方法声明
        # 支持:
        # methodName(param: Type): ReturnType;
        # methodName(): ReturnType;
        method_pattern = re.compile(
            r'([A-Za-z_]\w*)\s*\(([^)]*)\)\s*:\s*([A-Za-z_]\w+(?:\s*\|\s*(?:[A-Za-z_]\w+|undefined))?)\s*;',
            re.MULTILINE
        )

        for match in method_pattern.finditer(content):
            method_name = match.group(1)
            params_str = match.group(2).strip()
            return_type = match.group(3).strip()

            # 解析参数
            params = []
            if params_str:
                param_pattern = re.compile(r'([A-Za-z_]\w*)\s*:\s*([^{};]+)')
                for param_match in param_pattern.finditer(params_str):
                    param_name = param_match.group(1)
                    param_type = param_match.group(2).strip()
                    params.append((param_name, param_type))

            methods[method_name] = {
                'params': params,
                'return': return_type
            }

        return methods

    def _check_type_compatibility(self, cangjie_type: str, ts_type: str) -> Tuple[bool, str]:
        """检查仓颉类型和 TypeScript 类型是否兼容

        返回: (是否兼容, 错误信息)
        """
        # 处理泛型类型
        cj_base = cangjie_type.split('<')[0].strip()
        ts_base = ts_type.split('<')[0].strip()

        # 处理联合类型 (T | undefined)
        if '|' in ts_type:
            parts = [p.strip() for p in ts_type.split('|')]
            # Option<T> 对应 T | undefined
            if cj_base == 'Option':
                inner_type = cangjie_type.split('<')[1].rstrip('>').strip() if '<' in cangjie_type else cangjie_type[1:]
                expected_inner = self.TYPE_MAPPING.get(inner_type, inner_type)
                if expected_inner in parts:
                    return True, ""
            # 检查是否任一类型匹配
            for part in parts:
                if part == 'undefined':
                    continue
                compatible, _ = self._check_type_compatibility(cangjie_type, part)
                if compatible:
                    return True, ""
            return False, f"类型不兼容: 仓颉 '{cangjie_type}' 无法映射到 TypeScript '{ts_type}'"

        # 检查 TYPE_ALIASES（如 Unit 可映射为 void 或 undefined）
        if cj_base in self.TYPE_ALIASES:
            if ts_base in self.TYPE_ALIASES[cj_base]:
                return True, ""
            expected_list = ' 或 '.join(self.TYPE_ALIASES[cj_base])
            return False, f"类型不匹配: 仓颉 '{cangjie_type}' 应映射为 TypeScript '{expected_list}'，但声明为 '{ts_type}'"

        # 检查基本类型映射
        expected_ts = self.TYPE_MAPPING.get(cj_base)
        if expected_ts:
            if ts_base == expected_ts:
                return True, ""
            return False, f"类型不匹配: 仓颉 '{cangjie_type}' 应映射为 TypeScript '{expected_ts}'，但声明为 '{ts_type}'"

        # 自定义类型需要完全一致
        if cangjie_type == ts_type:
            return True, ""

        # 警告：未知类型映射
        return True, f"警告: 未知类型映射 '{cangjie_type}' -> '{ts_type}'，请手动检查"

    def _validate_type_mapping(self):
        """验证类型映射（高级检查）

        比较 Bridge.cj 和 Index.d.ts 中的方法签名，验证：
        1. 方法名一致
        2. 参数数量一致
        3. 参数类型一致（仓颉 -> TypeScript）
        4. 返回类型一致
        """
        cangjie_dir = self.module_path / "src/main/cangjie"
        types_dir = self.module_path / f"src/main/cangjie/types/lib{self.module_name}"

        if not types_dir.exists():
            return

        bridge_files = list(cangjie_dir.glob("*Bridge.cj"))
        if not bridge_files:
            return

        # 读取 TypeScript 声明文件
        index_dts = types_dir / "Index.d.ts"
        if not index_dts.exists():
            self.warnings.append(f"类型验证: {index_dts} 不存在，跳过类型映射验证")
            return

        ts_content = index_dts.read_text(encoding='utf-8')
        ts_methods = self._parse_typescript_methods(ts_content)

        # 逐个验证每个桥接类
        for bridge_file in bridge_files:
            cj_content = bridge_file.read_text(encoding='utf-8')
            cj_methods = self._parse_cangjie_methods(cj_content)

            if not cj_methods:
                continue

            # 验证每个仓颉方法在 TypeScript 中都有对应
            for method_name, cj_sig in cj_methods.items():
                if method_name not in ts_methods:
                    self.errors.append(
                        f"类型验证: 仓颉方法 '{method_name}' ({bridge_file.name}) "
                        f"在 TypeScript 声明中未找到对应"
                    )
                    continue

                ts_sig = ts_methods[method_name]

                # 验证参数数量
                if len(cj_sig['params']) != len(ts_sig['params']):
                    self.errors.append(
                        f"类型验证: 方法 '{method_name}' 参数数量不匹配 - "
                        f"仓颉: {len(cj_sig['params'])} 个, TypeScript: {len(ts_sig['params'])} 个"
                    )
                    continue

                # 验证每个参数类型
                for i, ((cj_param_name, cj_type), (ts_param_name, ts_type)) in enumerate(
                    zip(cj_sig['params'], ts_sig['params'])
                ):
                    compatible, error_msg = self._check_type_compatibility(cj_type, ts_type)
                    if not compatible:
                        self.errors.append(
                            f"类型验证: 方法 '{method_name}' 第 {i+1} 个参数 '{cj_param_name}' "
                            f"类型不匹配 - {error_msg}"
                        )
                    elif error_msg:
                        self.warnings.append(
                            f"类型验证: 方法 '{method_name}' 第 {i+1} 个参数 - {error_msg}"
                        )

                # 验证返回类型
                compatible, error_msg = self._check_type_compatibility(
                    cj_sig['return'], ts_sig['return']
                )
                if not compatible:
                    self.errors.append(
                        f"类型验证: 方法 '{method_name}' 返回类型不匹配 - {error_msg}"
                    )
                elif error_msg:
                    self.warnings.append(f"类型验证: 方法 '{method_name}' 返回类型 - {error_msg}")

            # 记录通过验证的方法数量
            if cj_methods:
                verified_count = sum(
                    1 for m in cj_methods if m in ts_methods
                )
                self.passed.append(
                    f"类型验证: {bridge_file.name} 中 {verified_count}/{len(cj_methods)} 个方法通过验证"
                )

    def _print_results(self) -> bool:
        """打印验证结果"""
        print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}验证结果{Colors.ENDC}\n")

        # 通过的检查
        if self.passed:
            print(f"{Colors.GREEN}{Colors.BOLD}✅ 通过的检查 ({len(self.passed)}):{Colors.ENDC}")
            for item in self.passed:
                print(f"  {Colors.GREEN}✓{Colors.ENDC} {item}")
            print()

        # 警告
        if self.warnings:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  警告 ({len(self.warnings)}):{Colors.ENDC}")
            for item in self.warnings:
                print(f"  {Colors.YELLOW}!{Colors.ENDC} {item}")
            print()

        # 错误
        if self.errors:
            print(f"{Colors.RED}{Colors.BOLD}❌ 错误 ({len(self.errors)}):{Colors.ENDC}")
            for item in self.errors:
                print(f"  {Colors.RED}✗{Colors.ENDC} {item}")
            print()

        # 总结
        print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")

        if not self.errors:
            print(f"{Colors.GREEN}{Colors.BOLD}✅ 所有检查通过！互操作结构配置正确。{Colors.ENDC}\n")
            return True
        else:
            print(f"{Colors.RED}{Colors.BOLD}❌ 发现 {len(self.errors)} 个错误，请修复后重试。{Colors.ENDC}\n")
            return False

def main():
    parser = argparse.ArgumentParser(
        description="验证 ArkTS-Cangjie 互操作结构",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --module filedownloader
  %(prog)s --module entry --project-root /path/to/project
  %(prog)s --module filedownloader --check-types
        """
    )

    parser.add_argument(
        '--module',
        required=True,
        help='模块名称（如 filedownloader, entry）'
    )

    parser.add_argument(
        '--project-root',
        type=Path,
        default=Path.cwd(),
        help='项目根目录路径（默认：当前目录）'
    )

    parser.add_argument(
        '--check-types',
        action='store_true',
        help='额外检查类型映射一致性（实验性）'
    )

    args = parser.parse_args()

    # 验证项目根目录
    if not args.project_root.exists():
        print(f"{Colors.RED}错误: 项目根目录不存在: {args.project_root}{Colors.ENDC}")
        return 1

    # 创建验证器并运行
    validator = InteropValidator(args.project_root, args.module)
    success = validator.validate_all(check_types=args.check_types)

    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
