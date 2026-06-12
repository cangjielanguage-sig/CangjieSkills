#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
import zipfile
import xml.sax.saxutils
from pathlib import Path
from typing import Any, Dict, List


STYLE_IDS = {
    "有效等价类": "style-valid-equivalence",
    "无效等价类": "style-invalid-equivalence",
    "边界值": "style-boundary-value",
}


def escape(text: Any) -> str:
    return xml.sax.saxutils.escape(str(text), {'"': "&quot;"})


def make_topic(title: Any, children: List[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    topic = {"title": str(title)}
    if children:
        topic["children"] = children
    return topic


def node_to_topics(node: Any) -> List[Dict[str, Any]]:
    if isinstance(node, dict):
        topics: List[Dict[str, Any]] = []
        for key, value in node.items():
            if isinstance(value, dict) and {"测试流程", "预期结果"}.issubset(value.keys()):
                result = str(value.get("预期结果", ""))
                flow = str(value.get("测试流程", ""))
                flow_children = [make_topic(result)] if result else None
                topics.append(make_topic(key, [make_topic(flow, flow_children)] if flow else None))
                continue

            children = node_to_topics(value)
            topics.append(make_topic(key, children))
        return topics
    if isinstance(node, list):
        return [make_topic(item, node_to_topics(item) if isinstance(item, (dict, list)) else None) for item in node]
    if node is None or str(node) == "":
        return []
    return [make_topic(node)]


def build_structure(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict) or not data:
        raise ValueError("JSON root must be a non-empty object")
    root_title = next(iter(data.keys()))
    root_body = data[root_title]
    return make_topic(root_title, node_to_topics(root_body))


def topic_xml(topic: Dict[str, Any], root: bool = False) -> str:
    topic_id = "root-topic" if root else "topic-" + uuid.uuid4().hex
    title = escape(topic.get("title", ""))
    style_id = STYLE_IDS.get(topic.get("title", ""))
    style_attr = f' style-id="{style_id}"' if style_id else ""
    children = topic.get("children") or []
    if not children:
        return f'<topic id="{topic_id}"{style_attr}><title>{title}</title></topic>'
    child_xml = "".join(topic_xml(child) for child in children)
    return (
        f'<topic id="{topic_id}"{style_attr}><title>{title}</title>'
        f'<children><topics type="attached">{child_xml}</topics></children></topic>'
    )


def write_xmind(structure: Dict[str, Any], output_file: str) -> str:
    if not output_file.endswith(".xmind"):
        output_file += ".xmind"
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<xmap-content xmlns="urn:xmind:xmap:xmlns:content:2.0" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:xlink="http://www.w3.org/1999/xlink" version="2.0">
  <sheet id="sheet-{uuid.uuid4().hex}">
    <title>{escape(structure.get("title", "测试用例设计"))}</title>
    {topic_xml(structure, root=True)}
  </sheet>
</xmap-content>
'''
    styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<xmap-styles xmlns="urn:xmind:xmap:xmlns:style:2.0" xmlns:fo="http://www.w3.org/1999/XSL/Format" version="2.0">
  <style id="style-valid-equivalence" type="topic"><topic-properties fo:color="#008000"/></style>
  <style id="style-invalid-equivalence" type="topic"><topic-properties fo:color="#FF0000"/></style>
  <style id="style-boundary-value" type="topic"><topic-properties fo:color="#0000FF"/></style>
</xmap-styles>
'''
    meta_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<meta xmlns="urn:xmind:xmap:xmlns:meta:2.0" version="2.0"><Author><Name>cangjie-testcase-xmind</Name></Author></meta>
'''
    manifest_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="urn:xmind:xmap:xmlns:manifest:1.0">
  <file-entry full-path="content.xml" media-type="text/xml"/>
  <file-entry full-path="styles.xml" media-type="text/xml"/>
  <file-entry full-path="meta.xml" media-type="text/xml"/>
</manifest>
'''
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("content.xml", content_xml.encode("utf-8"))
        archive.writestr("styles.xml", styles_xml.encode("utf-8"))
        archive.writestr("meta.xml", meta_xml.encode("utf-8"))
        archive.writestr("META-INF/manifest.xml", manifest_xml.encode("utf-8"))
    return str(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Cangjie testcase JSON to .xmind.")
    parser.add_argument("json_file")
    parser.add_argument("output_file", nargs="?")
    args = parser.parse_args()

    with open(args.json_file, "r", encoding="utf-8-sig") as handle:
        data = json.load(handle)
    output_file = args.output_file
    if not output_file:
        base = os.path.splitext(args.json_file)[0]
        output_file = base + ".xmind"
    output = write_xmind(build_structure(data), output_file)
    print(f"Successfully converted to XMind: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
