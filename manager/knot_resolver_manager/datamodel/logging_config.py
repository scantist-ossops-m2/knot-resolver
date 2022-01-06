from typing import List, Optional

from typing_extensions import Literal, TypeAlias

from knot_resolver_manager.utils import SchemaNode

LogLevelEnum = Literal["crit", "err", "warning", "notice", "info", "debug"]
LogTargetEnum = Literal["syslog", "stderr", "stdout"]
LogGroupsEnum: TypeAlias = Literal[
    "manager",
    "system",
    "cache",
    "io",
    "net",
    "ta",
    "tasent",
    "tasign",
    "taupd",
    "tls",
    "gnutls",
    "tls_cl",
    "xdp",
    "zimprt",
    "zscann",
    "doh",
    "dnssec",
    "hint",
    "plan",
    "iterat",
    "valdtr",
    "resolv",
    "select",
    "zonecut",
    "cookie",
    "statis",
    "rebind",
    "worker",
    "policy",
    "daf",
    "timejm",
    "timesk",
    "graphi",
    "prefil",
    "primin",
    "srvstl",
    "wtchdg",
    "nsid",
    "dnstap",
    "tests",
    "dotaut",
    "http",
    "contrl",
    "module",
    "devel",
    "reqdbg",
]


class LoggingSchema(SchemaNode):
    level: LogLevelEnum = "notice"
    target: Optional[LogTargetEnum] = None
    groups: Optional[List[LogGroupsEnum]] = None
