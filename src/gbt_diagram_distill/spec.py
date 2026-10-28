"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "diagram_distill",
 "domain": "creation",
 "desc": "**蒸馏件**（不是外挂）：把吞入件 wheresryan22/anatomy（MIT · 7551★ · 零依赖 Node）的 **craft 取法**提炼成我们自己的**概念物化图判据**：①概念物化（先把抽象概念发明成一个「它怎么转就是这个概念」的物理机构）②单一数源（图上每个数来自同一个驱动模型的读数）③几何不变量要有审计（不穿模，静止/拆解/过渡每一帧都查）④逐关节自检（交付前自己放大挨个关节看）。op=source 现读胶囊（尺寸+逐文件 sha256）· op=provenance 逐条指回原话（含**未蒸馏**两行：33 figures 画廊/WebGL/3D 引擎不取 · npx 安装不取）。**零作用域**：无 subprocess / 无 urllib / 无写盘。边界：接入端 ≡ 我们**已有**的出图位（code_art / scene_anchor / projection_card）；本位只蒸取法，**不建平行位**。op=method/source/provenance/where",
 "handler": "diagram_distill",
 "safe": true,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "method",
  "source",
  "provenance",
  "where"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
