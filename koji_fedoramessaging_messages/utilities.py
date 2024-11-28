# SPDX-FileCopyrightText: 2020-2024 Red Hat, Inc
#
# SPDX-License-Identifier: GPL-3.0-or-later

import datetime

_task_header_template = """Task {id} on {build_host}
Task Type: {method} ({arch})
Link: {url}
"""


def fill_task_template(task_info, files_base_url):
    params = {
        "id": task_info["id"],
        "build_host": task_info["host_name"] or "(unscheduled)",
        "method": task_info["method"],
        "arch": task_info["arch"],
        "url": task_info["url"],
    }
    retval = _task_header_template.format(**params)
    if task_info["result"]:
        # multi-values
        for kind in ["logs", "rpms", "srpms"]:
            if kind not in task_info["result"]:
                continue
            if not task_info["result"][kind]:
                continue
            retval += f"{kind}:\n"
            for item in task_info["result"][kind]:
                retval += f"  {files_base_url}/{item}\n"
        # single-values
        for kind in ["srpm"]:
            if kind not in task_info["result"]:
                continue
            item = task_info["result"][kind]
            retval += f"{kind}:\n  {files_base_url}/{item}\n"

    if task_info["children"]:
        retval += f"\nTask {task_info['id']} has the following sub-tasks:\n"
    for child in sorted(task_info["children"], key=lambda d: d.get("completion_time")):
        retval += "\n" + fill_task_template(child, files_base_url)

    return retval


def date_to_string(dt: str) -> str:
    fmt = "%a, %d %b %Y %H:%M:%S %Z"
    try:
        return datetime.datetime.fromisoformat(dt).strftime(fmt)
    except TypeError:
        return ""
