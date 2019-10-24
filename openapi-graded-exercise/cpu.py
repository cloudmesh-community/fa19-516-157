import platform
import cpuinfo
import re

import subprocess

from flask import jsonify


def get_processor_name():
    p = cpuinfo.get_cpu_info()['brand']

    p_info = {"model": p}

    return jsonify(p_info)


def get_processor_cache(level):
    if level == "l2":
        cache = cpuinfo.get_cpu_info()['l2_cache_size']
        cache_info = {"l2": cache}
        return jsonify(cache_info)
    elif level == "l3":
        cache = cpuinfo.get_cpu_info()['l3_cache_size']
        cache_info = {"l3": cache}
        return jsonify(cache_info)
    else:
        cache_info = {"l2": cpuinfo.get_cpu_info()['l2_cache_size'],
                      "l3": cpuinfo.get_cpu_info()['l3_cache_size']}
        return jsonify({"caches": cache_info})
